# doc-refine Layer 1 詳細監査基準リファレンス
## ファーストビュー・基本構成・離脱防止の定量的評価仕様

本リファレンスは、`doc-refine` スキルにおいてドキュメントのファーストビュー（Layer 1: First View & Anti-Abandonment）を客観的・論理的に監査・リライトするための詳細判定基準である。

---

## 1. Layer 1: First View (Above the Fold) 監査判定基準

閲覧時間が集中する Above the Fold（最上部1画面 / 1080px高以内、または最初の50行以内）において、以下の4要素が揃っているかを判定する。

### 1.1 4大必須構成要素 (The 4 Pillars of Above the Fold)

| 要素 | 必須要件・判定ルール | 違反時の判定 |
| :--- | :--- | :---: |
| **① One-Liner (LSP型)** | プロジェクト名直下に配置。<br>LSPパターン（Language + Software Technology + Purpose）で「何をするものか」「主要入力」「主要出力」を明記。<br>抽象的なスローガン・ポエムを禁止。<br>※完全欠落は **FAIL**、情報過多・冗長な場合は **WARN**。 | **完全欠落: L1 FAIL**<br>冗長: L1 WARN |
| **② Credibility Signal (バッジ/証明)** | ビルドステータス、バージョン、ライセンス等の客観的シグナルを提示。未検証の自称評価は不可。 | **L1: WARN** |
| **③ Visual Proof (Picture)** | CLIの入出力ログ、ターミナルGIF、またはUIスクリーンショット。<br>「どう動くか」をスクロールなしで視覚的に証明する。 | **L1: WARN** |
| **④ Minimal Quick Start (Push)** | コピペで即座に動作する $\le$ 3行の最小実行コマンド。<br>コードは **Basic構文（Level A: 単純代入・属性アクセス）** を厳守し、高度な技巧的構文（内包表記・メタプロ等）を排除。<br>※完全欠落は **FAIL**。 | **L1: FAIL** |

---

## 2. One-Liner & Why の設計テンプレート

### 2.1 LSPパターン One-Liner (機能的事実)
```markdown
[Language] implementation of [Software Technology] for [Purpose].
[ツール名] is a [カテゴリ名] that [主要な機能・処理] from [入力] into [出力] without [不要な依存/複雑さ].
```
- **Bad (スローガン・形容詞の過剰)**:
  - ❌ `SuperFastParser is the ultimate next-generation AI parser built to revolutionize your workflow.`
  - ❌ `Collect, Analyze and Share`
- **Good (客観的機能事実・LSP準拠)**:
  - ⭕ `TypeScript zero-dependency CLI tool for converting unformatted Markdown tables into normalized JSON schema.`

### 2.2 Positioning Statement (Why / 既存手法との差別化)
冒頭または特徴セクションの先頭に以下を配置し、既存手法との差異と採用理由を明示する：
```markdown
Unlike existing [代替ツールA, B] which [既存手法の摩擦・制限], [本ツール] [独自の解決アプローチ] to provide [具体的な実利].
```
- **Good 例**:
  - `Unlike standard markdown linters that only enforce indentation, doc-refine validates document structure against structural complexity and progressive disclosure.`

---

## 3. 標準セクション構成マトリクス

READMEは原則として以下の順序で構成する。全体像の把握を妨げる長大なドキュメントに対しては、`<details>` による情報の折りたたみや目次、別ドキュメントへの段階的開示（Progressive Disclosure）が提供されているかを評価する。

| 順序 | セクション名 | 必須度 | 最大許容行数 | 役割と離脱防止機能 |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Title & One-Liner (LSP)** | **必須 (MUST)** | 5行 | ツールの識別、カテゴリと入出力の確定 |
| **2** | **Badges & Visual Proof** | **推奨 (SHOULD)** | 10行 | 視覚的証明、実稼働の提示 |
| **3** | **Why & Key Features** | **必須 (MUST)** | 15行 | 既存手法との差別化、実利の提示 |
| **4** | **Quick Start / Minimal Example** | **必須 (MUST)** | 10行 | 3ステップ以内の即時動作確認、Basic構文 |
| **5** | **Prerequisites & Installation** | **必須 (MUST)** | 15行 | 動作環境、バージョン要件の事前開示 |
| **6** | **Usage & Advanced Config** | 任意 | - | 詳細オプション（20行超は `<details>` で折りたたみ） |
| **7** | **Limitations & Boundaries (両面提示)** | **必須 (MUST)** | 15行 | 境界条件、反証可能性、制約の事前開示 |
| **8** | **License & Contribution** | **必須 (MUST)** | 10行 | 法的利用可否、導線 |

---

## 4. 離脱防止と走査誘導のメカニズム

### 4.1 False Floor（完了の錯覚）の排除ルール
- **禁止パターン**:
  - ファーストビューの最下部に大きな水平線（`---`）や巨大な空行を配置し、視覚的にページが完結したように見せること。
- **遵守パターン**:
  - ファーストビューの折り目境界線上に、次セクションのH2見出し（例: `## 使い方` や `## 特徴`）をチラ見せ（Cut-off）させる。
  - 下方向への視線移動を物理的に誘発する。

### 4.2 Fパターン走査（Scanning）最適化ルール
- **パラグラフ制限**: 説明文のパラグラフ（地の文）は **連続3行以内** とする。4行以上の長文は箇条書きまたはテーブルに分割する。
- **フロントローディング（Front-loading）**: 箇条書きの先頭3単語に重要な名詞・動詞を配置する（接続詞や前置きで始めない）。
- **太字アンカー**: 読者が流し読みする際に視線が停留するよう、コア機能やキー数値を **太字** で強調する。

### 4.3 目次（Table of Contents）の設置閾値
- **H2見出し $\le$ 3個**: 目次は設置しない（目次自体が不要なスクロール負荷となるため）。
- **H2見出し $\ge$ 4個**: Quick Startの直後にアンカーリンク付き目次を設置し、長大なドキュメント内の特定セクションへダイレクトジャンプ可能にする。
