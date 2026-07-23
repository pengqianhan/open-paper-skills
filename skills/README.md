# OpenPaper Installable Skills

This directory is the standalone, GitHub CLI-installable OpenPaper catalog. The
skills are developed in
[AI-Human Research OS / Research-skills-hub](https://github.com/pengqianhan/AI-Human-Research-OS/tree/main/Research-skills-hub)
and distributed here for direct reuse. Each directory follows the Agent Skills
layout:

```text
skills/<skill-name>/SKILL.md
```

That layout lets GitHub CLI discover these skills automatically. The repository
root [README](../README.md) is the source of truth for public installation,
release, licensing, and AI-Human Research OS guidance.

## Catalog

| Skill | Description |
| --- | --- |
<!-- BEGIN GENERATED SKILLS CATALOG -->
| [codex-paper-figure-skill](codex-paper-figure-skill/) | Create editable, publication-style academic figures from paper text or figure descriptions. |
| [discover-academic-skills](discover-academic-skills/) | Discover and evaluate academic/research agent skills using strict quality and relevance gates. |
| [drawio-paper](drawio-paper/) | Generate publication-quality academic diagrams and statistical plots. |
| [explain-anything-html](explain-anything-html/) | Produce rich HTML explanations of papers, articles, documentation, and complex concepts. |
| [filetree-simple](filetree-simple/) | Generate and lint a compact top-level FILETREE.md navigation map from directory-owned entrypoints. |
| [human-cognition-cache](human-cognition-cache/) | Maintain a project-local, git-trackable cache of human context and knowledge state. |
| [karpathy-coding-rules](karpathy-coding-rules/) | Apply focused coding rules and working conventions. |
| [map-then-territory](map-then-territory/) | Draw a human-verifiable route map from start to destination, then drive agents through the territory edge by edge. |
| [okf-repo-organizer](okf-repo-organizer/) | Organize repositories and knowledge corpora into Open Knowledge Format bundles. |
| [paper-wiki-manager](paper-wiki-manager/) | Maintain a structured paper wiki, including paper notes, topics, concepts, and visualizations. |
| [research-bible](research-bible/) | Turn ML/AI research principles into plans, experiment loops, logs, and debugging routines. |
| [sell-research-honestly](sell-research-honestly/) | Audit evidence and turn research into persuasive, audience-specific value communication without overclaiming. |
| [session-handoff](session-handoff/) | Maintain or resume a repository-root `HANDOFF.md` that transfers a cross-session task arc to a cold session. |
| [skill-organizer](skill-organizer/) | Register a newly added hub skill into its collection's `index.md` and `README.md`. |
| [task-file-builder](task-file-builder/) | Draft context-rich `task.md` briefs for fresh agent sessions. |
| [uv-env](uv-env/) | Create and manage Python environments and dependencies with `uv`. |
| [writing-great-prompt](writing-great-prompt/) | Turn an intent into a lean, copy-ready prompt contract with destination, evidence, authority, and completion bar. |
<!-- END GENERATED SKILLS CATALOG -->

## Install with GitHub CLI

```bash
# Inspect a skill before installation
gh skill preview pengqianhan/openpaper research-bible

# Install one skill for Codex
gh skill install pengqianhan/openpaper research-bible --agent codex --scope user

# Install every OpenPaper skill
gh skill install pengqianhan/openpaper --all --agent codex --scope user
```

Before publishing a release, validate this catalog:

```bash
gh skill publish --dry-run
```

## Maintenance Rules

- Keep `name` in a skill's `SKILL.md` frontmatter identical to its directory name.
- Keep only skills that OpenPaper maintains and publishes in this directory.
  Third-party archival skills belong in [`../collected-skills/`](../collected-skills/).
- Include attribution and license information for any external assets, datasets,
  or reference material bundled with a skill.
- When publishing a sync from Research-skills-hub, record the upstream commit
  in the release notes.
