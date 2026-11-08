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
  1. **One-Liner (LSP & Steve Blank Formula)**: Exactly states Language + Software Technology + Purpose (or category, input, and output) without marketing fluff (Missing = FAIL, overly verbose = WARN).
  2. **Credibility Signals**: Build status, release version, and license badges.
  3. **Visual Proof (Picture)**: CLI terminal output, architecture diagram, UI screenshot, or minimal demo GIF (increases star velocity by 2.4x; 31_679.pdf).
  4. **Minimal Quick Start (Push)**: Copy-pasteable verification snippet in $\le$ 3 steps/lines using **Basic code constructs ($\ge$ 92% level A; Sitthithanasakul 2023)** (Missing = FAIL).
- **Hume's Guillotine (Fluff & Sermon Purge)**: Eliminate promotional slogans ("The next generation tool", "Empowering developers") and normative sermons ("Developers ought to..."). State only mechanized functional facts.
- **False Floor (Illusion of Completeness) Prevention**: Ensure the bottom of the first view visually cuts off or leads into the next section (H2 header) rather than dead-ending with excessive whitespace or terminal dividers (`---`).

### Layer 2: Structure & Progressive Disclosure (構成 & 段階的開示)
*Detailed specifications: [`references/layer-2-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-2-rules.md)*

- **3-Tier Architecture (情報の3層強制分離)**:
  - **Tier 1 (概要層 / Overview)**: LSP One-Liner, 視覚的証明, $\le$ 3行のMinimal Quick Startのみを配置。
  - **Tier 2 (根拠・主要仕様層 / Rationale & Core Specs)**: 既存代替との差別化根拠, 主要コンポーネント, 標準利用フロー, 制約境界を配置。
  - **Tier 3 (深層メカニズム・付録層 / Deep Mechanics & Appendix)**: 完全な設定スキーマ, 全CLIフラグ一覧, 高度なチューニング, 内部実装を `<details>` または別ドキュメントへ退避。Tier 1直後へのTier 3配置は **L2 FAIL** (Muralidhar et al. 2025, Springer & Whittaker 2019a)。
- **Cowan's Working Memory Capacity (4±1 チャンキング原則)**:
  - 単一見出し直下に並列提示される箇条書き項目、パラメータ一覧、主要機能数は **最大4個（許容上限5個）** に制限する (Cowan 2001, Kalyuga 2011)。
  - 5個以上の並列項目は上位カテゴリによる2階層クラスタリングまたは折りたたみを適用する (未整理な5個以上 = **L2 WARN**, 8個以上 = **L2 FAIL**)。
- **Structural Collapsible Triggers (構造的・意味論的折りたたみ基準)**:
  - 一次的な利用フロー（ハッピーパス）に直接寄与しない付録情報（全CLIフラグ一覧、網羅的環境変数、補助スキーマ、エッジケースのトラブルシューティング）は、本文から `<details><summary>...</summary></details>` へ折りたたむ (付録仕様の平坦露出 = **L2 WARN**, 主文脈を圧迫する露出 = **L2 FAIL**; Anik & Bunt 2024)。
- **Cognitive Alarm Containment (認知アラーム隔離)**:
  - 初期のメンタルモデル構築に不要な「破壊的操作、高度な設定変更、詳細なトラブルシューティング」をTier 1/2から排除し、最終セクションまたは `<details>` に隔離する (Muralidhar et al. 2025)。
- **Structural Table of Contents (構造的目次基準)**:
  - ドキュメント内に **H2見出しが4個以上（Cowan容量超過）** 存在する場合、読者の全体メンタルマップ構築（Su et al. 2012）を担保するため、Tier 1直下にアンカーリンク付き目次を義務付ける (見出し4個以上で欠落 = **L2 WARN**, リンク破損 = **L2 FAIL**)。
- **Physical Integration (空間的一体化による注意分割排除)**:
  - コードブロック内の引数・オプションの解説が無関係な段落や別見出しを跨いで分離記述されている場合、インラインコメントまたは直近マッピングテーブルへの空間的一体化を強制する (Sweller 2011, Oviatt 2006)。

### Layer 3: Credibility & Two-Sided Signaling (信頼性・両面提示・論証モデル)
*Detailed specifications: [`references/layer-3-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-3-rules.md)*

- **Mandatory Refutational Constraints (反論あり両面提示の義務化)**:
  - Must contain a dedicated constraints section (e.g., `## Limitations & Boundaries` or `## Non-Goals`) (Missing = **L3 FAIL**; Prana 2019).
  - Merely listing limitations without counterarguments degrades persuasiveness ($r = -.060 \sim -.069$; Allen 1991, O'Keefe 1999). Every constraint must follow the **3-Part Tuple**: `[Constraint Fact]` + `[Design Rationale / Trade-off]` + `[Workaround / Recommended Configuration]` (Unrefuted list = **L3 WARN**).
  - **Moderate Importance Principle**: Disclosed constraints must represent boundary conditions (scale limits, unsupported edge-cases) rather than fatal core flaws (which require code fixes = **L3 FAIL**) or trivial cosmetic notes (which add clutter = **L3 WARN**; Kamins et al. 1989).
- **Hype Purge (BAKA Words & Cheap Talk Elimination)**:
  - Detect and purge unsubstantiated marketing adjectives ("ultimate", "blazing fast", "best-in-class", "revolutionary", "flawless", "magic") without objective benchmark data (**L3 FAIL**; Paramitha 2026, Asa & Nautwima 2026).
  - Contextual Numbers: Any performance metric (e.g., "10x faster", "99% smaller") must specify baseline comparison, dataset size, and hardware environment. Unsupported numbers must be converted to functional facts.
- **Toulmin Argumentation Coupling (論証構造の結合)**:
  - Technical claims must satisfy Toulmin's structure: **Claim (主張)** + **Data (実測値)** + **Warrant (推論理由)** + **Backing (裏付け)** + **Rebuttal (例外・無効化条件)**. Fully coupled arguments outperform standard star ratings across competence, integrity, and benevolence ($t \ge 4.89, p < .001$; Rubin & Benbasat 2023).
- **Deeper System Transparency & Autonomy (深層の透明性と自律性保障)**:
  - For tools with automated behaviors or telemetry, explicitly disclose internal mechanics, communication destinations, and provide complete opt-out / customization mechanisms (e.g., `--no-telemetry` flag) to protect user autonomy ($\beta = 0.325, p < .05$; Rahman 2025, Cemiloglu 2021).

### Layer 4: Logical Architecture & Proof (論理構造 & 形式証明)
*Detailed specifications: [`references/layer-4-rules.md`](file:///c:/Users/rikui/Documents/VSCode/ドキュメント論─個人的な自由研究/skills/doc-refine/references/layer-4-rules.md)*

- **Gentzen Subformula Property (部分論理式性質による論理的飛躍検知)**:
  - カット除去定理に基づく部分論理式性質により、結論部や手順部に「前提部（Context/Input）で未定義の外部語彙・外部制約」が突如出現することを論理的飛躍（Non Sequitur）として機械的に検出し、前提部への明示を強制する (未定義語彙の飛躍 = **L4 FAIL**; Gentzen 1934/1935, Prawitz 2018)。
- **Hume's Guillotine Normalization (ヒュームのギロチン検知と条件付き因果文への変換)**:
  - 事実命題（〜である / is）から規範命題（〜すべきである / ought、〜が推奨される）への不当な飛躍を検出し、**「［前提・目的条件］を満たす要件がある場合、［手段］により［結果］が担保される」** という客観的条件付き因果文へ機械的に正規化する (説教的表現の検出 = **L4 FAIL**; David Hume 1739)。
- **Demarcation of RAA vs Consequences (背理法と実用論証の峻別)**:
  - 代替案の批判において、実用上の不利益（コスト・学習負荷等のトレードオフ）を論理的矛盾・絶対的不可能事と偽装する誤謬を検出し、客観的トレードオフ記述へ修正させる (偽装検出 = **L4 WARN**; Jansen 2008, Jacquette 2008)。
- **Enthymeme Disclosure (隠れた前提の開示強制)**:
  - 「$A$ である。したがって $B$ である」という推論において、両者を結ぶ媒介命題が省略されている場合、接続命題の明示を要求する (未根拠推論 = **L4 WARN**; Prawitz 2018)。
- **Assurance Case 3-Tier Separation (アシュアランス構造の3層分離)**:
  - 性能・品質に関する重要主張は、**Claim (主張)** + **Argument (論証)** + **Evidence (証拠)** の3層に明確に分離して記述する (証拠なき主張 = **L4 FAIL**, 論証なき生データ = **L4 WARN**; Rushby 2009, Knight & Yin 2010)。
- **Elimination of Pseudo-Readability (偽の可読性・トートロジー排除)**:
  - コードの字面をなぞっただけの無意味なコメントや説明文（トートロジー）を検出し、前提条件・副作用・例外を含む客観仕様へ書き換えさせる (無意味な反復文 = **L4 WARN**; Börstler & Paech 2016)。

### Layer 5: Empirical Evidence & Replicability (実証根拠 & 検証可能性)
- **Verifiable Commands**: Provide explicit CLI commands or test snippets that the reader can execute to verify claims.
- **Deterministic Outcomes**: State expected terminal output or behavior clearly.

---

## Theoretical & Empirical Backing (文献対応マップ)

This skill synthesizes empirical research and theoretical models across 8 domains and foundational thinking frameworks:

| Domain | Theoretical Basis & Reference | Applied Layer in doc-refine |
| :--- | :--- | :--- |
| **GitHub README & OSS Empirical Studies** | Prana et al., Gaughan et al., Sitthithanasakul et al., Abdulmajeed, Hellman et al., Fronchetti et al., Dantas et al. | **L1, L2** (Must-have sections, LSP pattern, basic code snippets, TOC) |
| **Copywriting & Landing Page Patterns** | PASONA, 4P, FAB, Above-the-Fold attention research | **L1** (Scroll engagement, problem-solution pairing) |
| **Conversion Rate & Bounce Prevention** | Scrolling behavior, Nielsen Norman attention distributions | **L1, L2** (Information placement, scannability) |
| **Credibility & Signaling Theory** | O'Keefe (Two-sided vs one-sided meta-analysis), Spence signaling | **L3** (Mandatory constraints, cost-bearing honesty) |
| **Argumentation & Persuasive Systems** | Toulmin model, PSD frameworks, explainable persuasion | **L3, L4** (Claim-data-warrant coupling, Jansen demarcation) |
| **Progressive Disclosure & Info Architecture** | Muralidhar (Selective Transparency), Springer & Whittaker, Anik & Bunt, Su (Foraging) | **L2** (3-tier architecture, collapsible triggers, structural TOC) |
| **Cognitive Load & Readability** | Sweller Cognitive Load Theory, Cowan ($4 \pm 1$), Börstler (Readability vs Comprehension) | **L2, L4** (Intrinsic/extraneous load reduction, split-attention, pseudo-readability purge) |
| **Logic & Formal Verification** | Gentzen (Cut elimination & subformula property), Prawitz (Inference), David Hume | **L4, L5** (Premise-conclusion consistency, Is-Ought filter, assurance cases) |
| **NaaM Thinking Framework** | Yuzuko Underson (Numbers are a Mirage, 7-layer causal audit) | **L1–L5 Core Backbone** (Unvarnished observation, constraints boundary, validating numbers via causal context) |
