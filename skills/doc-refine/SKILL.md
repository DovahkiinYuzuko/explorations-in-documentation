---
name: doc-refine
description: Use when creating, reviewing, auditing, or refining technical documentation, READMEs, or project specifications. Diagnoses documentation across 5 architectural layers—First View (Observation), Progressive Disclosure (Adoption), Credibility & Two-Sided Signaling (Constraints), Logical Structure (Rationale), and Empirical Evidence (Validation & Replicability)—eliminates unsubstantiated hyperbole, and provides structured rewrites.
---

# doc-refine

A universal, cross-runtime agent skill for auditing and refining technical documentation, READMEs, and specifications. It eliminates unsubstantiated hype, enforces two-sided disclosure of constraints, optimizes first-view clarity, and structures documents for cognitive efficiency and reproducibility.

## Core Principles

1. **No Hype Without Proof (大言壮語の完全排除)**:
   Never use hyperbolic adjectives ("ultimate", "blazing fast", "supreme") without mechanized, objective benchmarks and reproducible test conditions.
2. **Two-Sided Disclosure (両面提示の原則)**:
   Every piece of documentation must articulate what the software cannot do, its boundaries, resource limits, and non-recommended use cases alongside its benefits.
3. **Observation Precedes Evaluation (評価より事実の先行)**:
   The first view (Above the fold) must state what the software actually does, its inputs, and its outputs without promotional commentary.
4. **Adaptive Elicitation (環境適応型対話プロトコル)**:
   Audit findings must be presented with clear decision points. The skill adapts to native agent elicitation tools when present, and falls back to structured text options otherwise.

---

## The 5-Layer Documentation Framework

When diagnosing or authoring documentation, evaluate each layer independently:

| Layer | Architecture Layer | Core Focus | Target Questions |
| :---: | :--- | :--- | :--- |
| **L1** | **First View & Anti-Abandonment**<br>(ファーストビュー & 離脱防止) | Above the Fold / Observation | What is this tool? What are its inputs and outputs? Can a reader identify its essence in under 5 seconds without marketing fluff? |
| **L2** | **Structure & Progressive Disclosure**<br>(構成 & 段階的開示) | Cognitive Load / Adoption | Is the quick-start minimal? Are heavy details, edge-case configs, and deep tables collapsed to preserve working memory? |
| **L3** | **Credibility & Two-Sided Signaling**<br>(信頼性 & 両面提示) | Signaling Theory / Constraints | Are boundaries, limitations, and trade-offs explicitly disclosed? Are all hyperbolic claims and empty adjectives stripped? |
| **L4** | **Logical Architecture & Proof**<br>(論理構造 & 形式証明) | Deductive Logic / Rationale | Why this over existing alternatives? Are assertions supported by premises? Is there any logical leap or contradiction? |
| **L5** | **Empirical Evidence & Replicability**<br>(実証根拠 & 検証可能性) | Validation / Replicability | Are benchmarks accompanied by environment specs and reproduction steps? Can another developer reproduce the claims? |

---

## Output Contract (出力契約)

When executing `doc-refine`, agents **MUST** follow this two-phase structure in sequence. Do not collapse them or omit steps.

### Phase 1: Diagnostic Report (5層診断レポート)

Output a structured diagnosis evaluating the target document against the 5 layers:

```markdown
## Documentation Audit Report: [Document Name / Title]

### Layer Evaluation

| Layer | Status | Score (1-5) | Key Findings / Deviations |
| :--- | :---: | :---: | :--- |
| **L1: First View** | [PASS / WARN / FAIL] | X/5 | [Observation: clarity of inputs/outputs, first 5 lines] |
| **L2: Structure** | [PASS / WARN / FAIL] | X/5 | [Cognitive load, progressive disclosure, quick start] |
| **L3: Credibility** | [PASS / WARN / FAIL] | X/5 | [Two-sided constraints, hyperbole detection, BAKA words] |
| **L4: Logic** | [PASS / WARN / FAIL] | X/5 | [Why/Rationale, comparison with alternatives, consistency] |
| **L5: Evidence** | [PASS / WARN / FAIL] | X/5 | [Reproducibility of claims, verification commands] |

### Critical Issues (重大な改善点)
1. **[Layer X]**: [Specific flaw, quoted text, and why it degrades trust or readability]
2. **[Layer Y]**: [Specific flaw, quoted text, and why it degrades trust or readability]
```

### Phase 2: Adaptive Elicitation & Progression (対話分岐)

After presenting Phase 1, the agent **MUST** pause execution and confirm the next action with the user using the following protocol:

#### 1. When native question tools (`ask_question`, `AskUserQuestion`, etc.) are available:
Invoke the tool with:
- **Question**: "How would you like to proceed with refining this documentation?"
- **Options**:
  - `(Recommended) Full Rewrite`: Apply all 5-layer recommendations and generate the complete, refined Markdown document.
  - `Interactive Step-by-Step`: Refine Layer by Layer interactively, starting from Layer 1.
  - `Target Specific Layers`: Refine only selected layers (e.g., L3 Two-Sided Constraints & L1 First View).
  - `Audit Only`: Keep the diagnosis report and finish without code/text changes.

#### 2. When native question tools are NOT available (Fallback):
Append the following text prompt to the end of the response and end turn:
```markdown
---
**Next Step Selection:**
Please reply with your preferred action:
[1] Full Rewrite (Recommended: Generate complete refined Markdown incorporating all 5 layers)
[2] Interactive Step-by-Step (Review and approve changes layer by layer)
[3] Target Specific Layers (Specify which layers to refine, e.g., L1 and L3 only)
[4] Audit Only (Finish without modifying the document)
```

---

## Detailed Audit Criteria by Layer

### Layer 1: First View & Anti-Abandonment (Above the Fold)
*Detailed specifications: [`references/layer-1-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-1-rules.md)*

- **The 4 Pillars of Above the Fold**: Within the first screenful (top 50 lines / 1080px viewport, which captures **57% of total viewing time**), verify the presence of:
  1. **One-Liner (LSP & Steve Blank Formula)**: Exactly states Language + Software Technology + Purpose (ssrn-4543196, median 15–16 words) or category, input, and output without marketing fluff.
  2. **Credibility Signals**: Build status, release version, and license badges.
  3. **Visual Proof (Picture)**: CLI terminal output, architecture diagram, UI screenshot, or minimal demo GIF (increases star velocity by 2.4x; 31_679.pdf).
  4. **Minimal Quick Start (Push)**: Copy-pasteable verification snippet in $\le$ 3 steps/lines using **Basic code constructs ($\ge$ 92% level A; Sitthithanasakul 2023)**.
- **Hume's Guillotine (Fluff & Sermon Purge)**: Eliminate promotional slogans ("The next generation tool", "Empowering developers") and normative sermons ("Developers ought to..."). State only mechanized functional facts.
- **False Floor (Illusion of Completeness) Prevention**: Ensure the bottom of the first view visually cuts off or leads into the next section (H2 header) rather than dead-ending with excessive whitespace or terminal dividers (`---`).

### Layer 2: Structure & Progressive Disclosure (Adoption & Scanning)
*Detailed specifications: [`references/layer-1-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-1-rules.md)*

- **Standard Skeleton Order (Prana et al. 2019 / Abdulmajeed 2024)**:
  1. `Title & One-Liner` $\rightarrow$ 2. `Badges & Visual Proof` $\rightarrow$ 3. `Why & Key Features (FAB)` $\rightarrow$ 4. `Quick Start` $\rightarrow$ 5. `Prerequisites & Installation` $\rightarrow$ 6. `Usage & Configuration` $\rightarrow$ 7. `Limitations & Boundaries` $\rightarrow$ 8. `License`.
- **Optimal Document Length**: Target **500–1,000 words** (the empirical peak for newcomer attraction at 62.1%; drops to 31.3% when $>8,000$ words; Abdulmajeed 2024/2026).
- **Supply-Demand Gap Resolution (The Why Factor)**: Explicitly provide a 1-paragraph rationale answering "Why this over alternatives?" (demanded by 59.6% of developers, missing in 74.3% of repos; Prana 2019).
- **F-Pattern Scanning Optimization (78% of Readers Scan)**:
  - Paragraph text must not exceed **3 consecutive lines**.
  - Bullet points must front-load action verbs or key nouns in the first 3 words.
  - Bold text must serve as anchor points for fast eye scanning.
- **Information Collapsing**: Detailed parameter tables, exhaustive flag references, and troubleshooting matrices exceeding 20 lines must be placed in `<details><summary>...</summary></details>` blocks or separate reference documents.
- **TOC Threshold**: Do not include a Table of Contents for documents $\le$ 150 lines (avoids scroll friction); require a TOC only when $> 150$ lines.

### Layer 3: Credibility & Two-Sided Signaling
- **Mandatory Constraints Section**: Must contain a dedicated section such as `## Limitations & Boundaries` or `## Non-Goals`.
- **BAKA Words Purge**: Search and remove: "ultimate", "best-in-class", "revolutionary", "flawless", "infinite", "super".
- **Contextual Numbers**: Any number (e.g., "10x faster", "99% smaller") must include comparison baseline, test data size, and runtime environment. If unsupported, convert to qualitative functional description.

### Layer 4: Logical Architecture
- **Rationale Disclosure**: Clearly articulate why this project exists versus existing standard solutions.
- **Non-Contradiction**: Ensure prerequisites in Layer 3 match installation commands in Layer 2.

### Layer 5: Empirical Evidence & Replicability
- **Verifiable Commands**: Provide explicit CLI commands or test snippets that the reader can execute to verify claims.
- **Deterministic Outcomes**: State expected terminal output or behavior clearly.

---

## Theoretical & Empirical Backing (文献対応マップ)

This skill synthesizes empirical research and theoretical models across 8 domains and foundational thinking frameworks:

| Domain | Theoretical Basis & Reference | Applied Layer in doc-refine |
| :--- | :--- | :--- |
| **GitHub README & OSS Empirical Studies** | Prana et al., Gaughan et al., Sitthithanasakul et al., Abdulmajeed, Hellman et al., Fronchetti et al., Dantas et al. | **L1, L2** (Must-have sections, LSP pattern, 500-1000 word sweetspot, basic code snippets) |
| **Copywriting & Landing Page Patterns** | PASONA, 4P, FAB, Above-the-Fold attention research | **L1** (Scroll engagement, problem-solution pairing) |
| **Conversion Rate & Bounce Prevention** | Scrolling behavior, Nielsen Norman attention distributions | **L1, L2** (Information placement, scannability) |
| **Credibility & Signaling Theory** | O'Keefe (Two-sided vs one-sided meta-analysis), Spence signaling | **L3** (Mandatory constraints, cost-bearing honesty) |
| **Argumentation & Persuasive Systems** | Toulmin model, PSD frameworks, explainable persuasion | **L3, L4** (Claim-data-warrant coupling) |
| **Progressive Disclosure & Info Architecture** | Nielsen usability, selective transparency models | **L2** (Visual hierarchy, collapsible detail structures) |
| **Cognitive Load & Readability** | Sweller Cognitive Load Theory, comment comprehension studies | **L2, L4** (Intrinsic/extraneous load reduction) |
| **Logic & Formal Verification** | Deductive logic, proof theory, contradiction detection | **L4, L5** (Premise-conclusion consistency) |
| **NaaM Thinking Framework** | Yuzuko Underson (Numbers are a Mirage, 7-layer causal audit) | **L1–L5 Core Backbone** (Unvarnished observation, constraints boundary, validating numbers via causal context) |
