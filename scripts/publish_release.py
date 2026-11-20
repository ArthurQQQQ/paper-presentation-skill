"""Assemble immutable reference assets with current instructions, then publish a draft.

No presentation rendering, model calls, credentials in the archive, or source-paper
data processing. The previous complete release is a checksum-pinned asset source.
"""

import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "release.json").read_text())
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "ArthurQQQQ/paper-presentation-skill")
VERSION = MANIFEST["version"]
SKILL = MANIFEST["skill_name"]
if not re.fullmatch(r"v\d+\.\d+\.\d+", VERSION):
    raise ValueError("Release version must be a stable semantic version")
if REPOSITORY != "ArthurQQQQ/paper-presentation-skill":
    raise ValueError("This release definition belongs to its original repository")


def request_json(path, *, method="GET", payload=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "paper-presentation-skill-release",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": "Bearer " + os.environ["GITHUB_TOKEN"],
    }
    body = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://api.github.com/repos/" + REPOSITORY + path,
        data=body, headers=headers, method=method,
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)


def assemble():
    url = (
        "https://github.com/" + REPOSITORY + "/releases/download/"
        + MANIFEST["base_release"] + "/" + MANIFEST["base_asset"]
    )
    with urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "paper-presentation-skill-release"}),
        timeout=120,
    ) as response:
        previous = response.read()
    if hashlib.sha256(previous).hexdigest() != MANIFEST["base_sha256"]:
        raise ValueError("Previous release archive checksum does not match")

    contents = {}
    with zipfile.ZipFile(io.BytesIO(previous)) as original:
        for item in original.infolist():
            path = PurePosixPath(item.filename)
            if path.is_absolute() or ".." in path.parts or path.parts[0] != SKILL:
                raise ValueError("Unexpected path in reference archive")
            relative = path.relative_to(SKILL)
            if any(part.startswith(".") for part in relative.parts):
                continue
            if relative.parts[0] not in {"assets", "examples"} and str(relative) != "README.md":
                continue
            if not item.is_dir():
                contents[item.filename] = original.read(item)

    # Replace the complete maintained instruction set; retain immutable assets
    # and optional historical demos from the checksum-pinned previous package.
    for path in list(contents):
        relative = PurePosixPath(path).relative_to(SKILL)
        if relative.parts[0] in {"references", "agents"} or str(relative) in {
            "SKILL.md", "artifact-template.json",
        }:
            del contents[path]
    for path in (ROOT / "skill").rglob("*"):
        if path.is_symlink():
            raise ValueError("Symlinks are not part of the portable skill")
        if path.is_file():
            relative = path.relative_to(ROOT / "skill").as_posix()
            if not (relative.endswith((".md", ".yaml", ".json"))):
                raise ValueError("Unexpected instruction source file")
            contents[SKILL + "/" + relative] = path.read_bytes()
    contents[SKILL + "/README.md"] = (
        "# ReasoningBank Research Slides\n\n"
        "Provide a paper and speaking/Q&A duration. The skill adapts depth and "
        "summarization, reuses the original layouts and paper figures, and puts "
        "details and sources in speaker notes.\n\n"
        "Move this folder into your personal Codex skills directory, usually "
        "`~/.codex/skills/`, then invoke `$" + SKILL + "`. Confirm any missing "
        "presenter name and school after the structure is set.\n\n"
        "[Duration planning](references/duration-planning.md) · "
        "[Content workflow](references/paper-to-talk.md) · "
        "[Original figure selection](references/image-playbook.md)\n\n"
        "The full reference deck and optional historical previews are included. "
        "No personal profile, credentials, or private test-paper files are bundled. "
        "Historical teaching images and prompts document the reference production; "
        "new content figures come from the paper being presented.\n"
    ).encode()

    required = [
        "SKILL.md", "artifact-template.json", "agents/openai.yaml",
        "references/duration-planning.md", "assets/reference.pptx", "assets/reference.pdf",
    ]
    if any(SKILL + "/" + name not in contents for name in required):
        raise ValueError("Complete package is missing a required file")
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    archive = output / ("reasoningbank-research-slides-" + VERSION + ".zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for name, data in sorted(contents.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data, compresslevel=6)
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    sums = output / "SHA256SUMS"
    sums.write_text(checksum + "  " + archive.name + "\n")
    print(json.dumps({"archive": archive.name, "bytes": archive.stat().st_size,
                      "files": len(contents), "sha256": checksum}), flush=True)
    return archive, sums


def publish(archive, sums):
    target = os.environ["GITHUB_SHA"]
    existing = next((r for r in request_json("/releases?per_page=100")
                     if r["tag_name"] == VERSION), None)
    if existing and not existing["draft"]:
        raise ValueError("Version already published; existing release is preserved")
    payload = {
        "tag_name": VERSION,
        "target_commitish": target,
        "name": MANIFEST["title"],
        "body": (ROOT / MANIFEST["notes_file"]).read_text(),
        "draft": True,
        "prerelease": False,
    }
    if existing:
        release = request_json("/releases/" + str(existing["id"]), method="PATCH", payload=payload)
    else:
        release = request_json("/releases", method="POST", payload=payload)
    upload_url = release["upload_url"].split("{", 1)[0]
    for path in (archive, sums):
        previous = next((a for a in release.get("assets", []) if a["name"] == path.name), None)
        expected_digest = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
        if previous:
            if previous.get("digest") == expected_digest:
                continue
            raise ValueError("Draft contains a different asset; refusing to overwrite")
        req = urllib.request.Request(
            upload_url + "?" + urllib.parse.urlencode({"name": path.name}),
            data=path.read_bytes(), method="POST",
            headers={"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"],
                     "User-Agent": "paper-presentation-skill-release",
                     "Content-Type": "application/octet-stream"},
        )
        with urllib.request.urlopen(req, timeout=180) as response:
            attached = json.load(response)
        if attached["state"] != "uploaded" or attached["size"] != path.stat().st_size:
            raise ValueError("Release attachment did not complete")
    completed = request_json("/releases/" + str(release["id"]), method="PATCH",
                             payload={"draft": False, "make_latest": "true"})
    print("Published " + completed["html_url"], flush=True)


if __name__ == "__main__":
    try:
        publish(*assemble())
    except urllib.error.HTTPError as error:
        # HTTP bodies can include useful errors; keep logs free of request headers.
        print("GitHub release HTTP error: " + str(error.code), file=sys.stderr)
        raise SystemExit(1)
