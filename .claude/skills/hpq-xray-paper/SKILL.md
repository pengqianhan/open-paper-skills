---
name: hpq-xray-paper
description: "Paper X-ray. Extracts what the paper says (problem-perspective-result) and what it means for hpq (cognitive delta cards in ASCII art). Use when user shares an arxiv link, paper URL, PDF, or asks to analyze a research paper. Usually called via hpq-xray router. Do NOT use for blog posts or non-academic articles (use hpq-xray-article instead)."
user_invocable: true
---

# HPQ-Xray-Paper: 论文解读

你要做四件事，仅四件：
1. **论文说了什么**：问题 → 视角 → 结果
2. **站在谁的肩膀上**：5-7 篇关键前序工作，标注角色
3. **博导审稿**：博导审稿，给出判决
4. **对我意味着什么**：认知卡片（ASCII art 直观展示启发）

其它一切都服务于这四件事。

## 约束

### L0: 通用约束

#### Markdown 语法

- 加粗用 `**bold**`（双星号）
- 标题层级从 `#` 开始，不跳级

#### ASCII Art

所有图表、拓扑、卡片，一律使用纯 ASCII 字符绘制。

允许字符集：`+ - | / \ > < v ^ * = ~ . : # [ ] ( ) _ , ; ! ' "`  和空格。

禁止一切 Unicode 绘图符号，包括但不限于：
`─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬ ▼ ▲ ► ◄ → ← ↑ ↓ ● ○ ■ □ ◆ ◇`

例外：输出目标为 HTML 文件（浏览器渲染）的 skill 不受此限。

#### Markdown 文件规范

- 时间获取：**必须执行** `date "+%Y-%m-%d %a %H:%M"` 获取当前真实时间，不要凭印象填写。`date` 字段和文件名中的时间戳都来自这条命令的输出
- 文件名格式：`{YYYYMMDDTHHMMSS}-paper-{简短标题}.md`（例：`20260227T150000-paper-memobrain-executive-memory.md`），时间戳取自上述 `date` 命令
- 输出目录：repo 根目录下的 `notes/`（即与 `.claude/` 同级的 `notes/` 目录）
- 视觉类输出（HTML/PNG）例外：`~/Downloads/` 或 `/tmp/`

#### Markdown 文件头

```yaml
---
title: "{prose-as-title: what this paper argues or contributes}"
date: "{YYYY-MM-DD Day HH:MM}"
description: "{academic one-sentence summary, precise, jargon-permitted}"
publish_date: "{YYYY-MM-DD}"
keywords: "{keywords}"
topics: ["[[existing-topic-map]]"]
tags: "{tags}"
authors: "{authors}"
affiliations: "{affiliations}"
source: "{source URL — arxiv 论文用 /html/ 格式，如 https://arxiv.org/html/2601.08079}"
review: "{decision: strong accept / weak accept / borderline / weak reject / strong reject, one-sentence reason}"
---
```

注意：
- `title` 和文档 H1 必须是同一句 prose-as-title，写这篇论文真正提出/证明了什么；不要直接抄论文原题
- 过句子测试：`This paper argues that [title].` 读起来必须自然、具体、像一个可被链接的论断
- `source` 对 arxiv 论文统一存 `/html/` URL（可直接 WebFetch，无需二次转换）；非 arxiv 论文存原始 URL
- `description` 用学术语言写，可以用术语，目标读者是懂行的人。区别于 body 里的 `**一句话**`（大白话，电梯测试，目标读者是外行）
- `description` 是 schema-required 字段，必须是单句，且补充标题之外的方法、范围或含义信息
- `topics` 是 schema-required 字段，必须是非空 wiki-link 数组；优先填已有 topic map，如暂时没有更具体主题则用 `["[[index]]"]` 作为最小合规回退
- `review` 用学术英语写，不要用中文。

### L1: 认知类约束

#### 认知基线加载

执行分析前，读取以下文件建立认知基线：

1. repo 根目录下的 `know/soul.md` — 世界观、思维范式、核心信念
2. repo 根目录下的 `know/memory.md` — 长期记忆、知识连接

#### 诚实原则

- delta ≈ 0 是正常结果，不硬凑
- 没有碰撞就不造卡片
- 搜不到的信息标注「信息不足」，不编造
- 压不成一句话 = 还没想透，继续想，别糊弄

#### 认知碰撞卡片

卡片 = ASCII art，视觉优先。

好卡片的标准：遮住文字只看线条，仍能感受到结构关系（分叉、汇聚、层级、对比、拉扯）。

反面教材——文字列表伪装成卡片：

```
+------------------+
| 论文说: X        |
| 我原来想: Y      |
| 现在变成: Z      |
+------------------+
```

这不是卡片，是带框的文字。结构关系要用空间布局表达，不是用标签声明。

每张卡片锚定一个具体场景：一个思考方式、一个决策场景、或一个认知盲区的改变。卡片下方附一句金句级启发——能脱离上下文单独成立。

### L2: 写作红线

每条必须过，是写作质量的底线：

1. **口语检验** — 你会这样跟朋友介绍这篇论文吗？不会就改。学术腔是默认敌人
2. **短词优先** — 能用两个字说的不用四个字。「本文提出了一种新的框架」→「他们做了个东西」
3. **一句一事** — 每句只推进一步
4. **具体** — 名词看得见，动词有力气。形容词能砍就砍
5. **开头给理由** — 问题部分的第一句让人想知道答案
6. **不填充** — 删学术套话（「近年来随着...的发展」「值得注意的是」）。每句干货
7. **信任读者** — 说一遍够了。不重复结论


## 执行步骤

### 步骤 1：接收论文并预处理输入

| 用户输入 | 转换规则 |
|---------|---------|
| `2601.01290` 或 `arxiv:2601.01290` | → `https://arxiv.org/html/2601.01290` |
| `https://arxiv.org/abs/...` 或 `.../pdf/...` | → 替换为 `/html/` |
| `https://arxiv.org/html/...` | 直接使用 |
| 其他 URL 或 PDF 路径 | 按原有逻辑处理 |

arxiv 论文一律转为 `/html/` 格式，HTML 版本可直接 WebFetch 抓取全文。

提取论文原题、作者和来源信息；然后基于核心贡献**重新写一句 prose-as-title**，同时填入 YAML `title` 和文档 H1。不要把论文原题直接塞进 `title`。

### 步骤 2：加载认知参照系

执行认知基线加载（见约束 L1）。

### 步骤 3：论文说了什么

像跟聪明朋友在饭桌上说"这篇论文干了个什么事"——三句话，人话，不要论文八股：
- **问题**：作者要解决什么？
- **视角**：用什么方法/切入角度？
- **结果**：得到了什么？用"实验证明"和"作者推测"自然区分。推测性结论如果有趣，在步骤 5 做成"开放问题"碰撞卡片

**零术语规则**：每个技术概念必须立刻落在读者见过的事情上。不给例子就不准用那个词。

坏："共现概率只取决于隐含空间中的距离（平移对称性）"
好："一月和二月经常出现在同一段话里，一月和七月就很少——距离越近越常一起出现"

道理要长在场景里，不是贴在标签上。

**承重概念场景化**：每篇论文有 2-3 个"承重概念"——去掉它们论文的论证就塌了。这些概念不能用括号注释一笔带过（"gamma：条件熵衰减指数"）。括号注释是给已经懂的人的提示，不是解释。对每个承重概念：

1. 先找一个读者亲身经历过的场景（群聊记录、排队、找路...）
2. 在场景中逐步展开——至少 3 级渐进，让读者在熟悉的事情上"感受到"这个概念在变化
3. 最后才贴技术名字。此时名字是标签，不是定义

判断标准：去掉技术名字，读者仍然知道你在说什么 = 落地成功。只剩括号注释 = 失败。

概念之间的关系同样场景化。不是"alpha 是 gamma 和 beta 的比值"，而是"远处信息的性价比：值多少分 / 有多难够到 = scaling 有多陡"。

普通术语一句话类比即可，不需要场景展开。区分承重与非承重是关键判断。

最后压成一句大白话——像你在电梯里跟完全不懂这个领域的朋友说"这篇论文就是说……"。不准用术语，不准超过一句话。压不成 = 还没想透，继续想。

配一张餐巾纸图（ASCII），画出核心机制。

### 步骤 4：博导审稿

换身份：这个方向上带了二十年研究生的博导。学生拿着论文来找你，你判断这东西值不值得认真对待。

用白话说，像在办公室跟学生聊：

- **选题眼光**：问题值不值得做？真缺口还是人造缺口？
- **方法成熟度**：巧劲还是蛮力？有没有更自然的做法被忽略？
- **实验诚意**：baseline 公不公道？消融到位没？数字经不经得起追问？
- **写作功力**：最该说清楚的地方有没有偷懒？
- **判决**：strong accept / weak accept / borderline / weak reject / strong reject，一句话理由

好的说好，差的说差在哪儿。不装客气。

### 步骤 5：站在谁的肩膀上

从论文的 Introduction 和 Related Work 中，识别 **5-7 篇关键前序工作**。这些不是随便引用的参考文献，而是这篇论文的"智力血统"——去掉任何一篇，这篇论文的创新就无法成立。

#### Prior Work Identification Criteria

筛选标准（三者至少满足其一）：

1. **Direct Intellectual Lineage** - Papers that directly contributed to the core innovation
2. **Specific Contributions** - Papers with identifiable techniques, insights, or methods that were adopted
3. **Explicit Influence** - Papers cited as primary influences in the introduction or related work

#### Role Classifications

每篇前序工作标注一个角色，说明它在这篇论文的创新链条中扮演什么位置：

| Role | Description | Icon |
|------|-------------|------|
| **Foundation** | Introduced core problem formulation, dataset, or theoretical framework | 🏗️ |
| **Inspiration** | Specific idea/approach that sparked the key innovation | 💡 |
| **Gap Identification** | Limitations that motivated the research direction | 🔍 |
| **Baseline** | Primary system/method being improved upon | 📊 |
| **Extension** | Method directly extended or modified | 🔧 |
| **Related Problem** | Similar problem with transferable solution approach | 🔗 |

#### Exclusion Criteria

以下类型不选：
- Generic infrastructure/tools (PyTorch, CUDA, etc.)
- Complementary optimizations orthogonal to main contribution
- Standard baselines without deeper connection
- Well-known foundational works cited universally (e.g., Transformer, ResNet — unless本文直接修改了它们)

#### 链接规则

对每篇前序工作，按以下优先级确定链接：

1. **有笔记**：在 `notes/` 目录下搜索是否已有对应笔记（按论文标题关键词匹配文件名）。有则链接指向笔记文件的相对路径，如 `[MemoBrain](20260227T150000-paper-memobrain-executive-memory__read.md)`
2. **有 arxiv ID**：链接指向 arxiv，如 `[MemoBrain](https://arxiv.org/abs/2601.08079)`
3. **arxiv ID 未知**：运行 Semantic Scholar 脚本搜索论文标题获取真实 URL：
   ```bash
   python .claude/skills/hpq-xray-paper/scripts/search_paper.py "论文标题"
   ```
   脚本返回论文的 Semantic Scholar URL 和 DOI/arxiv 链接（如有）。用返回的最佳 URL 作为链接。
4. **搜索无果**：标注 `[Title](信息不足)`，不要编造占位符 URL（如 `arxiv.org/abs/xxxx`）

#### 输出格式

对每篇前序工作，写一句话说明它贡献了什么、本文如何用到。不要只列标题，要说清楚"从它那里拿走了什么"。标题用 `[Title](link)` 格式，按链接规则确定链接目标。

最后画一张 ASCII 谱系图，展示这些前序工作如何汇聚到本文的创新点。谱系图应该让读者一眼看到：哪些想法从哪里来，在哪里交汇。

### 步骤 6：对我意味着什么

读完这篇论文，我带走什么？

先用一句话回答：这篇论文的思想，可能改变我的什么？指向一个具体的思考习惯、决策模式、或认知盲区。不是"让我更了解 X"——那是信息增量，不是改变。如果找不到改变，诚实写"delta ≈ 0"。

soul.md + memory.md 提供"我是谁"的背景，但启发不限于已记录的条目。任何能提升我的决策质量的洞见都值得一张卡片：
- 一个可以直接用的思维工具（之前没有的）
- 一个改变了某个判断的新证据
- 一个没想过的角度或盲区
- 一个对已有认知的补充或修正

**三视角试探**——用以下三个方向寻找碰撞点，命中展开，没命中跳过，全没命中说"delta ≈ 0"：

- **迁移**：论文的某个机制/视角能移植升级我体系里的某个零件吗？
- **混搭**：论文的某个组件和我已有的东西组合能产生新东西吗？
- **反转**：论文的做法和我的默认假设相反吗？照出了什么盲区？

对每个有启发的点，生成一张认知卡片（ASCII art）。卡片质量标准见约束 L1。

卡片要直观展示：这个洞见如何改变我的某个思考方式、决策习惯、或打开一个盲区。看一眼就能 get 到启发在哪里。

**本 skill 的好卡片示例**——分叉型：
```
  Soul: "做了才懂"
        |
        |  但如果结构藏得太深...
        v
  +------------------+
  | 反馈能暴露结构?   |
  +---+----------+---+
      |          |
     YES         NO
      |          |
   生成优先    降秩优先
  (原路径)   (先看再做)
      |          |
      |     CTA: 0% vs 94%
      v          v
   Soul 成立   Soul 需加边界
```

阈值型（不是线性的，有个转折点）：
```
  我以为: 投入越多，产出越多（线性）

  投入 ----+----+----+----+----+---->
           |    |    |    |    |
  产出     .    .    .    .    .   线性预期
           .    .    .   /
  实际     .    .    . _/         <-- 阈值
           .    .    ./
           .____.___.'............   无效区
           |
       "原来这段全是白费的"
           |
           v
  决策改变: 不追问"做了多少"
            要追问"过没过线"
```

碰撞有多种形状——分叉、张力、阈值、缺口、翻转。选跟碰撞本身匹配的空间结构，不要把所有碰撞都压成同一种图。

论文的推测性观点如果有趣，也做成碰撞卡片——标注"开放问题"，只有方向没有结论。写一个尖锐的问题，不是温和的 checkbox。值得追就追得下去，不值得追一眼就知道。

### 步骤 7：过红线

逐条扫 L2 写作红线。额外检查：

- **破公式** — 否定式排比全文不超过两处，三段式改两项或四项
- **变节奏** — 长短句交替，不要每句都一样长
- **杀金句** — 听起来像可引用的名言，重写。装腔是敌人
- **查跳跃** — 逻辑每步可追，没有"因此显然"式跳跃

列修改清单确认后进入下一步。

### 步骤 8：生成 Markdown 报告

1. **执行 `date "+%Y-%m-%d %a %H:%M"` 获取当前真实时间**（见约束 L0），用于 YAML 的 `date` 字段和文件名时间戳。不要编造或复用时间
2. 文件名：`{YYYYMMDDTHHMMSS}-paper-{简短标题}.md`（例：`20260227T150000-paper-memobrain-executive-memory.md`）
3. 读取 `references/template.md` 获取报告结构，按模板填充
4. 确认 YAML `title` 与文档 H1 完全一致，且两者都使用 prose-as-title 句子
5. 写入 repo 根目录下的 `notes/{文件名}`

### 步骤 9：追加记录到 paper_memory.md

笔记写入 `notes/` 后，运行脚本自动从笔记 YAML frontmatter 提取字段并追加到 `know/paper_memory.md`。

**执行命令：**

```bash
python .claude/skills/hpq-xray-paper/scripts/append_to_memory.py notes/{刚写入的笔记文件名}
```

**脚本做了什么：**
1. 解析笔记文件的 YAML frontmatter（title, date, description, publish_date, keywords, topics, authors, review, source）
2. 去掉 title 的 `paper-` 前缀作为显示标题
3. 生成标准格式条目并追加到 `know/paper_memory.md` 末尾
4. 若 `paper_memory.md` 不存在则自动创建并写入文件头

**规则：**
- 所有字段值直接从笔记 YAML 原样复制，不要改写或重新措辞
- 条目标题链接指向笔记文件（`../notes/` 相对路径）
- 如果环境没有 Python，按脚本同等逻辑手动读取 YAML 并追加即可

## 输出质量标准

- **只有四个部分**：论文说了什么 + 博导审稿 + 站在谁的肩膀上 + 对我意味着什么。不加别的
- **问题勾人**：让不懂的人也想知道答案
- **外行能跟**：不懂这个领域的聪明人读完能复述核心思路
- **博导像博导**：有判断力有分寸，最后一句判决干脆
- **过了红线**：L2 每条都检查过，没有学术腔残留
