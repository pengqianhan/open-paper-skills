# Collected Skills

This directory is a provenance archive for third-party skills collected,
evaluated, or adapted in
[AI-Human Research OS / Research-skills-hub](https://github.com/pengqianhan/AI-Human-Research-OS/tree/main/Research-skills-hub).
It is intentionally outside the repository's [`skills/`](../skills/) catalog:
`gh skill install pengqianhan/openpaper --all` does not discover or install
these entries.

Before using or redistributing any collected skill, inspect its `SKILL.md`,
confirm its upstream source and license, and review any bundled scripts or
network access.

The repository-level [MIT License](../LICENSE) covers OpenPaper-owned material
only. It does not replace the attribution or license terms of collected skills.

## Catalog and Provenance

| Skill | Description | Upstream or provenance |
| --- | --- | --- |
<!-- BEGIN GENERATED SKILLS CATALOG -->
| [alphaxiv-paper-lookup](alphaxiv-paper-lookup/) | Look up arXiv papers through AlphaXiv's structured AI-generated overviews. | Third-party community skill; [an exact public copy](https://mz-moonzoo.tistory.com/138) is not an official AlphaXiv release. Verify provenance before redistribution. |
| [arxiv2md](arxiv2md/) | Convert arXiv papers to clean Markdown. | [timf34/arxiv2md](https://github.com/timf34/arxiv2md) (MIT) |
| [deepxiv-baseline-table](deepxiv-baseline-table/) | Build baseline-comparison tables from DeepXiv searches and paper sections. | Adapted from [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main) |
| [deepxiv-cli](deepxiv-cli/) | Search and read academic papers through the DeepXiv CLI. | Adapted from [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main) |
| [deepxiv-trending-digest](deepxiv-trending-digest/) | Produce concise digests of recent DeepXiv trending papers. | Adapted from [DeepXiv/deepxiv_sdk](https://github.com/DeepXiv/deepxiv_sdk/tree/main) |
| [drawio](drawio/) | Generate draw.io diagrams and optionally export them to PNG, SVG, or PDF. | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) |
| [explain-diff-html](explain-diff-html/) | Produce rich HTML explanations of code changes, diffs, branches, and pull requests. | [Geoffrey Litt's skill](https://gist.github.com/geoffreylitt/a29df1b5f9865506e8952488eac3d524) |
| [grill-for-unknowns](grill-for-unknowns/) | Interrogate a plan against docs/source evidence, surface unknown unknowns, and avoid rushing into build mode. | [nicobailon/grill-for-unknowns](https://github.com/nicobailon/grill-for-unknowns), MIT |
| [hf-cli](hf-cli/) | Work with models, datasets, repositories, and other Hugging Face Hub resources through `hf`. | [huggingface/skills](https://github.com/huggingface/skills/blob/main/skills/hf-cli/SKILL.md) |
| [hugging-face-paper-pages](hugging-face-paper-pages/) | Read Hugging Face paper pages and retrieve structured paper metadata. | [huggingface/skills](https://github.com/huggingface/skills/blob/main/skills/hugging-face-paper-pages/SKILL.md) |
| [ml-paper-writing](ml-paper-writing/) | Write and prepare ML/AI papers for major research venues. | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) (MIT) |
| [paper-finder](paper-finder/) | Find, organize, summarize, and cite ML/AI research papers. | Adapted from [bchao1/paper-finder](https://github.com/bchao1/paper-finder/tree/main) |
| [pyzotero](pyzotero/) | Programmatically manage Zotero libraries using the pyzotero client. | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) (MIT) |
<!-- END GENERATED SKILLS CATALOG -->

## Intake Rules

1. Record an upstream URL, source commit or release, license, and any local modifications.
2. Review every executable file and remote endpoint before use.
3. Keep collected skills under `collected-skills/<skill-name>/`; do not place
   them under `skills/` unless their provenance, license, and maintenance
   ownership have been resolved.
4. Move a skill into [`../skills/`](../skills/) only when OpenPaper assumes
  responsibility for maintaining and publishing it as an installable skill.

For the installable original catalog, see the repository root
[README](../README.md) or [`../skills/README.md`](../skills/README.md).
