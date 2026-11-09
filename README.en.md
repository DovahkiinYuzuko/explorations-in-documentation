# explorations-in-documentation / ドキュメント論─個人的な自由研究

[![Language: 日本語](https://img.shields.io/badge/Language-%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=flat-square)](./README.md)
[![Language: English](https://img.shields.io/badge/Language-%F0%9F%87%BA%F0%9F%87%B8%20English-blue?style=flat-square)](./README.en.md)
[![Main Paper](https://img.shields.io/badge/Paper-PAPER.md-8A2BE2?style=flat-square&logo=gitbook&logoColor=white)](./PAPER.md)
![Agent Skill](https://img.shields.io/badge/Agent_Skill-doc--refine-blue?style=flat-square&logo=markdown&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square&logo=opensourceinitiative&logoColor=white)](./LICENSE.MIT)

An independent exploratory study synthesizing 56 primary sources across 8 domains—formal logic, cognitive science, persuasion engineering, and advertising—to propose a hypothesis model for *"What makes good technical documentation?"* ([**`PAPER.md`**](./PAPER.md)), accompanied by the `doc-refine` agent skill built as a practical prototype of these principles.

---

### Table of Contents
- [explorations-in-documentation / ドキュメント論─個人的な自由研究](#explorations-in-documentation--ドキュメント論個人的な自由研究)
    - [Table of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Repository Document Architecture (The 5 Pillars)](#repository-document-architecture-the-5-pillars)
    - [Core Principles Proposed in This Study (Hypothesis Model)](#core-principles-proposed-in-this-study-hypothesis-model)
    - [Installing the `doc-refine` Agent Skill](#installing-the-doc-refine-agent-skill)
    - [Limitations, Boundaries \& Trade-offs](#limitations-boundaries--trade-offs)
    - [LICENSE](#license)

---

### Overview
This repository began as a personal exploratory study addressing a common tendency in generative AI (LLMs): inflating technical writing with unverified promotional hyperbole while skipping mechanical verification.

Rather than relying on superficial grammar checks or rigid fill-in-the-blank templates, this research investigates how human readers scan text, evaluate logical validity, and form trust—synthesizing findings from 56 academic and empirical sources into an information design hypothesis model applicable to READMEs, specifications, and technical documents.

---

### Repository Document Architecture (The 5 Pillars)

This repository is organized into separated documents by concern. To read the main body of the study, start with **[`PAPER.md`](./PAPER.md)**.

| Document | Role | Description |
| :--- | :--- | :--- |
| **[`PAPER.md`](./PAPER.md)** | **[Main Paper] Synthesis of the Study** | The comprehensive monograph integrating empirical findings and primary citations across 8 domains into a hypothesis model of technical documentation. |
| **[`PHILOSOPHY.md`](./PHILOSOPHY.md)** | **[Why] Origins & Philosophy** | The motivation behind the study, the hybrid approach combining formal logic with advertising techniques, and core guiding attitudes. |
| **[`ARCHITECTURE.md`](./ARCHITECTURE.md)** | **[How] Skill Architecture** | Architectural guide mapping each component of `doc-refine` (`SKILL.md`, `principles.md`, `context-adaptation.md`) to the specific theories and empirical findings from the 56 sources and Agent Skills specifications. |
| **[`CITATIONS.md`](./CITATIONS.md)** | **[Sources] Official Bibliography** | Bibliographic records (DOIs, venues, authors) for the 56 sources and their mapping to the chapters of `PAPER.md`. |
| **[`skills/doc-refine/`](./skills/doc-refine/)** | **[Practice] Agent Skill** | The operational skill definition comprising the 3-step protocol (`SKILL.md`), the 4 design principles (`references/principles.md`), and the context adaptation guide (`references/context-adaptation.md`). |

---

### Core Principles Proposed in This Study (Hypothesis Model)

While detailed in **[`PAPER.md`](./PAPER.md)**, the hypothesis model proposed in this study centers on five perspectives:

1. **Science of Attention & Onboarding**:
   Grounded in eye-tracking tendencies (57% of viewing time concentrated above the fold) and empirical OSS gaps (Why missing in 74.3% and When missing in 78.6% of READMEs), aiming to reduce initial confusion and visual "False Floors."
2. **Cognitive Load & Progressive Disclosure**:
   Reconciling working memory capacity ($4 \pm 1$ chunks for novel information) with the empirical finding that readers prefer high information depth over summaries—avoiding arbitrary deletion of details by structuring them via **Grouping × Separation of Concerns (SoC)**.
3. **Logical Backbone & Necessity**:
   Connecting foundational problems deductively to functional mechanisms and architectural choices, while applying Hume's Guillotine to replace normative preaching ("developers should...") with objective specifications and conditional causality.
4. **Credibility & Refutational Two-Sided Signaling**:
   Replacing cheap talk with comparative baselines, reproducible local verification commands (Witnesses), and refutational two-sided constraint disclosure (Constraint Fact + Design Trade-off Rationale + Workaround), which is expected to foster reader trust.
5. **Context Adaptation Over Rigid Templates**:
   Avoiding one-size-fits-all fill-in-the-blank templates in favor of flexible adaptation tailored to the document's medium and project nature (e.g., production CLI tools, libraries, internal specs, or casual web toys).

---

### Installing the `doc-refine` Agent Skill

**General Agent Environments (Skills CLI Compatible):**
```bash
npx skills add DovahkiinYuzuko/explorations-in-documentation --skill doc-refine
```

**Installation in Antigravity Environments:**
```bash
agy plugin install DovahkiinYuzuko/explorations-in-documentation
```

---

### Limitations, Boundaries & Trade-offs

In accordance with our disclosure principles, the boundaries and trade-offs of this hypothesis model and skill are stated below:

- **Unverified Nature as a Cross-Disciplinary Hypothesis Model**:
  - *Constraint Fact*: While each of the 56 cited studies carries its own empirical or theoretical backing, this integrated cross-disciplinary model itself has not yet undergone direct empirical validation (such as large-scale controlled A/B testing).
  - *Design Rationale*: As an independent exploratory study, the primary objective was to deductively formulate a practical hypothesis model from dispersed literature and prototype it as an AI agent skill.
  - *Workaround / Recommended Configuration*: Treat the principles presented here not as rigid laws, but as a repertoire of design hypotheses ("applying structure X under condition Y is expected to yield effect Z") to be adapted based on actual reader feedback and project context.
- **Incompatibility with Emotional Copywriting and Creative Prose**:
  - *Constraint Fact*: This framework is not suited for fiction, poetry, emotional essays, or consumer sales letters driven by emotional agitation.
  - *Design Rationale*: Designed with a focus on formal logic, refutational two-sided disclosure, and verifiable factual propositions under information asymmetry.
  - *Workaround / Recommended Configuration*: For documents aiming for emotional resonance or narrative lingering, traditional rhetoric and storytelling techniques are better suited.
- **Markup Dependency for Interactive Collapsible Elements**:
  - *Constraint Fact*: Interactive `<details>` accordions require Markdown or HTML rendering support.
  - *Design Rationale*: Adopted to provide information scent while protecting initial working memory within a single document view.
  - *Workaround / Recommended Configuration*: In non-markup environments such as plain text (.txt), RFCs, or inline code comments, apply the underlying structure ("Grouping × SoC") by separating deep reference material into appendices or external pointer files.
- **Ecosystem Fragmentation of Global Skill Discovery Paths**:
  - *Constraint Fact*: Global installations via Skills CLI (`npx skills add -g`) do not populate Antigravity's global configuration directory (`~/.gemini/config/skills/`).
  - *Design Rationale*: Cross-ecosystem standardization of agent skill registries is an emerging domain with differing directory discovery hierarchies.
  - *Workaround / Recommended Configuration*: For Antigravity environments, utilize `agy plugin install` or place the skill into the workspace root `.agents/skills/`.

---

### LICENSE

[MIT](./LICENSE.MIT)
