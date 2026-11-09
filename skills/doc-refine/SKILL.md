---
name: doc-refine
description: Designs, crafts, audits, and refines technical documentation and READMEs. Converts marketing hyperbole into verifiable facts, applies refutational two-sided constraint disclosure, enforces above-the-fold Quick Starts, and structures documents for cognitive efficiency. Use when writing new READMEs or specifications from scratch (0-to-1), or auditing and rewriting existing technical documents (1-to-10). Triggers on requests like "refine documentation", "write README", "audit technical doc", "eliminate hype", or "structure spec".
---

# doc-refine

A lightweight operational protocol for drafting, auditing, and refining technical documentation and READMEs. It eliminates promotional hyperbole, enforces refutational two-sided constraint disclosure, optimizes first-view cognitive accessibility, and grounds every claim in verifiable facts.

## When to Use

Use this skill when:
- **0→1 Drafting**: Creating a brand-new README, API guide, or architecture specification from project context or source code.
- **1→10 Refinement**: Auditing and rewriting existing documentation to prune promotional buzzwords, eliminate normative preachiness ("ought"/"should"), and structure cognitive flow.
- Preparing documents for public release where developer trust, clarity, and rapid adoption are critical.

## When NOT to Use

Do not use this skill for:
- Writing consumer marketing copy, sales landing pages, or promotional blog posts.
- Generating application source code (use domain-specific coding workflows).
- Project task tracking or issue management (use `local-issues` or similar skills).
- Line-by-line syntax linting or code formatting.

---

## Operational Workflow

Agents executing `doc-refine` follow this 3-step sequence:

```
[1. Mode Selection & Analysis]
       |
       +---> Mode A: 0→1 Drafting (From scratch)
       +---> Mode B: 1→10 Refinement (Existing text)
       |
[2. Plan Presentation & User Confirmation (Hard Stop)]
       |
       v (User approves plan)
[3. Structured Document Generation]
```

### Step 1: Mode Selection & Analysis

Determine the operational mode based on user intent and target files:

1. **Mode A: 0→1 Drafting (New Document)**
   - Analyze source code, package manifests, and project context.
   - Load patterns from `references/patterns-0to1-creation.md`.
   - Identify: (a) Axiomatic problem (Why), (b) LSP Pattern, (c) Level A minimal example, (d) Known constraints.

2. **Mode B: 1→10 Refinement (Existing Document)**
   - Inspect existing documentation.
   - Load patterns from `references/patterns-1to10-refinement.md`.
   - Scan for:
     - Undefined comparative adjectives ("fast", "lightweight", "best-in-class").
     - Normative moralizing statements ("developers ought to...", "you should always...").
     - Unrefuted bare limitations (negative bullets without rationale or workarounds).
     - Flat cognitive overload (H2 $\ge$ 4 without TOC, lists $> 5$ items without chunking).

### Step 2: Plan Presentation & User Confirmation (Hard Stop)

**MANDATORY STOP**: Present a concise strategy plan to the user before writing or rewriting full documents:
- Identified mode (Drafting or Refinement).
- Key patterns to apply (e.g., LSP formulation, 3-element constraint tuples, TOC restructuring).
- Target files and proposed structural outline.
- **End turn immediately and wait for user approval.**

### Step 3: Structured Document Generation

Upon user confirmation, output the complete, production-ready document adhering to `references/readme-template.md`:
- Do not output placeholders or unexpanded `TODO` markers.
- Keep Tier 1 concise ($\le$ 50 lines before Quick Start).
- Isolate Tier 3 technical depths (exhaustive CLI flags, schemas) inside `<details>` blocks or separate files.

---

## Core Execution Rules

### 1. The LSP One-Liner Pattern
The very first sentence under the project header must follow the LSP formula:
```
[Language / Environment] + [Software Category] + [Specific Problem Solved / Purpose]
```
*Example*: "A zero-dependency Python 3.11+ CLI tool that audits OpenAPI schemas against breaking changes."

### 2. Level A Quick Start
Quick Start snippets must use only elementary syntax (assignments, imports, attribute access). Avoid complex list comprehensions, lambdas, or unneeded async boilerplate. Keep runnable in $\le$ 3 lines.

### 3. Refutational Two-Sided Disclosure
Never list technical limitations as bare negative bullets. Every constraint must be formulated as a 3-element tuple:
1. **Fact**: Exact limitation, boundary, or non-recommended environment.
2. **Rationale**: Architectural trade-off or engineering reason.
3. **Alternative**: Recommended workaround or alternative configuration.

### 4. Hume's Guillotine (Fact-Value Separation)
Eliminate all normative preaching ("should", "ought", "must", "best practice"). Replace with objective conditional causality:
- *Bad*: "You must always set the pool size to 10."
- *Good*: "To prevent connection exhaustion under burst traffic, configure the connection pool size to 10 or higher."

### 5. Baselines for Benchmarks
Never write "blazing fast" or "10x performance" without an explicit baseline and hardware note:
```markdown
> [!NOTE]
> Tested on AMD Ryzen 9 7950X, Ubuntu 24.04 with a 10MB dataset. Processing time was 42ms vs 89ms on v1.2 (2.1x speedup). Results vary by hardware and dataset structure.
```

### 6. Cognitive Chunking & Progressive Disclosure
- Restrict parallel bullet points under any single heading to $4 \pm 1$ items.
- Provide a Markdown Table of Contents (TOC) whenever a document contains 4 or more H2 headings.
- Move exhaustive tables, full schemas, and low-level diagnostic guides into collapsible `<details>` tags or external files.

---

## Antipatterns to Avoid

| Antipattern | Description | Remediation |
| :--- | :--- | :--- |
| **Premature Execution** | Rewriting entire documents without presenting Step 2 plan and waiting for user approval. | Halt after Step 2 plan output and wait for explicit confirmation. |
| **Bare Limitation Dumping** | Listing limitations without architectural rationale or workarounds ($r = -.060$ in persuasiveness). | Formulate as 3-element tuple: Fact + Rationale + Alternative. |
| **Unanchored Adjectives** | Using "fast", "simple", "scalable" without baselines or mechanisms. | State the concrete mechanism (e.g., "in-memory index") and provide test baselines with `[!NOTE]`. |
| **Normative Sermonizing** | Lecturing developers on how they "should" build software. | Convert to conditional causality: "When [condition], [mechanism] produces [result]." |
| **Context Dump** | Dumping 20 CLI flags or full configuration schemas directly after the introduction. | Encapsulate Tier 3 data within `<details>` or separate reference files. |

---

## Reference Guides

- [0→1 Drafting Patterns](references/patterns-0to1-creation.md): In-depth guide for axiomatic Why, LSP pattern, and Level A code design.
- [1→10 Refinement Patterns](references/patterns-1to10-refinement.md): Replacement catalogs for hyperbolic adjectives, Hume's guillotine, and chunking.
- [Standard README Template](references/readme-template.md): Complete, copy-pasteable Markdown template.
