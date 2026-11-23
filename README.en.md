# explorations-in-documentation / ドキュメント論─個人的な自由研究

**English** | [日本語](./README.md)

[![Main Paper](https://img.shields.io/badge/Paper-PAPER.md-8A2BE2?style=flat-square&logo=gitbook&logoColor=white)](./PAPER.md)
[![Paper PDF](https://img.shields.io/badge/PDF-PAPER.pdf-B31B1B?style=flat-square&logo=readthedocs&logoColor=white)](https://github.com/DovahkiinYuzuko/explorations-in-documentation/releases)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-doc--refine-blue?style=flat-square&logo=markdown&logoColor=white)](./skills/doc-refine/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square&logo=opensourceinitiative&logoColor=white)](./LICENSE.MIT)

This repository houses an independent exploratory study on *"What makes good documentation?"* ([**`PAPER.md`**](./PAPER.md)) and the `doc-refine` agent skill implementing its text-based information design principles. Synthesizing primary literature across formal logic, cognitive science, advertising engineering, and psycholinguistics, it proposes a unified hypothesis model free of hype and unverified claims.

Generative AI (LLMs) often inflate documentation with unsubstantiated hyperbole while skipping mechanical verification. Rather than offering superficial grammar checks or rigid fill-in-the-blank templates, this repository provides an information-design lens applicable across text-based documents—from READMEs, specifications, and architecture guides to operational manuals, articles, and plain-text notes.

## Table of Contents
- [Repository Document Architecture](#repository-document-architecture)
- [Overview of the Hypothesis Model](#overview-of-the-hypothesis-model)
- [Installing and Using the `doc-refine` Agent Skill](#installing-and-using-the-doc-refine-agent-skill)
- [Limitations, Boundaries & Trade-offs](#limitations-boundaries--trade-offs)
- [LICENSE](#license)

## Repository Document Architecture

This repository separates documents by role. To read the main body of the study, start with **[`PAPER.md`](./PAPER.md)**.

| Document | Role | Description |
| :--- | :--- | :--- |
| **[`PAPER.md`](./PAPER.md)** | **[Main Paper] Synthesis of the Study** | The comprehensive monograph integrating interdisciplinary literature and primary citations into a 3-Part, 5-Pillar hypothesis model of documentation design. While `PAPER.md` is the Single Source of Truth (SSoT), a direct PDF build (`PAPER.pdf`) is also available on [GitHub Releases](https://github.com/DovahkiinYuzuko/explorations-in-documentation/releases) for readers who prefer PDF. |
| **[`PHILOSOPHY.md`](./PHILOSOPHY.md)** | **[Why] Origins & Philosophy** | The motivation behind the study, the hybrid approach combining formal logic with advertising techniques, and core guiding attitudes. |
| **[`ARCHITECTURE.md`](./ARCHITECTURE.md)** | **[How] Skill Architecture** | Architectural guide mapping each component of `doc-refine` to the underlying theories and empirical findings from cited literature and specifications. |
| **[`REFERENCES.md`](./REFERENCES.md)** | **[Sources] Official Bibliography** | Bibliographic records (DOIs, venues, authors) for the cited literature and their mapping to the chapters of `PAPER.md`. |
| **[`skills/doc-refine/`](./skills/doc-refine/)** | **[Practice] Agent Skill** | The operational skill definition comprising `SKILL.md` (4-Stage Pipeline and dual-track independent audit), four on-demand reference guides, and an emoji detection script. |

## Overview of the Hypothesis Model

In **[`PAPER.md`](./PAPER.md)**, the hypothesis model is organized into three parts and five pillars following the reader's cognitive processing sequence.

### Part I: Perception, Spatial Structure, and Reading Rhythm (Foundation of Readability)
1. **Science of Attention & Onboarding (Chapter 2)**:
   Reader attention concentrates heavily above the fold, yet many OSS READMEs omit *Why* a tool exists and *When* to use it. To reduce initial friction, this pillar covers literal upfront definitions, a single minimal onboarding path, and avoiding visual "False Floors" and conjunction-search delays.
2. **Spatial Structure & Cognitive Load (Chapter 3)**:
   Working memory is limited for novel information, yet readers prefer comprehensive depth over stripped-down summaries. Instead of deleting details, this pillar separates information into three tiers via **Grouping × Separation of Concerns (SoC)**. It also compares structured formats (bullet lists, sentence headlines with visual evidence, tables, and graphs) and distinguishes instructive graphics from decorative visual elements (such as emojis) regarding comprehension and screen-reader accessibility.
3. **Prose Rhythm & Breathing (Chapter 4)**:
   Focusing on the temporal capacity of the phonological loop during silent reading, this pillar examines syntactic dependency complexity and the pitfall of mechanical sentence shortening that inflates lexical density. It also covers balancing parallel syntax for scanning with syntactic variety for prose, five API documentation smells, and the effective boundaries of adjunct questions in expository text.

### Part II: Logic, Credibility, and Boundary Disclosure (Foundation of Trust)
4. **Logical Backbone & Necessity (Chapter 5)**:
   Connects foundational problems deductively through mechanisms to concrete outcomes, while distinguishing *Reductio ad Absurdum* (logical impossibility) from trade-offs (argument from consequences). Guided by Hume's Guillotine, it replaces normative preaching ("should") with objective specifications and conditional causality.
5. **Credibility, Honesty & Boundary Disclosure (Chapter 6)**:
   Avoids unverified hyperbole and AI-induced format bias in favor of comparative baselines with measurement conditions, locally reproducible verification commands, and refutational two-sided constraint disclosure (Constraint Fact + Trade-off Rationale + Workaround). It further covers replacing vague constraints with concrete value ranges and dynamic I/O examples, alongside how reader expertise shifts perceptions of clarity.

### Part III: Context Adaptation and Model Boundaries
6. **A "Lens for Thinking" Rather Than a Rigid Template (Chapter 7)**:
   Imposing fixed fill-in-the-blank forms or blanket bans undermines a document's purpose and authorial voice. Instead, each principle is weighted flexibly according to the medium, audience expertise, and project nature—ranging from production CLI tools, libraries, and Agent Skills to internal specifications, general manuals, casual web toys, and plain-text notes.

## Installing and Using the `doc-refine` Agent Skill

### Installation

The standard installation method for Skills CLI-compatible environments is a single command:

```bash
npx skills add DovahkiinYuzuko/explorations-in-documentation --skill doc-refine
```

In Antigravity environments, install it as a plugin:

```bash
agy plugin install https://github.com/DovahkiinYuzuko/explorations-in-documentation
```

Once installed, invoke it from a compatible agent chat by specifying your target document (e.g., *"Refine `README.md` with `doc-refine`"* or *"Restructure this design spec draft using `doc-refine`"*).

### Execution Workflow (4-Stage Pipeline)

`doc-refine` scales between **Full** mode (new documents or full rewrites) and **Lite** mode (single-section additions or short notes), building documentation in four stages:

1. **Stage 1 (Fact Collection)**: Extracts a fact list—commands, paths, value ranges, boundary behaviors, and constraints—from implementation code, configuration, and tests.
2. **Stage 2 (Bare Minimal Blueprint & Agreement)**: Presents a stripped-down structural and logical blueprint without stylistic embellishment, confirming the author's core intent and any missing facts before drafting.
3. **Stage 3 (Prose Drafting & Format Implementation)**: Writes the full text without compressing agreed facts or boundaries, applying structured formats and natural reading rhythm.
4. **Stage 4 (Dual-Track Independent Audit, Staging & Application)**: Splits review into Part I (perception, structure, rhythm) and Part II (logic, credibility, boundaries, implementation alignment) to counter confirmation bias, reconciles conflicts into a staged physical file with a brief audit summary, and applies changes to the target file after user confirmation.

## Limitations, Boundaries & Trade-offs

In accordance with our disclosure principles, the boundaries and trade-offs of this hypothesis model and skill are stated below:

- **Unverified Nature as a Cross-Disciplinary Model and Domain Gaps**:
  While each cited study carries its own empirical or theoretical backing, this integrated cross-disciplinary model itself has not yet undergone direct large-scale controlled validation. Some cited studies also examine non-technical domains such as learning materials, emails, or language-reading experiments. As an independent exploratory study, the initial priority was to deductively assemble dispersed findings into a testable hypothesis model and prototype it as an agent skill. Treat these principles not as proven laws, but as a repertoire of design lenses to be calibrated through real-world use and reader feedback.
- **Incompatibility with Emotional Copywriting and Familiarity Trade-offs**:
  This framework is not suited for fiction, poetry, emotional essays, or consumer sales letters driven by emotional agitation. Even within technical writing, restraining decorative elements or switching from traditional bullet lists to sentence headlines may feel subjectively less familiar or less ornate to readers accustomed to conventional styles. This reflects a deliberate trade-off prioritizing cognitive clarity, logical transparency, and accessibility; for documents aimed at emotional resonance or immediate visual flair, traditional rhetoric and storytelling techniques are more appropriate.
- **Increased Authoring, Maintenance, and Verification Effort**:
  Verifying baselines, documenting concrete value ranges and dynamic I/O examples, and keeping specs aligned with code changes require more effort than writing brief promotional claims. This model intentionally shifts that cost from readers—who would otherwise spend time searching externally or writing defensive workarounds—onto the authoring side. To keep this workload manageable, human authors focus on core intent and design judgment while delegating fact-checking, structuring, and auditing to `doc-refine`.
- **Single-File Size Growth Under Non-Compression and Markup Dependency**:
  Including value ranges, dynamic I/O examples, and trade-off rationales in a single file (such as `README.md`) without truncation naturally increases raw byte and line counts compared to the original, even when visually collapsed via `<details>`.<br>This reflects a priority on completeness so readers do not need to search external sources or inspect code; however, if the resulting file feels too long or heavy in practice, that size can serve as a practical cue to consider where to apply file-level Separation of Concerns (e.g., splitting deep reference sections into dedicated `docs/` files). Because `<details>` accordions also depend on Markdown/HTML rendering, non-markup environments such as plain text (`.txt`) or RFCs can likewise separate deep details into an appendix or external files.

## LICENSE

[MIT](./LICENSE.MIT)
