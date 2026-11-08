---
name: doc-refine
description: Use when creating, reviewing, auditing, or refining technical documentation, READMEs, API guides, or architecture specifications.
---

# doc-refine

A universal agent skill for diagnosing, structuring, and refining technical documentation, READMEs, and specifications. It eliminates unsubstantiated hyperbole, enforces refutational two-sided disclosure of constraints, optimizes first-view clarity, and structures documents for cognitive efficiency and empirical reproducibility.

## Overview

High-quality documentation communicates verifiable facts rather than promotional claims. `doc-refine` audits technical documents against a 5-layer architecture and generates structured, two-sided, reproducible documentation that minimizes cognitive load and maximizes developer trust.

## When to Use

Use this skill when:
- Creating a new README or specification for a project or library
- Reviewing or auditing existing documentation for technical accuracy, clarity, and trust
- Pruning unsubstantiated marketing hype, buzzwords, or normative sermons ("ought"/"should")
- Structuring complex configuration options, flags, and architecture diagrams for cognitive accessibility
- Establishing reproducible verification commands and empirical benchmarks

## When NOT to Use

Do not use this skill for:
- Writing marketing copy, sales landing pages, or promotional blog posts
- Generating code implementations from scratch (use domain-specific coding skills instead)
- Managing issues, project task queues, or sprint tracking (use `local-issues` or similar skills)
- Checking mechanical code formatting or linting errors

---

## Core Principles

1. **No Hype Without Proof (大言壮語の完全排除)**:
   Eliminate hyperbolic adjectives ("ultimate", "blazing fast", "best-in-class") unless supported by mechanized benchmarks and reproducible test conditions.
2. **Two-Sided Disclosure (両面提示の原則)**:
   Every document must articulate boundaries, resource limits, and non-recommended use cases alongside benefits, structured as a 3-part refutational tuple.
3. **Observation Precedes Evaluation (評価より事実の先行)**:
   Above the fold must state objective functional facts (inputs, processing, outputs) before any qualitative claims.
4. **Progressive Disclosure & Cognitive Containment (段階的開示と認知的隔離)**:
   Separate information into 3 tiers. Keep happy paths minimal; isolate exhaustive tables, edge cases, and internals into collapsible sections or appendices.

---

## The 5-Layer Documentation Framework

| Layer | Architecture Layer | Core Focus | Target Questions | Detailed Reference |
| :---: | :--- | :--- | :--- | :--- |
| **L1** | **First View & Anti-Abandonment** | Above the Fold / Observation | What is this tool? What are its inputs/outputs? Can a reader identify its essence in under 5 seconds? | [`references/layer-1-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-1-rules.md) |
| **L2** | **Structure & Progressive Disclosure** | Cognitive Load / Adoption | Is the quick-start minimal ($\le$ 3 lines)? Are deep configs and exhaustive tables collapsed? | [`references/layer-2-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-2-rules.md) |
| **L3** | **Credibility & Two-Sided Signaling** | Signaling Theory / Constraints | Are boundaries and trade-offs disclosed with counterarguments? Are buzzwords purged? | [`references/layer-3-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-3-rules.md) |
| **L4** | **Logical Architecture & Proof** | Deductive Logic / Rationale | Why this over alternatives? Are assertions supported by premises (Gentzen subformula property)? | [`references/layer-4-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-4-rules.md) |
| **L5** | **Empirical Evidence & Replicability** | Validation / Replicability | Are benchmarks accompanied by hardware specs and reproduction commands (NaaM 4-tuple)? | [`references/layer-5-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-5-rules.md) |

*For complete academic citations and empirical backing across 8 domains, see [`references/theoretical-foundations.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/theoretical-foundations.md).*

---

## Execution Protocol

Agents executing `doc-refine` **MUST** follow this three-phase protocol in sequence. Never skip Phase 2 to produce an unapproved rewrite.

```
+-----------------------------------+
| Phase 1: Diagnostic Report        |
| - Evaluate target across L1-L5    |
| - Format via template             |
+-----------------+-----------------+
                  |
                  v
+-----------------+-----------------+
| Phase 2: Adaptive Elicitation     |
| - Prompt user for next action     |
| - Halt and wait for user response |
+-----------------+-----------------+
                  | (User approves rewrite)
                  v
+-----------------+-----------------+
| Phase 3: Refined Rewrite Output   |
| - Output complete Markdown        |
| - Format via standard template    |
+-----------------------------------+
```

### Phase 1: Diagnostic Report
Evaluate the document against Layers 1 through 5 using the specific audit criteria in each reference file.
Load and adhere strictly to the standardized format defined in [`templates/diagnostic-report-template.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/templates/diagnostic-report-template.md).

### Phase 2: Adaptive Elicitation & Progression
After outputting Phase 1, **pause execution** and ask the user how to proceed:
1. **When native question tools (`ask_question`, `AskUserQuestion`) are available:**
   Prompt with options:
   - `(Recommended) Full Rewrite`: Apply all 5-layer recommendations to produce a complete refined document.
   - `Interactive Step-by-Step`: Refine layer by layer interactively.
   - `Target Specific Layers`: Refine only selected layers (e.g., L1 and L3).
   - `Audit Only`: Keep the diagnosis report and finish without text edits.
2. **When native question tools are unavailable (Fallback text):**
   Append a structured selection menu to the response and end turn:
   ```markdown
   ---
   **Next Step Selection:**
   Please reply with your preferred action:
   [1] Full Rewrite (Recommended: Generate complete refined Markdown incorporating all 5 layers)
   [2] Interactive Step-by-Step (Review and approve changes layer by layer)
   [3] Target Specific Layers (Specify which layers to refine, e.g., L1 and L3 only)
   [4] Audit Only (Finish without modifying the document)
   ```

### Phase 3: Refined Rewrite Output
When the user requests a full or partial rewrite, generate the complete refined document following [`templates/refined-readme-template.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/templates/refined-readme-template.md).
- Do not leave placeholder comments or `TODO` items.
- Ensure all constraints follow the 3-part refutational tuple: `[Constraint Fact]` — `[Design Rationale / Trade-off]` — `[Workaround / Recommended Configuration]`.
- Verify that every benchmark number contains the NaaM 4-tuple (Hardware/Runtime, Dataset, Baseline, Variance).

---

## Common Mistakes & Antipatterns

| Antipattern | Description | Remediation |
| :--- | :--- | :--- |
| **Workflow Shortcut** | Jumping straight to rewriting without presenting the Phase 1 diagnosis and obtaining Phase 2 user approval. | Always stop after Phase 1 and wait for explicit user selection. |
| **Unrefuted Limitation Listing** | Listing limitations as bare bullet points without rationale or workarounds ($r = -.069$ in persuasiveness). | Always apply the 3-part refutational tuple: Fact + Rationale + Workaround. |
| **Hume's Guillotine Violation** | Inserting normative preachiness ("Developers ought to...", "You should always..."). | Normalize to objective conditional causality: "When [condition], [mechanism] ensures [result]". |
| **Context Dump (Flat Structure)** | Placing exhaustive CLI flags, full schemas, or troubleshooting steps directly after Quick Start. | Push Tier 3 details into `<details>` collapsible blocks or dedicated reference docs. |
| **Pseudo-Readability** | Adding comments that merely restate the syntax without explaining preconditions, edge-cases, or rationale. | Replace with concrete operational specs or omit extraneous lines. |
