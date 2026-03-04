# OpenPaper — AI-Powered Academic Paper Writing with Claude Code

A curated collection of [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills) that turn Claude into a capable research collaborator: from drafting publication-ready ML papers to generating professional diagrams.

## Skills

| Skill | Description | Source |
|-------|-------------|--------|
| [`ml-paper-writing`](#ml-paper-writing) | Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) |
| [`drawio`](#drawio) | Generate and export draw.io diagrams as `.drawio`, PNG, SVG, or PDF | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) |

---

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) (CLI)
- For `drawio` exports: [draw.io desktop app](https://github.com/jgraph/drawio-desktop/releases)
- For `ml-paper-writing`: LaTeX distribution ([TeX Live](https://tug.org/texlive/) recommended) and optional Python packages (`semanticscholar`, `arxiv`, `habanero`, `requests`)

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
- **Provides LaTeX templates** for all major venues (ICML 2026, ICLR 2026, NeurIPS 2025, ACL, AAAI 2026, COLM 2025)
- **Guides conference resubmissions**: page-limit adjustments, venue-specific requirements, blind-review compliance
- **Applies writing philosophy** from leading ML researchers (Neel Nanda, Sebastian Farquhar, Andrej Karpathy, Zachary Lipton, Jacob Steinhardt)

### Supported Venues

| Conference | Page Limit | Key Requirement |
|------------|------------|-----------------|
| NeurIPS 2025 | 9 pages | Mandatory checklist |
| ICML 2026 | 8 pages | Broader Impact Statement |
| ICLR 2026 | 9 pages | LLM disclosure required |
| ACL | 8 pages | Limitations section mandatory |
| AAAI 2026 | 7 pages | Strict style file adherence |
| COLM 2025 | 9 pages | Language model focus |

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
├── acl/              # ACL / EMNLP
├── aaai2026/         # AAAI 2026
└── colm2025/         # COLM 2025
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
    │   │   └── colm2025/
    │   └── references/
    │       ├── writing-guide.md      # Gopen & Swan, Perez micro-tips
    │       ├── citation-workflow.md  # Citation API docs and Python code
    │       ├── checklists.md         # NeurIPS / ICML / ICLR / ACL checklists
    │       ├── reviewer-guidelines.md
    │       └── sources.md
    └── drawio/
        └── SKILL.md                  # Skill definition
```

---

## Credits

- **ml-paper-writing** skill: [Orchestra Research / AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) — MIT License
- **drawio** skill: [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp)
- Writing philosophy sourced from: Neel Nanda, Sebastian Farquhar, Gopen & Swan, Zachary Lipton, Jacob Steinhardt, Ethan Perez, Andrej Karpathy

---

## License

This repository is provided under the MIT License. Individual skills retain their upstream licenses — see each skill's `SKILL.md` for details.
