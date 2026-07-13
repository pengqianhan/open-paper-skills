# OpenPaper Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/agent%20skills-Codex%20%C2%B7%20Claude%20Code-blue.svg)](https://agentskills.io/specification)

OpenPaper Skills is the standalone, GitHub CLI-installable distribution of
research skills developed in
[AI-Human Research OS](https://github.com/pengqianhan/AI-Human-Research-OS)'s
`Research-skills-hub`. Use this repository when you want to add a focused
research capability to an existing Codex or Claude Code project.

> Need a complete, long-horizon research workspace rather than individual
> skills? Explore [AI-Human Research OS](https://github.com/pengqianhan/AI-Human-Research-OS)
> for project templates, research memory, human context, a paper wiki, and
> agent operating rules.

![OpenPaper Skills visual overview: modular skills flow into an AI research agent, which produces a polished academic paper with figures, charts, and validated results.](assets/openpaper-skills-hero-v2.png)

## Choose Your Starting Point

| Your goal | Start here |
| --- | --- |
| Add a focused capability to an existing agent project | Install one or more skills from this repository. |
| Plan research, run experiments, and prepare a paper | Start with [`research-bible`](skills/research-bible/) and [`task-file-builder`](skills/task-file-builder/). |
| Maintain a long-lived paper knowledge base | Use [`paper-wiki-manager`](skills/paper-wiki-manager/). |
| Build a complete, durable human-agent research environment | Use [AI-Human Research OS](https://github.com/pengqianhan/AI-Human-Research-OS). |

## Install Skills

The installable catalog follows the Agent Skills convention of
`skills/<skill-name>/SKILL.md`. GitHub CLI `v2.90.0` or later discovers these
directories automatically.

```bash
# Inspect a skill before installation
gh skill preview pengqianhan/openpaper research-bible

# Install one skill for Codex at user scope
gh skill install pengqianhan/openpaper research-bible --agent codex --scope user

# Install every OpenPaper skill for Codex
gh skill install pengqianhan/openpaper --all --agent codex --scope user
```

At project scope, Codex uses the shared `.agents/skills/` directory. See
GitHub's [agent-skills announcement](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/) and the
[Agent Skills specification](https://agentskills.io/specification).

## Installable OpenPaper Catalog

| Skill | Description |
| --- | --- |
<!-- BEGIN GENERATED SKILLS CATALOG -->
| [`codex-paper-figure-skill`](skills/codex-paper-figure-skill/) | Create editable, journal-style academic figures and diagrams from paper text or figure descriptions. |
| [`discover-academic-skills`](skills/discover-academic-skills/) | Find and evaluate research-oriented agent skills with academic-relevance and quality gates. |
| [`drawio-paper`](skills/drawio-paper/) | Generate publication-quality academic diagrams and statistical plots. |
| [`explain-anything-html`](skills/explain-anything-html/) | Produce rich HTML explanations of papers, articles, documentation, and complex concepts. |
| [`human-cognition-cache`](skills/human-cognition-cache/) | Maintain a project-local, git-trackable cache of human context and knowledge state. |
| [`karpathy-coding-rules`](skills/karpathy-coding-rules/) | Apply a focused set of coding rules and working conventions. |
| [`okf-repo-organizer`](skills/okf-repo-organizer/) | Organize repositories and knowledge corpora into Open Knowledge Format bundles. |
| [`paper-wiki-manager`](skills/paper-wiki-manager/) | Maintain a structured paper wiki, including paper notes, concepts, topics, and visualizations. |
| [`research-bible`](skills/research-bible/) | Turn ML/AI research principles into research plans, experiment loops, logs, and debugging routines. |
| [`task-file-builder`](skills/task-file-builder/) | Draft context-rich `task.md` briefs for fresh agent sessions. |
| [`uv-env`](skills/uv-env/) | Create and manage Python environments and dependencies with `uv`. |
<!-- END GENERATED SKILLS CATALOG -->

For catalog maintenance details, see [`skills/README.md`](skills/README.md).

## Sync & Provenance

| Item | Policy |
| --- | --- |
| Development source | [AI-Human Research OS / Research-skills-hub](https://github.com/pengqianhan/AI-Human-Research-OS/tree/main/Research-skills-hub) |
| Public distribution | This repository, which packages selected skills for direct `gh skill` installation. |
| Sync record | Every sync or public release should record the full Research-skills-hub commit SHA in its commit message or release notes. |
| Third-party content | Skills in [`collected-skills/`](collected-skills/) retain their upstream provenance and license; they are not republished as part of the installable catalog. |

This record lets users reconcile an installed release with its development
source, while keeping the standalone catalog easy to install.

### Automatic upstream sync

The [`sync-upstream-skills`](.github/workflows/sync-upstream-skills.yml)
workflow mirrors skill directories from AI-Human Research OS every day and can
also be run manually from the GitHub Actions page. It applies these mappings:

| AI-Human Research OS source | This repository |
| --- | --- |
| `Research-skills-hub/open-paper-skills/<skill>/` | `skills/<skill>/` |
| `Research-skills-hub/collected-skills/<skill>/` | `collected-skills/<skill>/` |

Only child directories containing `SKILL.md` are mirrored. Repository-specific
files such as the root README and each catalog's README/index are preserved.
Paths listed in [`.syncignore`](.syncignore) are excluded. Successful changes
are committed by GitHub Actions, and [`.upstream-revision`](.upstream-revision)
records the exact source commit after the first synchronization.

For immediate synchronization after an upstream change, add this workflow to
`AI-Human-Research-OS/.github/workflows/notify-openpaper-sync.yml`:

```yaml
name: Notify OpenPaper skill sync

on:
  push:
    branches: [main]
    paths:
      - "Research-skills-hub/open-paper-skills/**"
      - "Research-skills-hub/collected-skills/**"

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger OpenPaper sync
        env:
          GH_TOKEN: ${{ secrets.OPENPAPER_DISPATCH_TOKEN }}
        run: |
          gh api repos/pengqianhan/openpaper/dispatches \
            --method POST \
            -f event_type=research-skills-updated \
            -f "client_payload[source_sha]=${GITHUB_SHA}"
```

Create `OPENPAPER_DISPATCH_TOKEN` as a fine-grained personal access token scoped
only to `pengqianhan/openpaper`, with repository `Contents: read and write`, and
save it as an Actions secret in AI-Human Research OS. In this repository, set
**Settings → Actions → General → Workflow permissions** to **Read and write** so
the receiving workflow can commit synchronized files. The daily and manual
sync modes work without the cross-repository token.

## Releases

Validate the catalog before publishing:

```bash
gh skill publish --dry-run
```

Tag releases so users can install a reproducible version:

```bash
gh skill install pengqianhan/openpaper research-bible --pin v0.1.0
```

## Collected Skills Archive

[`collected-skills/`](collected-skills/) is a third-party provenance and
evaluation archive. It is deliberately outside `skills/`, so
`gh skill install pengqianhan/openpaper --all` does not install its contents.
See [`collected-skills/README.md`](collected-skills/README.md) for the full
catalog, upstream links, and intake rules.

## License

OpenPaper-owned code and documentation are licensed under the
[MIT License](LICENSE). Each entry in `collected-skills/` retains its upstream
license and attribution; the repository-level MIT license does not replace
those third-party terms.
