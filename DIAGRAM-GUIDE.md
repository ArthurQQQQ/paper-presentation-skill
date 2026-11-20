# Explain the paper's figures

**Original overview → focused panel → visible case → clear explanation.**

![Current production workflow](assets/readme/workflow-dark.svg)

## Current workflow

1. **Select the source.** Verify the paper version and figure/table number. Prefer author-provided originals or material from the same-version PDF.
2. **Reuse the template.** Place the source in the approved figure frame, preserving its aspect ratio. Reuse the original overview or zoom into a faithful original panel.
3. **Unfold the explanation.** Keep positions stable. At each step explain the input, operation, output, state and condition. Make the case’s meaningful change visible with necessary editable phrases: faithfully sourced or clearly hypothetical. Preserve original edges, labels, axes, units and comparison groups.
4. **Write the notes.** Record what to point at, how to read it, the transition, limitations and exact source. After edits or crops, synchronize these directions with the final image. Check projection-size readability.

Content figures use only original paper figures, tables and faithful crops. When the paper has no suitable figure, use a large-text page with spoken detail in notes. Do not generate illustrations or redraw mechanisms/results for a new talk.

Slide titles, conclusions and necessary short labels remain editable. Embedded paper images retain their original content; PNG labels are rasterized.

## Reference archive

![Dark README adaptation of the historical retrieval teaching example; candidate order is illustrative.](assets/readme/retrieval-dark.svg)

[See the actual historical figure and full slide](EXAMPLES.md).

The approved ReasoningBank deck combined a stationary overview, native explanation and embedded teaching figures. The figure above is a README adaptation of that historical example. Its query candidates, ordering and atom wording were teaching choices; the ranking was not measured.

Current talks reuse the layout with the new paper's own figures. The archived ImageGen prompt below documents how the original example was made; it is not the current production default. No image model or API adapter is bundled.

<details>
<summary>Historical ImageGen prompt · exact production text</summary>

Actual ImageGen call: **2026-11-13, 04:52:46.658 UTC**, opaque background. The prefix and composition were joined with one space.

### Shared style prefix

```text
Generate one very wide academic flow diagram for an ICLR computer science paper. Aspect ratio 3:1, tightly composed on pure white. Paper typography: crisp Arial, bold navy labels, pale UNC-blue fills, very thin muted blue-gray outlines and clean simple arrowheads. Small monochrome line icons are fine. No extraneous text or caption, no overall title, no figure number, no shadows, no gradients, no decoration. Large legible type at projected size, preserve exactly the supplied words and do not add or repeat words.
```

### Retrieval composition

```text
Composition: a left-to-right flow of three academic blocks linked by thin right arrows. First block headed “Embed new query” and one example below “What did I buy first?” Second, slightly wider block headed “Rank by cosine similarity” with exactly two rows: “1   When was my first purchase?” and “2   What is the return policy?” Highlight just row 1 in pale blue. Third block headed “Add linked atom to prompt” and one example below “Check the full order history”. The arrow to block 3 starts from the highlighted first-ranked row in block 2. Show no similarity scores, only the two rank numbers. Exactly 3 columns, no additional headings, icons optional only if they don't crowd out text. Fit complete exact wording in large clear type.
```

</details>

<details>
<summary>Source and embedding</summary>

Actual assets from the final 43-page ReasoningBank presentation. The first-purchase task derives from paper Figure 15. The new query, return-policy candidate, ordering and exact atom wording are authored teaching examples, not recorded retrieval output. The mechanism follows Appendix A.2 and the public WebArena implementation.

The generated image was cropped to **2172 × 370 px** at `(0,180)` to remove unused margins. Slide 15 contains it within `x=.65, y=4.82, w=12, h=2.28 in`, preserving its aspect ratio rather than stretching it. The skill retains this exact final crop as `assets/image-references/teaching-retrieval.png`.

This is an archival production record. Current talks reuse the template layout with figures from the paper being presented; this historical prompt does not authorize new generated content figures.

</details>
