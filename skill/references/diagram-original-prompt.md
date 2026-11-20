# Original retrieval-diagram prompt

Recovered from the actual image-generation call recorded at **2026-11-13T04:52:46.658Z** during the canonical ReasoningBank presentation production. This is an **original recovered prompt**, not a newly reconstructed template. The relevant invocation used `image_gen__imagegen` with `transparent_background: false`; the third prompt combined the shared prefix and the retrieval-specific composition below, separated by one space.

## Shared style prefix — exact text

```text
Generate one very wide academic flow diagram for an ICLR computer science paper. Aspect ratio 3:1, tightly composed on pure white. Paper typography: crisp Arial, bold navy labels, pale UNC-blue fills, very thin muted blue-gray outlines and clean simple arrowheads. Small monochrome line icons are fine. No extraneous text or caption, no overall title, no figure number, no shadows, no gradients, no decoration. Large legible type at projected size, preserve exactly the supplied words and do not add or repeat words.
```

## Retrieval composition — exact text

```text
Composition: a left-to-right flow of three academic blocks linked by thin right arrows. First block headed “Embed new query” and one example below “What did I buy first?” Second, slightly wider block headed “Rank by cosine similarity” with exactly two rows: “1   When was my first purchase?” and “2   What is the return policy?” Highlight just row 1 in pale blue. Third block headed “Add linked atom to prompt” and one example below “Check the full order history”. The arrow to block 3 starts from the highlighted first-ranked row in block 2. Show no similarity scores, only the two rank numbers. Exactly 3 columns, no additional headings, icons optional only if they don't crowd out text. Fit complete exact wording in large clear type.
```

## Source identity and final asset

The **first-purchase task** derives from ReasoningBank Figure15. The new query, return-policy candidate, candidate ordering and exact atom wording are **authored teaching examples**; their ranking was not measured. Retrieval mechanics are explained from paper AppendixA.2 and the public WebArena implementation. This diagram is not an original paper figure, screenshot or experimental output.

The generated image was saved as `retrieve-first-purchase.png`, then cropped at **left0, top180, width2172, height370** to remove unused vertical margins. The final deck embeds `retrieve-first-purchase-cropped.png` with aspect-preserving containment inside a slide region at **x0.65, y4.82, w12, h2.28in**; it does not stretch the image to that region. Mechanism boxes above it and the title remain native PowerPoint objects.

The installed skill asset `assets/image-references/teaching-retrieval.png` is **byte-identical to this final cropped image**. Both have SHA256 `79201987bbb306d4f2d49ccf8586789a911104244be7c1a5093c9b16df443402`.

For new content, use these original words only as a reference for the authored original. Replace task-specific content deliberately and label an adapted prompt as a new adaptation. A request for “3:1” in the original prompt did not determine the final crop ratio.
