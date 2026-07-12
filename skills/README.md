# Original OpenPaper Skills

This directory is the canonical catalog of original, repo-maintained OpenPaper
skills. Each directory follows the Agent Skills layout:

```text
skills/<skill-name>/SKILL.md
```

That layout lets GitHub CLI discover these skills automatically. The repository
root [README](../README.md) is the source of truth for the public catalog and
installation guidance.

## Catalog

| Skill | Description |
| --- | --- |
| [codex-paper-figure-skill](codex-paper-figure-skill/) | Create editable, publication-style academic figures from paper text or figure descriptions. |
| [discover-academic-skills](discover-academic-skills/) | Discover and evaluate academic/research agent skills using strict quality and relevance gates. |
| [drawio-paper](drawio-paper/) | Generate publication-quality academic diagrams and statistical plots. |
| [explain-anything-html](explain-anything-html/) | Produce rich HTML explanations of papers, articles, documentation, and complex concepts. |
| [karpathy-coding-rules](karpathy-coding-rules/) | Apply focused coding rules and working conventions. |
| [okf-repo-organizer](okf-repo-organizer/) | Organize repositories and knowledge corpora into Open Knowledge Format bundles. |
| [paper-wiki-manager](paper-wiki-manager/) | Maintain a structured paper wiki, including paper notes, topics, concepts, and visualizations. |
| [research-bible](research-bible/) | Turn ML/AI research principles into plans, experiment loops, logs, and debugging routines. |
| [task-file-builder](task-file-builder/) | Draft context-rich `task.md` briefs for fresh agent sessions. |
| [uv-env](uv-env/) | Create and manage Python environments and dependencies with `uv`. |

## Install with GitHub CLI

```bash
# Inspect a skill before installation
gh skill preview pengqianhan/openpaper research-bible

# Install one skill for Codex
gh skill install pengqianhan/openpaper research-bible --agent codex --scope user

# Install every original OpenPaper skill
gh skill install pengqianhan/openpaper --all --agent codex --scope user
```

Before publishing a release, validate this catalog:

```bash
gh skill publish --dry-run
```

## Maintenance Rules

- Keep `name` in a skill's `SKILL.md` frontmatter identical to its directory name.
- Keep original skills only in this directory. Third-party skills belong in
  [`../collected-skills/`](../collected-skills/).
- Include upstream attribution and license information for any external assets,
  datasets, or reference material bundled with an original skill.
