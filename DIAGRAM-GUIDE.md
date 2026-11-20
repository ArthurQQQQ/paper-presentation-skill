# 内置 diagram：从机制到嵌入页面

需要把论文机制、共享边界、状态变化或贯穿案例画成图时读本页。这里是随本 skill 分发的制作方法，不依赖另一份未安装的 diagram skill，也不是一个自动渲染引擎。具体制作使用当前报告的演示工具。

## 原稿实际怎么做

![最终第15页](showcase-mechanism.png)

第13–15页把三层组合在一起：右上固定总览及原生局部高亮；上方可编辑的对象、文字和连接；下方嵌入同一案例的蓝白教学图。最终稿的教学图是 PNG，图内文字不能当作可编辑文字。精确机制和结果图继续使用原生对象或真实来源。

![实际嵌入的检索案例图](showcase-diagram.png)

上图的候选与排序是教学示意，未测量相似度分数。新 query、两条候选与所选 atom 用来解释检索关系，不能当作真实运行记录。

[查看当时实际使用的原始 prompt](#original-retrieval-diagram-prompt)：已从原制作调用找回共同风格词与检索构图词，也记录了成品裁切和等比嵌入方式。改成新主题时，替换语义对象并标明是新适配，不把原词直接当成新论文事实。

## 先选关系，再选图

| 要让听众理解什么 | 适合的构图 | 必须核对的语义 |
|---|---|---|
| 数据或控制怎样流动 | 定向流程；分支写条件 | 箭头传递的对象，数据流与控制流的区别 |
| 什么发生了变化 | 对齐的前后状态 | 相同对象、变化字段与触发操作 |
| 哪些任务共享状态 | 泳道、边界与共享容器 | 归属、隔离；未共享的对象不画连线 |
| 一个操作怎么落地 | 同一输入走过机制的案例 | 输入、中间状态、输出，跨页术语一致 |
| 当前步骤处在全图哪里 | 固定总览加局部高亮 | 不改全图拓扑；高亮和正在讲的步骤一致 |

若一幅图承载多个推理依赖，先拆成几次揭示或几页。不要为了装下全部节点缩小正文。

## 图的最小交付规格

为每幅图保留一个简洁规格，和逐页设计合并即可：

```text
主旨与听众问题：
来源身份：论文原图 / 忠实重绘 / 教学示意 / 研究假设
节点：稳定 ID；显示标签；输入/输出/状态字段
边：起点 → 终点；传递什么；必要条件
边界：容器归属；哪些节点不能连接
布局：画布；对象区域；原生文字与图像的分工
展开：初始可见对象；每次揭示新增的一个理解依赖；最终静态状态
嵌入：插入区域；等比缩放；替代文字；讲者备注中的来源和限制
实际生成记录：工具、prompt、参考图、修改与最终素材；未生成时注明
```

以“query similarity”案例为例：

| 阶段 | 输入 → 操作 → 输出 | 视觉表达 |
|---|---|---|
| 编码 | 新任务 query → embedding → 查询向量 | 左列；放大镜只是图标，不新增检索步骤 |
| 排序 | 查询向量与历史 query 向量 → cosine 排序 → 选中的历史 experience | 中列；只高亮所选候选，不虚构分数 |
| 载入 | 所选 experience 的关联 atoms → 格式化 title/content → system prompt | 右列；不能误画成只把历史 query 送入 prompt |

完整 trace 在该机制中为 judging/extraction 提供材料；检索 key 是 task query。不要因为画的是 memory 就把全文轨迹改成向量检索输入。新论文必须重新确认这些事实，不继承这个例子的模块。

## 制作：精确层与案例层

**精确层。** 用演示工具的原生形状、文本和连接绘制拓扑。先摆节点和边界，再连边，最后加入短标签。数据、公式、关键术语和需要改动的文字保持可编辑。使用白底、蓝色重点、克制浅蓝面板，规格见 完整包内的 `references/visual-system.md`。

**案例层。** 只有图形能帮助解释时才生成素材。先固定对象、状态、边表和逐字标签，再套用 完整包内 `references/image-playbook.md` 的模板A/B/C。精确分支、公式或多文字内容适合直接原生制作；生成图可负责简单图标、短案例或概念物件。需要改文字时重建原生层，或用图像编辑工具修改并复核，不能声称改了 PNG 内的文字对象。

**空间与字号。** 参考第15页的上机制、下案例关系；下方案例区域约 `x=.65, y=4.82, w=12, h=2.28 in`。它是原稿几何示例，不是每张图都要套的尺寸。保持图像原比例，留出箭头和文字边缘；内容多或字号已选大时拆页。不要复制原稿中偏小标签作为新图的字号要求。

## 怎样嵌入与展开

- **PPTX：** 上层用原生对象；下层图片等比 contain 到目标区域，添加描述内容的 alt text 和备注。保留生成素材及实际 prompt。右上总览用固定几何，高亮使用独立原生对象。静态分步页可以复制当前页，只增加必要内容或移动高亮；最终页必须独立可读。
- **HTML slides：** 需要精确和可访问的文字时用 DOM 文本及 SVG 连接；生成素材使用普通图片，保留 alt、原比例和可读的展示尺寸。揭示状态与讲述步骤一致，打印/导出包含完整静态终态。
- **README：** 使用宽图和短说明展示实际成果；它是展示入口，不承担可编辑源文件的角色。链接到制作方法与可下载的完整包。

本例可按三次展开：先看到新 query；再加入两条历史 query 与所选候选；最后加入关联 atom 和送入 prompt 的连接。共同对象位置不动。若动画不可用，交付同样顺序的三页，而不是只有一个小字密集的全图。

## 检查什么

沿一条真实或明确标注的教学输入走完图，逐条读出“这个箭头传递什么”。检查分支可达、条件互斥或重叠的真实含义、共享边界、术语和来源身份；无数据不画结果数字。再在实际展示尺寸检查标签、箭头、裁切、颜色与静态终态。保留图源和可编辑精确层，区分“已有参考图”“本次新生成素材”和“尚未渲染的规格”。


---

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
