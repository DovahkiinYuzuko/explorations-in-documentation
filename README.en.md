# explorations-in-documentation / doc-refine

[![Language: 日本語](https://img.shields.io/badge/Language-%F0%9F%87%AF%F0%9F%87%B5%20%E6%97%A5%E6%9C%AC%E8%AA%9E-red?style=flat-square)](./README.md)
[![Language: English](https://img.shields.io/badge/Language-%F0%9F%87%BA%F0%9F%87%B8%20English-blue?style=flat-square)](./README.en.md)
![Agent Skill](https://img.shields.io/badge/Agent_Skill-doc--refine-blue?style=flat-square&logo=markdown&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-5--Layer-brightgreen?style=flat-square&logo=gitbook&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square&logo=opensourceinitiative&logoColor=white)](./LICENSE.MIT)

An independent exploratory study and agent skill `doc-refine` that accepts Markdown technical specifications as input and applies 5-layer constraints grounded in cognitive science and formal logic to output honest, hype-free, reproducible technical documentation disclosing boundaries and trade-offs.

---

### Table of Contents
- [Overview](#overview)
- [Visual Proof of Execution](#visual-proof-of-execution)
- [Installation](#installation)
- [Skill Invocation and Usage](#skill-invocation-and-usage)
- [Steering Goals of the 5-Layer Framework](#steering-goals-of-the-5-layer-framework)
- [Limitations, Boundaries & Trade-offs](#limitations-boundaries--trade-offs)
- [Related Documents](#related-documents)
- [LICENSE](#license)

---

### Overview
This repository is an exploratory research project addressing the tendency of generative AI (LLMs) to use ungrounded promotional rhetoric and skip empirical verification when authoring technical documentation.
By imposing constraints derived from cognitive psychology and formal logic onto agent behavior, the skill `doc-refine` suppresses hyperbole, minimizes reader cognitive load, and generates honest technical documentation (such as READMEs and specifications) aligned with verifiable facts and structural boundaries.

---

### Visual Proof of Execution

The following transcript demonstrates the actual conversational flow and structured diagnostic output when an agent executes this skill (auditing the repository's own `README.md`):

```markdown
> User:
> Audit README.md against doc-refine standards!

> Agent:
> Evaluated the target document against the 5-layer doc-refine architecture (Phase 1).

### Diagnostic Summary
| Layer | Focus | Status | Target Findings & Improvement Points |
| :---: | :--- | :---: | :--- |
| **L1** | First View & Anti-Abandonment | WARN | Abstract LSP One-Liner I/O definition; visual proof missing |
| **L2** | Structure & Progressive Disclosure | WARN | Monolithic multi-language vertical stack inducing scroll fatigue |
| **L3** | Credibility & Two-Sided Signaling | PASS | Hyperbole purged; limitations fulfill 3-part refutational tuple |
| **L4** | Logical Architecture & Proof | PASS | Normative preaching ("ought") purged; unified into causal propositions |
| **L5** | Empirical Evidence & Replicability | WARN | Deterministic expected output snippet missing |

---
**[Phase 2: Adaptive Elicitation / Hard Stop]**
Turn terminated per protocol. Awaiting explicit user selection:
[1] Full Rewrite (Apply all 5-layer recommendations to produce complete refined document)
[2] Interactive Step-by-Step (Review and approve changes layer by layer)
[3] Target Specific Layers (Refine selected layers only)
[4] Audit Only (Finish without modifying the document)
```

As demonstrated above, the agent never rushes ahead to rewrite files unilaterally; it outputs an objective diagnostic table during Phase 1 and immediately enforces a hard stop awaiting explicit human direction.

---

### Installation

Add the skill to your agent environment using one of the methods below:

**General Agent Environments (Skills CLI Compatible):**
```bash
npx skills add DovahkiinYuzuko/explorations-in-documentation --skill doc-refine
```

> [!WARNING]
> **Scope Boundaries Between Skills CLI and Antigravity**
> `npx skills add` installs skills into `.agents/skills/` of the current project or the proprietary paths of supported clients (e.g., Claude Code, Cursor).
> Even when executing `npx skills add -g`, **it does not register skills into Antigravity's global configuration directory (`~/.gemini/config/skills/`)**. To utilize the skill globally across all Antigravity workspaces, refer to the Antigravity-specific setup instructions below.

<details>
<summary>Installation and Usage in Antigravity Environments</summary>

To install as a global plugin in Antigravity, run:
```bash
agy plugin install DovahkiinYuzuko/explorations-in-documentation
```

Alternatively, copy the `skills/doc-refine/` directory from this repository directly into `.agents/skills/` at your workspace root for immediate local recognition.
</details>

---

### Skill Invocation and Usage

Direct your agent to execute the skill on a target specification or document:

```text
/doc-refine README.md
```

- **Workflow and Behavioral Protocol**:
  The skill operates across three structured phases:
  1. **Phase 1 (5-Layer Diagnosis)**: Audits the target document across L1 through L5 metrics (First View, Structure, Credibility, Logic, Evidence) and outputs diagnostic findings.
  2. **Phase 2 (Adaptive Elicitation / Hard Stop)**: Enforces an immediate turn termination following diagnosis to prevent premature unapproved rewriting, awaiting explicit user instructions (Full Rewrite, Step-by-Step, Audit Only).
  3. **Phase 3 (Refined Output)**: Upon user confirmation, generates a structured document disclosing boundaries and trade-offs.

---

### Steering Goals of the 5-Layer Framework

The framework imposes constraints across five layers to systematically align agent output:

- **Layer 1: First View & Anti-Abandonment**:
  Aims to communicate the tool's functional essence and minimal execution instructions above the fold (within the first screen) to prevent cognitive friction and reader abandonment.
- **Layer 2: Structure & Progressive Disclosure**:
  Aims to respect working memory limits by separating minimal happy-path onboarding from exhaustive technical reference tables through Separation of Concerns (SoC).
- **Layer 3: Credibility & Two-Sided Signaling**:
  Aims to strip unverified promotional adjectives and enforce the disclosure of limitations formatted as refutational 3-part tuples (Constraint Fact + Design Rationale + Workaround).
- **Layer 4: Logical Architecture & Fact-Value Separation**:
  Aims to purge normative preaching ("developers ought to...") under Hume's Guillotine and normalize statements into objective conditional causality ("under condition X, mechanism Y ensures result Z").
- **Layer 5: Empirical Evidence & Replicability**:
  Aims to eliminate floating metrics lacking experimental context, requiring self-contained runnable commands alongside explicit hardware and runtime specifications.

---

### Limitations, Boundaries & Trade-offs

In accordance with our own disclosure principles, the architectural constraints of this skill are explicitly stated:

- **Markup Dependency for Interactive Collapsible Elements**:
  - *Constraint Fact*: The `<details>` tags recommended by the default specification require Markdown or HTML rendering support.
  - *Design Rationale*: Adopted to provide an engaging information scent while preserving initial working memory.
  - *Workaround / Recommended Configuration*: In non-markup environments such as plain text (.txt), RFC, or internal specification environments, apply the underlying principle ("Grouping × SoC") by isolating references into appendices or external pointer files.
- **Incompatibility with Emotional Copywriting and Creative Prose**:
  - *Constraint Fact*: This framework is not intended for emotional essays, poetry, or persuasive sales copy.
  - *Design Rationale*: Strictly optimized for formal logic, refutational two-sided honesty, and verifiable factual propositions.
  - *Workaround / Recommended Configuration*: For documents aiming for emotional resonance or immediate commercial conversion, traditional sales copywriting methods should be utilized instead.
- **Ecosystem Fragmentation of Global Skill Discovery Paths**:
  - *Constraint Fact*: Global installations via Skills CLI (`npx skills add -g`) do not populate Antigravity's global configuration directory (`~/.gemini/config/skills/`).
  - *Design Rationale*: Cross-ecosystem standardization of agent skill registries is an emerging domain with differing directory discovery hierarchies.
  - *Workaround / Recommended Configuration*: For Antigravity environments, utilize `agy plugin install` or place the skill into the workspace root `.agents/skills/`.

---

### Related Documents

- **[`PHILOSOPHY.md`](./PHILOSOPHY.md)**: Origins and design philosophy of the project.
- **[`ARCHITECTURE.md`](./ARCHITECTURE.md)**: Technical rationale and empirical literature citations for the 5 layers.
- **[`CITATIONS.md`](./CITATIONS.md)**: Official bibliography mapping theoretical sources.
- **[`skills/doc-refine/`](./skills/doc-refine/)**: Agent skill definition and evaluation rules.

---

### LICENSE

[MIT](./LICENSE.MIT)
