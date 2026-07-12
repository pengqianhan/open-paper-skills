# OpenPaper Skills

An academic-research skill library for AI coding agents such as Codex and Claude Code.

This repository deliberately separates two kinds of skills:

- [`skills/`](skills/) contains original OpenPaper skills. It is the publishable, installable catalog.
- [`collected-skills/`](collected-skills/) contains third-party skills collected for reference and evaluation. It is not part of the default installable catalog.

## Original OpenPaper Skills

The directories in [`skills/`](skills/) follow the Agent Skills convention of `skills/<skill-name>/SKILL.md`, so GitHub CLI can discover and install them directly.

| Skill | Description |
| --- | --- |
| [`codex-paper-figure-skill`](skills/codex-paper-figure-skill/) | Create editable, journal-style academic figures and diagrams from paper text or figure descriptions. |
| [`discover-academic-skills`](skills/discover-academic-skills/) | Find and evaluate research-oriented agent skills with academic-relevance and quality gates. |
| [`drawio-paper`](skills/drawio-paper/) | Generate publication-quality academic diagrams and statistical plots. |
| [`explain-anything-html`](skills/explain-anything-html/) | Produce rich HTML explanations of papers, articles, documentation, and complex concepts. |
| [`karpathy-coding-rules`](skills/karpathy-coding-rules/) | Apply a focused set of coding rules and working conventions. |
| [`okf-repo-organizer`](skills/okf-repo-organizer/) | Organize repositories and knowledge corpora into Open Knowledge Format bundles. |
| [`paper-wiki-manager`](skills/paper-wiki-manager/) | Maintain a structured paper wiki, including paper notes, concepts, topics, and visualizations. |
| [`research-bible`](skills/research-bible/) | Turn ML/AI research principles into research plans, experiment loops, logs, and debugging routines. |
| [`task-file-builder`](skills/task-file-builder/) | Draft context-rich `task.md` briefs for fresh agent sessions. |
| [`uv-env`](skills/uv-env/) | Create and manage Python environments and dependencies with `uv`. |

### Install original skills with GitHub CLI

GitHub CLI `v2.90.0` or later can discover the repository's `skills/*/SKILL.md` directories.

```bash
# Preview one skill before installation
gh skill preview pengqianhan/openpaper research-bible

# Install one skill for Codex at user scope
gh skill install pengqianhan/openpaper research-bible --agent codex --scope user

# Install every original OpenPaper skill for Codex
gh skill install pengqianhan/openpaper --all --agent codex --scope user
```

At project scope, Codex uses the shared `.agents/skills/` directory. To validate the publishable catalog before a release, run:

```bash
gh skill publish --dry-run
```

See GitHub's [agent-skills announcement](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/) and the [Agent Skills specification](https://agentskills.io/specification).

## Collected Skills

[`collected-skills/`](collected-skills/) is a research and provenance archive. These third-party skills are intentionally kept outside `skills/`, so `gh skill install pengqianhan/openpaper --all` does not install them.

| Skill | Description |
| --- | --- |
| [`alphaxiv-paper-lookup`](collected-skills/alphaxiv-paper-lookup/) | Look up arXiv papers through AlphaXiv's structured AI-generated overviews. |
| [`arxiv2md`](collected-skills/arxiv2md/) | Convert arXiv papers to clean Markdown. |
| [`deepxiv-baseline-table`](collected-skills/deepxiv-baseline-table/) | Build baseline-comparison tables from DeepXiv searches and paper sections. |
| [`deepxiv-cli`](collected-skills/deepxiv-cli/) | Search and read academic papers through the DeepXiv CLI. |
| [`deepxiv-trending-digest`](collected-skills/deepxiv-trending-digest/) | Produce concise digests of recent DeepXiv trending papers. |
| [`drawio`](collected-skills/drawio/) | Generate draw.io diagrams and optionally export them to PNG, SVG, or PDF. |
| [`explain-diff-html`](collected-skills/explain-diff-html/) | Produce rich HTML explanations of code changes, diffs, branches, and pull requests. |
| [`hf-cli`](collected-skills/hf-cli/) | Work with models, datasets, repositories, and other Hugging Face Hub resources through `hf`. |
| [`hugging-face-paper-pages`](collected-skills/hugging-face-paper-pages/) | Read Hugging Face paper pages and retrieve structured paper metadata. |
| [`human-cognition-cache`](collected-skills/human-cognition-cache/) | Maintain a project-local, git-trackable cache of user context and knowledge state. |
| [`ml-paper-writing`](collected-skills/ml-paper-writing/) | Write and prepare ML/AI papers for major research venues. |
| [`paper-finder`](collected-skills/paper-finder/) | Find, organize, summarize, and cite ML/AI research papers. |
| [`pyzotero`](collected-skills/pyzotero/) | Programmatically manage Zotero libraries using the pyzotero client. |

Before using or redistributing a collected skill, inspect its `SKILL.md`, confirm its upstream source and license, and review any bundled scripts or network access.

## Repository Structure

```text
.
├── skills/                 # Original, gh-installable OpenPaper catalog
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── scripts/        # optional
│       ├── references/     # optional
│       └── assets/         # optional
└── collected-skills/       # Third-party reference archive; not auto-installed
    └── <skill-name>/
        └── SKILL.md
```

Each skill in `skills/` must have a `SKILL.md` file with YAML frontmatter. Its `name` field must match the containing directory name.
