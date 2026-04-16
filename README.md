# OpenPaper — AI-Powered Academic Paper Writing with Claude Code

A curated collection of [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills) that turn Claude into a capable research collaborator: from drafting publication-ready ML papers to generating professional diagrams.

## Skills

| Skill | Description | Source |
|-------|-------------|--------|
| [`ml-paper-writing`](#ml-paper-writing) | Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) |
| [`pyzotero`](#pyzotero) | Programmatically manage Zotero libraries: retrieve, create, update items, export BibTeX | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) |
| [`drawio`](#drawio) | Generate and export draw.io diagrams as `.drawio`, PNG, SVG, or PDF | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) |
| [`drawio-paper`](#drawio-paper) | Generate publication-quality academic diagrams and statistical plots via PaperBanana pipeline | Original |
| [`hugging-face-paper-pages`](#hugging-face-paper-pages) | Look up and read Hugging Face paper pages, fetch structured metadata for AI research papers | [huggingface/skills](https://github.com/huggingface/skills/blob/main/skills/hugging-face-paper-pages/SKILL.md) |
| [`alphaxiv-paper-lookup`](#alphaxiv-paper-lookup) | Look up arXiv papers on AlphaXiv for structured AI-generated overviews | Original |
| [`hpq-xray-paper`](#hpq-xray-paper) | X-ray a paper: extract core argument, prior work lineage, advisor-style review, and personal cognitive delta cards | [ljg-skill-xray-paper](https://github.com/lijigang/ljg-skill-xray-paper) (modified) |
| [`paper-finder`](#paper-finder) | Find and organize ML/AI research papers into a reusable topic knowledge base with summaries and BibTeX | [bchao1/paper-finder](https://github.com/bchao1/paper-finder/tree/main) (adapted) |
| [`deepxiv-cli`](#deepxiv-cli) | Access open-access academic papers via CLI with hybrid search and section-level reads | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main) |
| [`deepxiv-baseline-table`](#deepxiv-baseline-table) | Build markdown baseline comparison tables from deepxiv search and targeted section reads | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main) |
| [`deepxiv-trending-digest`](#deepxiv-trending-digest) | Summarize trending papers into a concise markdown digest with deep-dive recommendations | [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main) |

---

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) (CLI)
- For `drawio` exports: [draw.io desktop app](https://github.com/jgraph/drawio-desktop/releases)
- For `ml-paper-writing`: LaTeX distribution ([TeX Live](https://tug.org/texlive/) recommended) and optional Python packages (`semanticscholar`, `arxiv`, `habanero`, `requests`)
- For `pyzotero`: `pyzotero` Python package (`uv add pyzotero`) and a [Zotero API key](https://www.zotero.org/settings/keys)
- For `drawio-paper`: Python with `matplotlib`, `numpy`, `pillow` and the PaperBananaBench dataset (see [setup](#setup-1))
- For `hugging-face-paper-pages` and `alphaxiv-paper-lookup`: no additional setup required
- For `hpq-xray-paper`: Python 3 (for helper scripts); optional `know/soul.md` and `know/memory.md` for personalized cognitive delta
- For `paper-finder`: no required setup; optional web access recommended for current paper discovery
- For `deepxiv-cli`, `deepxiv-baseline-table`, and `deepxiv-trending-digest`: install DeepXiv CLI (`pip install deepxiv-sdk`)

### Installation

Clone this repository into any project directory where you want to use the skills:

```bash
git clone https://github.com/your-username/openpaper.git
cd your-project
cp -r path/to/openpaper/.claude .
```

Or clone directly inside your research project:

```bash
cd my-research-project
git clone https://github.com/your-username/openpaper.git .claude-skills
cp -r .claude-skills/.claude .
```

The skills are automatically detected by Claude Code from the `.claude/skills/` directory.

---

## ml-paper-writing

> Write publication-ready ML/AI papers for top academic venues.

### What It Does

- **Drafts complete papers** from your research repository — methods, experiments, related work, and all
- **Enforces citation integrity**: never hallucinates references; always fetches BibTeX programmatically via DOI
- **Provides LaTeX templates** for all major venues (ICML 2026, ICLR 2026, NeurIPS 2025, ACL, AAAI 2026, COLM 2025, IEEE IEEEtran, ACM acmart)
- **Guides conference resubmissions**: page-limit adjustments, venue-specific requirements, blind-review compliance
- **Applies writing philosophy** from leading ML researchers (Neel Nanda, Sebastian Farquhar, Andrej Karpathy, Zachary Lipton, Jacob Steinhardt)

### Supported Venues

#### ML/AI Conferences

| Conference | Page Limit | Key Requirement |
|------------|------------|-----------------|
| NeurIPS 2025 | 9 pages | Mandatory checklist |
| ICML 2026 | 8 pages | Broader Impact Statement |
| ICLR 2026 | 9 pages | LLM disclosure required |
| ACL / EMNLP / NAACL | 8 pages | Limitations section mandatory |
| AAAI 2026 | 7 pages | Strict style file adherence |
| COLM 2025 | 9 pages | Language model focus |

#### IEEE & ACM Journals / Conferences

| Venue | Template | Covers |
|-------|----------|--------|
| IEEE Transactions (TPAMI, TNNLS, TIP) | `ieeetran/bare_jrnl.tex` | Journals, no fixed page limit |
| IEEE CS Conferences (WACV, ICASSP) | `ieeetran/bare_conf_compsoc.tex` | Typically 8 pages |
| ACM CHI, KDD, MM, SIGCOMM | `acmart/sample-sigconf.tex` | 8–12 pages + refs |
| ACM SIGGRAPH / TOG | `acmart/sample-acmtog.tex` | No fixed limit |

### Usage

```
/ml-paper-writing write a NeurIPS paper from this repo
/ml-paper-writing draft the related work section for ICLR
/ml-paper-writing convert this NeurIPS submission to ICML format
/ml-paper-writing verify and fix citations in main.tex
```

### Citation Safety

AI-generated citations have a ~40% error rate. This skill enforces a strict workflow:

1. Search via Claude Code's built-in web search or Semantic Scholar API
2. Verify existence in 2+ sources
3. Fetch BibTeX programmatically via DOI
4. Mark unverifiable references as `[CITATION NEEDED]` — never invent them

### Included Templates

```
.claude/skills/ml-paper-writing/templates/
├── neurips2025/      # NeurIPS 2025
├── icml2026/         # ICML 2026
├── iclr2026/         # ICLR 2026
├── acl/              # ACL / EMNLP / NAACL
├── aaai2026/         # AAAI 2026
├── colm2025/         # COLM 2025
├── ieeetran/         # IEEE Transactions & Conferences (IEEEtran v1.8b)
└── acmart/           # ACM Publications — CHI, SIGGRAPH, KDD, MM… (acmart v2.14)
```

---

## pyzotero

> Programmatically interact with your Zotero reference library.

### What It Does

- **Read and search** your Zotero library items, collections, and tags
- **Create and update** bibliographic references from templates
- **Export citations** as BibTeX, CSL-JSON, or formatted bibliographies
- **Upload attachments** and manage PDF files linked to items
- **Automate research workflows** — sync references, batch-tag, or build custom pipelines

### Setup

Get your credentials from [zotero.org/settings/keys](https://www.zotero.org/settings/keys) and store them as environment variables:

```bash
export ZOTERO_LIBRARY_ID=your_user_id
export ZOTERO_API_KEY=your_api_key
export ZOTERO_LIBRARY_TYPE=user   # or "group"
```

Install the Python client:

```bash
uv add pyzotero
```

### Usage

```
/pyzotero search my library for papers on transformers
/pyzotero export all items in the "NeurIPS 2025" collection as BibTeX
/pyzotero add a new journal article entry for this paper
/pyzotero upload this PDF as an attachment to item ABC123
```

---

## drawio

> Generate native draw.io diagrams and export to PNG, SVG, or PDF.

### What It Does

- Generates `.drawio` files in native mxGraphModel XML format
- Exports to PNG, SVG, or PDF with embedded XML (files remain editable in draw.io)
- Works directly from natural language descriptions

### Usage

```
/drawio create a system architecture diagram
/drawio png flowchart for the training pipeline
/drawio svg ER diagram for the database schema
/drawio pdf overview of the model architecture
```

### Output Formats

| Format | Editable in draw.io | Notes |
|--------|---------------------|-------|
| `.drawio` | Yes | Native XML, open directly in draw.io |
| `.drawio.png` | Yes (embedded XML) | Viewable everywhere |
| `.drawio.svg` | Yes (embedded XML) | Scalable vector |
| `.drawio.pdf` | Yes (embedded XML) | Printable |

### Requirements

The draw.io desktop app must be installed for export (PNG/SVG/PDF). The skill auto-detects it at:

- **macOS**: `/Applications/draw.io.app/Contents/MacOS/draw.io`
- **Linux**: `drawio` (via snap/apt/flatpak)
- **Windows**: `C:\Program Files\draw.io\draw.io.exe`

---

## drawio-paper

> Generate publication-quality academic paper diagrams and statistical plots using a PaperBanana-inspired multi-agent pipeline.

### What It Does

- **Diagram mode**: Transforms methodology sections and figure captions into polished `.drawio` diagrams through retrieval, planning, styling, visualization, and critique stages
- **Plot mode**: Transforms raw data (tabular/JSON) into publication-ready statistical plots via Python/matplotlib, following the same multi-stage pipeline
- Uses reference-driven design from the PaperBananaBench dataset for aesthetically refined outputs

### Setup

Before first use, download the PaperBananaBench reference dataset:

```bash
# Download from Hugging Face
curl -L -o .claude/skills/drawio-paper/PaperBananaBench.zip \
  https://huggingface.co/datasets/dwzhu/PaperBananaBench/resolve/main/PaperBananaBench.zip

# Extract
python .claude/skills/drawio-paper/scripts/extract_bench.py
```

For plots, ensure Python packages are available:

```bash
pip install matplotlib numpy pillow
```

### Usage

```
/drawio-paper create a framework overview diagram from the methodology section
/drawio-paper generate a bar chart comparing model performance from results.csv
/drawio-paper pipeline diagram for the training workflow described in Section 3
```

---

## hugging-face-paper-pages

> Look up and read Hugging Face paper pages, and fetch structured metadata for AI research papers.

### What It Does

- **Fetches paper content as markdown** from Hugging Face paper pages (`hf.co/papers/{ID}.md`)
- **Retrieves structured metadata** via the Papers API: authors, linked models/datasets/spaces, GitHub repo, project page
- **Searches papers** with hybrid semantic and full-text search
- **Browses Daily Papers** feed with date/week/month filtering
- Supports input from Hugging Face URLs, arXiv URLs, or raw arXiv IDs

### Supported Inputs

| Input | Paper ID |
|-------|----------|
| `https://huggingface.co/papers/2602.08025` | `2602.08025` |
| `https://huggingface.co/papers/2602.08025.md` | `2602.08025` |
| `https://arxiv.org/abs/2602.08025` | `2602.08025` |
| `https://arxiv.org/pdf/2602.08025` | `2602.08025` |
| `2602.08025v1` | `2602.08025v1` |
| `2602.08025` | `2602.08025` |

### API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /papers/{ID}.md` | Paper content as markdown |
| `GET /api/papers/{ID}` | Structured metadata (authors, summary, links) |
| `GET /api/papers/search?q=...` | Hybrid semantic + full-text search |
| `GET /api/daily_papers` | Daily Papers feed with filtering |
| `GET /api/models?filter=arxiv:{ID}` | Models linked to a paper |
| `GET /api/datasets?filter=arxiv:{ID}` | Datasets linked to a paper |
| `GET /api/spaces?filter=arxiv:{ID}` | Spaces linked to a paper |

### Usage

```
/hugging-face-paper-pages summarize https://huggingface.co/papers/2602.08025
/hugging-face-paper-pages explain paper 2602.08025
/hugging-face-paper-pages find models linked to this paper
```

### Notes

- No authentication required for public paper pages
- Write endpoints (claim authorship, index paper, update links) require `Authorization: Bearer $HF_TOKEN`
- Prefer the `.md` endpoint for reliable machine-readable output

---

## alphaxiv-paper-lookup

> Look up arXiv papers on AlphaXiv for structured AI-generated overviews.

### What It Does

- **Fetches structured AI-generated overviews** of arXiv papers from `alphaxiv.org/overview/{ID}.md`
- **Falls back to full paper text** via `alphaxiv.org/abs/{ID}.md` when more detail is needed
- Faster and more reliable than reading raw PDFs
- No authentication required

### Supported Inputs

| Input | Paper ID |
|-------|----------|
| `https://arxiv.org/abs/2401.12345` | `2401.12345` |
| `https://arxiv.org/pdf/2401.12345` | `2401.12345` |
| `https://alphaxiv.org/overview/2401.12345` | `2401.12345` |
| `2401.12345v2` | `2401.12345v2` |
| `2401.12345` | `2401.12345` |

### Usage

```
/alphaxiv-paper-lookup summarize 2401.12345
/alphaxiv-paper-lookup explain https://arxiv.org/abs/2401.12345
```

---

## hpq-xray-paper

> X-ray a research paper: extract what it says, trace its intellectual lineage, give an advisor-level review, and surface personal cognitive deltas.

### What It Does

This skill performs four tasks — and only four — on any academic paper:

1. **What the paper says** — Problem → Perspective → Result, written in plain language with a napkin-sketch ASCII diagram of the core mechanism
2. **Standing on whose shoulders** — Identifies 5–7 key prior works that form the paper's intellectual lineage, with role annotations (Foundation, Inspiration, Gap, Baseline, Extension, Related Problem) and an ASCII genealogy chart
3. **Advisor review** — A candid evaluation as a senior PhD advisor: topic quality, method maturity, experimental rigor, writing quality, and a verdict (strong accept → strong reject)
4. **What it means for me** — Cognitive delta cards (ASCII art) that visualize how the paper's insights could change a specific thinking habit, decision pattern, or blind spot

### Origin

Forked from [lijigang/ljg-skill-xray-paper](https://github.com/lijigang/ljg-skill-xray-paper) with the following modifications:

- **Added prior work analysis** (Task 2): traces the paper's intellectual lineage with role-classified references and an ASCII genealogy chart
- **Added advisor review** (Task 3): simulates a senior PhD advisor giving a candid assessment with a formal verdict
- **Changed note template to Markdown**: output is a structured `.md` file with YAML frontmatter instead of plain text
- **Added helper scripts**: `search_paper.py` for Semantic Scholar lookups and `append_to_memory.py` for automated paper memory logging

### How It Works

1. Accepts an arXiv ID, URL, or PDF path and converts arXiv links to `/html/` format for full-text fetching
2. Loads a personal cognitive baseline from `know/soul.md` and `know/memory.md` (if present)
3. Runs through the four analysis tasks with strict writing quality checks (no jargon, no filler, oral-style clarity)
4. Generates a timestamped Markdown report in `notes/` and appends a summary entry to `know/paper_memory.md`

### Usage

```
/hpq-xray-paper 2601.01290
/hpq-xray-paper https://arxiv.org/abs/2601.01290
/hpq-xray-paper path/to/paper.pdf
```

### Key Constraints

- **Zero-jargon rule**: every technical concept must be grounded in a familiar scenario before the term is introduced
- **ASCII art only**: all diagrams use pure ASCII characters — no Unicode box-drawing symbols
- **Honesty**: if there is no cognitive delta, the output says "delta ≈ 0" rather than fabricating insights
- **Writing quality gates (L2)**: oral test, short-word preference, one-idea-per-sentence, no academic filler

---

## paper-finder

> Find, rank, and organize related papers into a persistent topic workspace.

### What It Does

- **Searches broadly** across arXiv, Semantic Scholar, Google Scholar-style web results, and major venues
- **Covers multiple angles** for a topic: direct keywords, cross-domain synonyms, enabling mechanisms, and motivating applications
- **Builds a reusable paper workspace** with a memory bank, mind graph, per-paper summaries, discussion notes, and combined BibTeX
- **Keeps discovery current** by requiring web search rather than relying only on model memory

### Workspace Layout

```text
<topic-name>/
├── memory-bank.md
├── mind-graph.md
├── references.bib
├── summaries/
├── discussions/
└── pdfs/              # only when explicitly requested
```

### Usage

```
/paper-finder find papers on mixed-resolution diffusion transformers
/paper-finder build a literature review workspace for efficient video generation
/paper-finder compare recent CVPR and ICCV papers on 3D Gaussian splatting
```

### Origin

Adapted from [bchao1/paper-finder](https://github.com/bchao1/paper-finder/tree/main) and included here as part of the broader OpenPaper skill collection.

---

## deepxiv-cli

> Access open-access academic papers through the DeepXiv CLI with hybrid search and token-efficient reading.

### What It Does

- **Searches papers** with hybrid retrieval (BM25 + vector semantics)
- **Reads at multiple depths**: brief summary, paper structure (`--head`), section-level, or full text
- **Supports multiple sources**: arXiv and PMC today, with bioRxiv/medRxiv planned
- **Includes an analysis agent** via `deepxiv agent query` for higher-level synthesis

### Usage

```
/deepxiv-cli search papers about agent memory from this month
/deepxiv-cli read arXiv 2409.05591 with --brief
/deepxiv-cli show sections for 2409.05591 with --head
/deepxiv-cli summarize the Introduction section of 2409.05591
```

---

## deepxiv-baseline-table

> Build a markdown baseline table for a topic using DeepXiv search plus targeted experiment-section extraction.

### What It Does

- **Finds candidate papers** by topic and date range with `deepxiv search`
- **Screens efficiently** using `deepxiv paper <id> --brief`
- **Extracts benchmark evidence** from `--head` and experiment/result sections only
- **Outputs comparison-ready tables** including open-source status, datasets, metrics, and score notes

### Typical Output Columns

| Title | arXiv | URL | Open Source | Code URL | Datasets / Benchmarks | Metrics / Scores | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Usage

```
/deepxiv-baseline-table build a baseline table for agentic memory papers in the last 30 days
/deepxiv-baseline-table compare datasets and benchmark scores for recent multimodal reasoning papers
```

---

## deepxiv-trending-digest

> Turn recent DeepXiv trending papers into a concise markdown digest with recommended deep dives.

### What It Does

- **Collects trending papers** from `deepxiv trending` over a configurable time window
- **Builds quick summaries** from `--brief` for all shortlisted papers
- **Deepens selectively** with `--head` and 1-2 high-value sections for top candidates
- **Produces a digest report** with executive themes, per-paper takeaways, and deep-dive recommendations

### Usage

```
/deepxiv-trending-digest make a 7-day trending digest and highlight top 3 papers worth deeper reading
/deepxiv-trending-digest summarize this week's hottest papers and suggest next sections to read
```

---

## Repository Structure

```
.claude/
└── skills/
    ├── ml-paper-writing/
    │   ├── SKILL.md                  # Skill definition
    │   ├── templates/                # LaTeX templates per venue
    │   │   ├── neurips2025/
    │   │   ├── icml2026/
    │   │   ├── iclr2026/
    │   │   ├── acl/
    │   │   ├── aaai2026/
    │   │   ├── colm2025/
    │   │   ├── ieeetran/             # IEEE (IEEEtran v1.8b)
    │   │   └── acmart/               # ACM (acmart v2.14)
    │   └── references/
    │       ├── writing-guide.md      # Gopen & Swan, Perez micro-tips
    │       ├── citation-workflow.md  # Citation API docs and Python code
    │       ├── checklists.md         # NeurIPS / ICML / ICLR / ACL checklists
    │       ├── reviewer-guidelines.md
    │       └── sources.md
    ├── pyzotero/
    │   ├── SKILL.md                  # Skill definition
    │   └── references/               # API docs (read, write, search, export…)
    ├── drawio/
    │   └── SKILL.md                  # Skill definition
    ├── drawio-paper/
    │   ├── SKILL.md                  # Skill definition
    │   ├── scripts/                  # Setup scripts (extract_bench.py)
    │   └── PaperBananaBench/         # Reference dataset (after setup)
    ├── hugging-face-paper-pages/
    │   └── SKILL.md                  # Skill definition
    ├── alphaxiv-paper-lookup/
    │   └── SKILL.md                  # Skill definition
    ├── paper-finder/
    │   └── SKILL.md                  # Skill definition
    ├── deepxiv-cli/
    │   └── SKILL.md                  # Skill definition
    ├── deepxiv-baseline-table/
    │   └── SKILL.md                  # Skill definition
    ├── deepxiv-trending-digest/
    │   └── SKILL.md                  # Skill definition
    └── hpq-xray-paper/
        ├── SKILL.md                  # Skill definition
        ├── references/
        │   └── template.md           # Markdown report template
        └── scripts/
            ├── append_to_memory.py   # Auto-append to paper_memory.md
            └── search_paper.py       # Semantic Scholar paper lookup
```

---

## Credits

- **ml-paper-writing** skill: [Orchestra Research / AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) — MIT License
- **pyzotero** skill: [K-Dense-AI / claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) — MIT License
- **drawio** skill: [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp)
- **drawio-paper** skill: PaperBanana-inspired pipeline, reference dataset from [dwzhu/PaperBananaBench](https://huggingface.co/datasets/dwzhu/PaperBananaBench)
- **hugging-face-paper-pages** skill: [huggingface/skills](https://github.com/huggingface/skills/blob/main/skills/hugging-face-paper-pages/SKILL.md)
- **alphaxiv-paper-lookup** skill: [AlphaXiv](https://alphaxiv.org)
- **paper-finder** skill: adapted from [bchao1/paper-finder](https://github.com/bchao1/paper-finder/tree/main)
- **hpq-xray-paper** skill: forked from [lijigang/ljg-skill-xray-paper](https://github.com/lijigang/ljg-skill-xray-paper), modified with prior work analysis, advisor review, and Markdown note format
- **deepxiv-cli** skill: adapted from [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main)
- **deepxiv-baseline-table** skill: adapted from [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main)
- **deepxiv-trending-digest** skill: adapted from [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main)
- Writing philosophy sourced from: Neel Nanda, Sebastian Farquhar, Gopen & Swan, Zachary Lipton, Jacob Steinhardt, Ethan Perez, Andrej Karpathy

---

## License

This repository is provided under the MIT License. Individual skills retain their upstream licenses — see each skill's `SKILL.md` for details.
