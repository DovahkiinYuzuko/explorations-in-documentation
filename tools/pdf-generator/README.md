# PAPER.md PDF 生成パイプライン

[English](./README.en.md) | **日本語**

本リポジトリの [`PAPER.md`](../../PAPER.md) を Single Source of Truth とし、Pandoc・Typst・Playwright を組み合わせて A4 論文プレプリント形式の PDF（既定出力: `tools/pdf-generator/output/PAPER.pdf`）を生成するためのビルドツールです。

汎用的な Markdown-to-PDF 変換器ではなく、GitHub Releases 向けの自動ビルド（[`.github/workflows/release-paper.yml`](../../.github/workflows/release-paper.yml)）および作者のローカル環境（Windows + WSL + Google Chrome）での手元確認を目的として構成されています。

### 目次
- [構成ファイル](#構成ファイル)
- [前提環境と依存関係](#前提環境と依存関係)
- [実行方法](#実行方法)
- [変換仕様とレイアウト](#変換仕様とレイアウト)
- [設計上のスコープと制約](#設計上のスコープと制約)

### 構成ファイル

| ファイル | 役割 |
| :--- | :--- |
| [`build_pdf.py`](./build_pdf.py) | Markdown の前処理、Mermaid 図の PNG レンダリング、Pandoc による Typst 変換、Typst コンパイルを順に実行するビルドスクリプト。 |
| [`template.typ`](./template.typ) | A4 用紙・余白、和欧混植フォント、Booktabs 風テーブル、引用ブロックの分割制御などを定義する Typst テンプレート。 |
| [`requirements.txt`](./requirements.txt) | `build_pdf.py` の Mermaid 図描画に必要な Python パッケージ（`playwright`）の定義。 |

ビルド時には作業用ディレクトリ `tools/pdf-generator/.build/` が生成され、中間ファイル（`body.md`, `abstract.md`, `body.typ`, `main.typ`, `mermaid_*.png` 等）が出力されます。

### 前提環境と依存関係

#### 1. Python パッケージ
Mermaid 図のブラウザ描画に `playwright` を使用します。

```bash
pip install -r tools/pdf-generator/requirements.txt
```

#### 2. 外部バイナリ・フォント・ブラウザ
実行する OS 環境に応じて参照先が分岐します。

| 環境 | Pandoc / Typst の参照先 | フォント参照先 | ブラウザ（Mermaid 描画用） |
| :--- | :--- | :--- | :--- |
| **Windows（`os.name == "nt"`）** | WSL 内の `~/.local/bin/pandoc` および `~/.local/bin/typst` | WSL 内の `$HOME/.local/share/fonts` | ローカルのインストール済み Google Chrome（自動探索） |
| **Linux / WSL 内実行（CI 含む）** | `PATH` 上の `pandoc` / `typst`（未検出時は `~/.local/bin/`） | `~/.local/share/fonts`（存在する場合）およびシステムフォント | Playwright の Chromium（`PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` で上書き可） |

Linux / CI 環境でブラウザを準備する場合は、あわせて Playwright 用の Chromium を導入します。

```bash
playwright install chromium
```

### 実行方法

リポジトリルートから既定設定のまま実行すると、`PAPER.md` を読み込んで `tools/pdf-generator/output/PAPER.pdf` を生成します。

```bash
python tools/pdf-generator/build_pdf.py
```

入力元や出力先を変更したい場合は `--input` と `--output` を指定します。

```bash
python tools/pdf-generator/build_pdf.py --input PAPER.md --output PAPER.pdf
```

GitHub 上で生成物を配布する場合は、[`.github/workflows/release-paper.yml`](../../.github/workflows/release-paper.yml) が `v*` / `paper-v*` タグの push または手動実行（`workflow_dispatch`）を契機に `ubuntu-latest` 上で同コマンドを実行し、生成した `PAPER.pdf` を GitHub Releases へアップロードします。

### 変換仕様とレイアウト

`build_pdf.py` と `template.typ` は、`PAPER.md` の GitHub 表示用記法を崩さずに PDF 組版へ橋渡しするため、以下の処理を順に行います。

1. **セクション分離と自動目次化**: 最初の `# ` 行を論文タイトル、`## 要旨` で始まる節を要旨（Abstract）として抽出し、`## 目次` 節を除去して Typst 側の `#outline`（深さ 2）に置き換えます。残りの見出しレベルは 1 段繰り上げます（`##` → `#`）。
2. **GitHub 固有記法とリンクの正規化**: コードフェンス外にある `$`...`$` 形式のインライン数式を Pandoc 準拠の `$...$` へ変換し、`./` で始まる相対リンクを GitHub 上の絶対 URL（`blob/HEAD`）へ書き換えます。`<br>` タグは表セル内では半角スペースに、通常行では強制改行に変換します。
3. **Mermaid 図の高解像度画像化**: `mermaid` コードブロックを HTML に埋め込み、Playwright 経由で背景白・`device_scale_factor=4` の PNG 画像として書き出します。
4. **引用ブロックのページ跨ぎ制御**: Pandoc が変換した Typst の `#quote(block: true)` 内で、`#strong[\(日本語訳)]` を境界として原文ブロックと日本語訳・出所ブロックを分割し、それぞれに `breakable: false` を設定します。
5. **和欧混植レイアウト**: A4（上下余白 23mm、左右余白 26mm）をベースに、本文へ `Libertinus Serif` / `Noto Serif CJK JP`（10.5pt）、見出し・表ヘッダ等へ `Noto Sans CJK JP`、数式へ `New Computer Modern Math`、コードへ `DejaVu Sans Mono` を指定しています。

### 設計上のスコープと制約

- **作者の Windows + WSL 環境および CI 環境への特化**
  - *制約事実*: Windows から直接実行した場合、ネイティブ Windows 版の Pandoc / Typst ではなく WSL 内の `~/.local/bin/pandoc`・`~/.local/bin/typst`・`$HOME/.local/share/fonts` を固定パスで呼び出し、ブラウザも `Program Files` または `AppData\Local\Google\Chrome` 配下の Google Chrome のみを探索します。
  - *設計理由*: Windows 側に Typst や日本語 CJK フォントを別途構築したり Playwright 用 Chromium を二重にダウンロードしたりする手間を省き、CI 環境（`ubuntu-latest`）に近い Linux バイナリ環境と既存ローカルブラウザをそのまま流用するためです。
  - *対処法*: 異なる環境で実行する場合は、WSL ターミナル内から Linux としてスクリプトを実行する（`PATH` 上のバイナリを参照します）、GitHub Actions の `workflow_dispatch` でビルドする、あるいは `build_pdf.py` 内のパス定数を自身の環境に合わせて変更してください。
- **`PAPER.md` 固有の見出し・メタデータ構造への依存**
  - *制約事実*: `## 要旨`・`## 目次` という日本語見出しの固定判定、相対リンク変換先の `GITHUB_BLOB_BASE`（`DovahkiinYuzuko/explorations-in-documentation/blob/HEAD`）のハードコード、Mermaid 画像の代替テキスト固定（`統合モデル概念図`）、および `template.typ` 内の著者名既定値（`Yuzuko Underson (DovahkiinYuzuko)`）とヘッダ短縮規則（`：` 区切り）は本リポジトリの `PAPER.md` に固定されています。
  - *設計理由*: 任意の Markdown に広く対応する汎用ツールではなく、`PAPER.md` の組版品質と再現性を優先した専用ビルドスクリプトとして設計しているためです。
  - *対処法*: 別の文書や別リポジトリ向けに転用する場合は、`--input` / `--output` の指定に加えて `build_pdf.py` の定数・見出し判定および `template.typ` の既定引数を対象文書に合わせて書き換えてください。
- **Mermaid 描画時のインターネット接続要件**
  - *制約事実*: 入力 Markdown に `mermaid` コードブロックが含まれる場合、描画用 HTML が `https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js` を読み込むため、実行時にネットワーク接続が必要です。
  - *設計理由*: ローカル環境への Node.js および `@mermaid-js/mermaid-cli` の追加導入を不要とし、Python とブラウザのみで依存を完結させるためです。
  - *対処法*: オフライン環境でビルドする必要がある場合は、Mermaid ブロックを含まない Markdown を対象とするか、`build_pdf.py` の `MERMAID_CDN_URL` をローカルに保存した `mermaid.min.js` の参照へ置き換えてください。
