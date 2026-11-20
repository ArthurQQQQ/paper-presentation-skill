# 保留源与中间页索引

## 哪个版本

唯一模板源是 `../assets/reference.pptx`，来自Arthur确认的最终交付，原文件名为`ReasoningBank-Agent-Memory-Presentation.pptx`。

源文件最终修改时间为 2026-11-13，31,980,311 bytes。43 页（40 正片 + 3 备份含分隔页）。`../assets/reference.pdf` 是该版已有的配套渲染；`../assets/preview.png` 是首张实际页面的已有渲染。

原制作记录的最终修订为“机制优先、SWE-bench原图与结果讲点”。本skill保留必要视觉与完整源稿；运行只依赖包内相对路径，不依赖作者机器上的历史目录。

不要误用项目 `PROJECT.json` 中 32 页稿、November 11 的 50+7 HTML，或其旧 45+7 PDF 作为最终模板。

## 看哪些实际页面

以下路径均相对 skill 根目录。前三页是最终修改后检查的 PNG；其余沿用先前全稿检查中后来未改的页面。它们是实际模板输出，不是新 skill 处理另一篇论文的验证结果。

| 最终页 | PNG | 内容与可复用模式 |
|---:|---|---|
| 1 | `assets/pages/01.png` | 居中学校标识、蓝带大标题、下方署名 |
| 9 | `assets/pages/09.png` | 左上校标、蓝色标题、大幅论文总图、底部大字讲点 |
| 13 | `assets/examples/13-consolidation.png` | 先讲成功/失败路径与追加机制，再展示同一首购经验怎样进入 bank；右上固定闭环定位 |
| 14 | `assets/examples/14-bank-scope.png` | 先说明共享范围，再用同一任务例子对照 Shopping 与 Admin 的边界 |
| 15 | `assets/examples/15-retrieval.png` | 编码→排序→载入的普遍机制在上；具体 query、候选和 atom 在下 |
| 22 | `assets/examples/22-benchmark.png` | 大幅原论文图解释 issue→patch→tests；主体保留原证据，右下小视频入口 |
| 24 | `assets/examples/24-main-results.png` | 短结论标题；完整比较表、指标方向和必要限定，属于证据密度例外 |
| 28 | `assets/examples/28-failure-result.png` | 一项失败学习实验，原图+具体差异+只覆盖该比较的结论 |
| 30 | `assets/examples/30-retrieval-result.png` | “更多不总更好”的曲线，区分取用条数与库容量 |
| 38 | `assets/examples/38-research-map.png` | 操作如何连接表示、持续学习和环境适应；图中方向是研究关系而非实测结果 |
| 40 | `assets/examples/40-takeaways.png` | 少量配图观点收束论文与讲者研究方向 |

## 来源、保留与验证覆盖

2026-11-17扩展：`assets/pages/01.png`–`43.png`保留所有页面的已有渲染，`references/page-by-page.md`逐页说明优点、改进和可迁移方法。8、9、10、12使用`qa-mechanism`，11使用最后的`judge-slide-11.png`，13–15和22使用`qa-presentation`，其他使用后续未改的`qa-titles`。最终PPTX的逐页原生文字与备注另在本次任务内容检查记录中核对。没有重新渲染。

`assets/image-references/` 保存原稿使用过的教学和概念插图，`diagram-original-prompt.md` 保存当时的检索图 prompt。这些是制作档案。新稿以 [原图选用](image-playbook.md) 为准。

- 最终 PPTX 与 PDF 原样保留。PPTX 内含讲者备注、原图和内嵌媒体；这些内容用于理解与版式参照，不自动成为下一报告的事实。
- 原作者制作路径 `build-deck.cjs`、`mechanism-revision.cjs` 的几何与色彩用来提取视觉规格。未把带有旧绝对依赖的构建脚本当作可移植生成器。
- 所附 PNG 来自该次制作的 `qa-presentation` 和 `qa-titles`，没有在封装 skill 时重新渲染。
- 原制作记录核对了 43 页和三个内嵌媒体，PowerPoint 放映点播仍未复测。新报告的功能需要按其实际输出重新验证。
- skill 的来源与参考完整性检查不等于其已在新论文上完成端到端视觉复现。实际应用后再按输出进行检查。
