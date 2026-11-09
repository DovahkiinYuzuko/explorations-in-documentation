# 参考文献公式目録 (CITATIONS & Traceability Matrix)

本ドキュメントは、「ドキュメント論─個人的な自由研究」およびエージェントスキル `doc-refine` の設計基盤となった全学術文献・理論モデル・一次資料の公式文献目録（Bibliography）である。
全8カテゴリ（全54文献＋3基盤公理）の書誌情報（DOI / 掲載誌 / 著者）、抽出された実測データ・理論モデル、およびドキュメント工学フレームワーク（5層アーキテクチャ: Layer 1〜5）への直接的な作用（Informed Insights & Applied Mechanisms）を決定論的に記録する。

---

## 1. 導出・作用トレーサビリティマトリクス (Traceability Matrix)

| 文献ID | 領域 | 主要文献・著者 | 抽出実測データ・理論モデル | 5層アーキテクチャへの直接の作用 |
| :--- | :--- | :--- | :--- | :--- |
| **`[REF-PRANA2019]`** | GitHub/OSS実証 | Prana et al. (2019) | 393リポジトリ解析。Why欠落率74.3%、When欠落率78.6%。 | **L1** Why配置（目的の明示）、**L3** 制約セクション（What-Not）必須化 |
| **`[REF-SITTHI2023]`** | GitHub/OSS実証 | Sitthithanasakul et al. (2023) | PyPI 1,620件解析。スニペットの92%がBasic構文（Level A: 基本構文）。 | **L1** Quick Start Basic構文規範（Level A強制、技巧的構文排除） |
| **`[REF-ABDUL2024]`** | GitHub/OSS実証 | Abdulmajeed (2026) | 717リポジトリCatBoost/SHAP解析。README長が静的ドキュメント要因中第1位（平均SHAP 0.420）。中程度の長さでピークに達する非線形関係。 | **L1** ファーストビュー（50行以内）、**L2** 3層情報分離（過長ドキュメントの分割） |
| **`[REF-HELLMAN2023]`**| GitHub/OSS実証 | Hellman et al. (2023) | GitHub概要欄の実態調査。高品質リポジトリから創発した **LSP（Language, Software technology, Purpose）** パターンが読者に最も好まれることを実証。 | **L1** LSP One-Liner規範（Language + Software technology + Purpose による機能事実の定義） |
| **`[REF-GAUGHAN2025]`**| GitHub/OSS実証 | Gaughan et al. (2025) | 初版README中央値160語。煩雑な誓約（CLA等）は新規参入者を激減させる。 | **L1/L2** 初動の認知的摩擦・不安喚起の排除規約 |
| **`[REF-FRONCH2023]`** | GitHub/OSS実証 | Fronchetti et al. (2023) | 65%にCONTRIBUTING欠落、新人の主要障壁（タスク選定・環境構築）の75%以上が放置。 | **L2/L3** オンボーディング導線、ローカルテスト再現手順の明示 |
| **`[REF-FOUNDJEM]`**   | GitHub/OSS実証 | Foundjem et al. (ICSE) | オンボーディング充実によるバグ14%減少、PR受容率13.5%向上、定着率35%延長。 | **L1〜L5** ドキュメント品質投資によるプロジェクト保守性向上 |
| **`[REF-DANTAS2023]`** | GitHub/OSS実証 | Dantas et al. (2023) | PR可読性改善370件分析。開発者の83.8%が可読性を重視、直感性・モジュール化・冗長性排除。 | **L4** サンプルコードの直感的命名と冗長性排除 |
| **`[REF-ALLEN1991]`** | 説得工学 | Allen (1991) | メタ分析（$N=7,547$）。反論なし両面提示 $r=-.060$ vs 反論あり $r=.076$。 | **L3** 反論あり両面提示（3連タプル構文）の義務化 |
| **`[REF-OKEFE1999]`**  | 説得工学 | O'Keefe (1999) | メタ分析（$N=20,111$）。非広告文書において反論なき弱点開示は説得力を破壊（$r=-.069$）。 | **L3** トレードオフ・解消ロジック併記の必須化 |
| **`[REF-KAMINS1989]`** | シグナリング | Kamins et al. (1989) | 開示実験（$t=3.27, p<.005$）。「中程度の重要度」の弱点開示のみ信頼性最大化。 | **L3** 開示制約の3水準分類（致命的欠陥/中程度/些細） |
| **`[REF-PARAM2026]`**  | 信頼性・シグナリング | Paramitha et al. (2026) | 252検索ソース＋870 Redditスレッドの大規模レビュー。スター数・DL数等の安価な信頼シグナル（Cheap Signals）の崩壊とレモン市場化を実証。 | **L3/L5** 安価な自称主張・誇張の排除、再現可能な決定論的検証（Costly Signals）の義務化 |
| **`[REF-ASA2026]`**    | 信頼性・シグナリング | Asa & Nautwima (2026) | コスト高シグナル（Costly signals）による分離均衡。第三者検証と透明性が信頼を形成。 | **L3/L5** 模倣困難な生テスト・独立検証環境の提示 |
| **`[REF-TSOY2012]`**   | 信頼性・シグナリング | Tsoy & Staples (Queen's) | OSS参加における第三者評価と客観的実績（$p < .001$）の信頼形成効果。 | **L3** 客観的実績・外部検証キューの明示 |
| **`[REF-RUBIN2023]`**  | 論証モデル | Eran Rubin & Benbasat (2023) | 3実験研究。Toulminモデルの各要素（Data, Warrant, Backing, Rebuttal）の結合が能力・誠実性・善意の知覚を有意に向上させる。 | **L3/L4** 論証結合構文（Claim-Data-Warrant-Backing-Rebuttal） |
| **`[REF-REED2005]`**   | 論証モデル | Chris Reed & Glenn Rowe (2005) | トゥールミンモデルと Pollock の Undercutter（論拠切断）の形式化。 | **L4** 論拠（Warrant）への反論に対する事前防御 |
| **`[REF-NABWIRE2026A]`**| 説得工学 | Sharon Nabwire et al. (2026a) | PSDにおける透明性と控えめさ（低侵襲性）が継続利用意図を高める。 | **L3** 控えめな情報提示とダークパターンの排除 |
| **`[REF-NABWIRE2026B]`**| 説得工学 | Sharon Nabwire et al. (2026b) | 透明性支援が知覚有効性と信頼性を高める因果関係の実証。 | **L3** プロセス透明性・根拠開示の義務化 |
| **`[REF-RAHMAN2024]`** | 説得工学 | Parinda Rahman & Ifeoma Adaji (2024)| 倫理的・高信頼な説得技術の設計要件。欺瞞の排除と選択の自由保障。 | **L3** オプトアウト・選択自律性の確保 |
| **`[REF-RAHMAN2025]`** | 説得工学 | Rahman (2025) | PLS-SEM分析。ユーザーの信頼には透明性（Transparency）と自律性（Autonomy）が決定的な影響を及ぼし、欺瞞的ダークパターンは信頼を破壊する。 | **L3** 深層の透明性とオプトアウト手順の義務化 |
| **`[REF-BENNER2022]`** | 説得工学 | Dennis Benner et al. (2022) | 倫理的PSD命題（P1: 意図開示, P3: 自律性と自由の確保）。 | **L3** 意図開示とユーザー自律性の保障 |
| **`[REF-CEMILOGLU2021]`**| 説得工学 | Deniz Cemiloglu & Raian Ali (2021)| 説明可能な説得（Explainable Persuasion）とインフォームド・コンセント。 | **L3** 行動喚起における理由説明義務化 |
| **`[REF-AMGOUD2009]`** | 論証モデル | Leila Amgoud (2009) / Rahwan | 意思決定のための論証理論。賛成・反対理由の評価と受容性セマンティクス。 | **L4** トレードオフ評価と工学的正当化ステップ |
| **`[REF-MURALI2025]`** | 段階的開示 | Muralidhar et al. (2025) | 臨床AI診断システムにおける選択的透明性実験。オンデマンドな段階的開示（Progressive Disclosure）が情報過負荷を防ぎ、推論理解を促進する。 | **L2** 3層アーキテクチャ（Tier 1〜3）、オンデマンドな情報開示 |
| **`[REF-SPRING2020]`** | 段階的開示 | Springer & Whittaker (2020) | 4つの実証実験。透明性の逆説（細かな誤りの即時開示が初期不信を招く現象）。初期はシンプルなヒューリスティックを提示し、詳細はオンデマンドで開示する。 | **L2** 深層詳細・全フラグ一覧のオンデマンド隔離 |
| **`[REF-ANIK2026]`**   | 段階的開示・情報設計 | Anik & Bunt (2026) | 32名被験者実験。ユーザーは認知負荷が高くても詳細で完全な情報（Information Depth）を強く好む。段階的開示が学習の知覚を有意に向上させる。 | **L2** 情報を削らず深さを保った上での階層的段階開示（SoC × Progressive Disclosure） |
| **`[REF-NIELSEN2006]`**| 段階的開示 | Jakob Nielsen (2006) | Progressive Disclosure。初見時は基本・必須機能のみ、高度なオプションは要求に応じて開示。 | **L2** 必須手順と詳細設定の階層分離 |
| **`[REF-HORTON2006]`** | 情報設計 | Sarah Horton (2006) | Access by Design。Webの表層下の情報構造化。 | **L2** 見出しレベルの階層整合性保証 |
| **`[REF-PROCTER2001]`**| 情報設計 | Chris Procter & Judith Symonds (2001)| Webユーザビリティと情報階層。迷わないナビゲーション構造。 | **L2** 明瞭なディレクトリ・ファイルリンク導線 |
| **`[REF-MATTYAS2020]`**| 情報設計 | Dóra Mattyasovszky-Philipp et al. (2020)| 認知的情報システムにおけるモデル駆動型アーキテクチャ。 | **L2** 概念モデルとドキュメント構造の整合 |
| **`[REF-STOREY1997]`** | 認知設計 | Margaret-Anne Storey et al. (1997) | ソフトウェア探索におけるメンタルモデル構築支援要素。 | **L2** トップダウン/ボトムアップ両面探索の支援 |
| **`[REF-COWAN2001]`**  | 認知負荷 | Cowan (2001) | 未知情報に対する純粋な作業記憶容量（注意の焦点）は $4 \pm 1$（中央値4）。 | **L2** 単一見出し直下の並列項目数上限（$\le 4$ 個） |
| **`[REF-DURAN2022]`**  | 認知負荷 | Rodrigo Duran et al. (2022) | 計算機科学教育における認知負荷理論の適用。スキーマ構築支援。 | **L2** 初見者の外在性認知負荷の極小化 |
| **`[REF-SWEL2011]`**   | 認知負荷 | Sweller et al. (2011) / Kalyuga (2011)| 相互依存情報の空間的分離による注意分割効果（Split-Attention）と外在性認知負荷（ECL）の急増。 | **L2** 空間的一体化（コード内注釈・直近対比表） |
| **`[REF-SU2012]`**     | 情報設計 | Su, Tempero, Hosking, Grundy (2012) | アーキテクチャ文書における情報採餌（Information Foraging）行動調査。読者は目次や構造的手がかりを起点に探索する。 | **L2** 構造的目次（TOC）基準（H2見出し4個以上で必須） |
| **`[REF-PAECH2016]`**  | ドキュメント可読性 | Barbara Paech et al. (2016) | メソッドチェーンとコメントが可読性・理解度に与える影響の実験。 | **L4** コード例のコメントによる意図開示 |
| **`[REF-KALYUGA2011]`**| 認知負荷 | Slava Kalyuga (2011) | 専門性の逆転効果（Expertise Reversal Effect）。初心者向け説明と熟達者向け情報。 | **L2** 初心者向けと熟達者向けの分離・階層化 |
| **`[REF-JACQUETTE2008]`**| 論理学 | Dale Jacquette (2008) | 背理法（Reductio ad Absurdum）の演繹的構造と責任帰属。 | **L4** 背理法によるツッコミどころ排除と前提責任明示 |
| **`[REF-JANSEN2007]`** | 論理学 | Henrike Jansen (2007) | 背理法（論理矛盾）と結果論証（因果的悪影響）の峻別。 | **L4** 背理法とトレードオフの峻別（絶対的不可能偽装の排除） |
| **`[REF-RUSHBY2009]`** | 形式検証 | John Rushby (2009) | Assurance Case 3層分離（Claims + Arguments + Evidence）と全称命題の限定（Caveats）。 | **L4/L5** 主張・論証・証拠の3層構文と制約条件明記 |
| **`[REF-PRAWITZ2018]`**| 証明論 | Dag Prawitz (2018) | 推論の妥当性と証明の認識論的力（Epistemic Power）。 | **L4** 前提から結論への妥当な導出ステップの担保 |
| **`[REF-VONPLATO2020]`**| 証明論 | Jan von Plato (SEP 2020) | ゲンツェンの自然演繹、迂回（hillock/detours）の除去と正規形（Normal Form）。 | **L4** 無駄な前置きや自明な消費の除去（正規形の維持） |
| **`[REF-BAIER2024]`**  | 形式検証 | Daniel Baier et al. (CPAchecker, 2024)| 証拠生成（Witness Validation）と反例（Counterexample）可視化。 | **L5** 実行可能な検証Witness（コマンド・テスト）添付 |
| **`[REF-KNIGHT2010]`** | 形式検証 | Xiang Yin & John Knight (NASA NFM 2010)| 構造的一致仮説（Structural Correspondence）と部分証明。 | **L4/L5** 設計とドキュメントの構造的1対1一致 |
| **`[REF-SIEG1998]`**   | 証明論 | Wilfried Sieg & John Byrnes | 自然演繹における戦略的証明探索（Intercalation Calculus）。 | **L4** 目標主導型の論理展開 |
| **`[REF-NIELSEN2018]`**| CVR・視線誘導 | Jakob Nielsen (2018) | NNGroupアイトラッキング（13万点固着解析）。閲覧時間の57%がAbove the Fold、74%が上位2画面に集中。 | **L1** ファーストビュー集中設計（50行以内の密度最大化）、**L2** 視覚動線制御 |
| **`[REF-MULLIN2023]`** | CVR・視線誘導 | Shanelle Mullin (2023) | Google視認性データ73% vs 44%、NNGroup平均格差84%。False Floor（騙しの床）による離脱。 | **L2** 視覚的連続性（Foldをまたぐ目次・見出しの覗かせ、孤立境界線禁止） |
| **`[REF-SHAPIRO2020]`**| 離脱防止・LP | Julian Shapiro (2020) | Adoption Rate = Desire × Friction / Effort。5秒テスト（What/Why/Howの即答性）。 | **L1** 5秒テスト適合性監査、専門用語・探索労力の極小化 |
| **`[REF-DRY2020]`**    | コピー・表現 | Harry Dry (2020) | Jargon（抽象的メタファー）の排除と具体的動作・入出力事実への正規化。 | **L1/L4** 抽象的形容詞の排除、平易な字義通り名詞・動詞規範 |
| **`[REF-UNBOUNCE2022]`**| CVR・離脱防止 | Unbounce (2022) | 競合するマルチCTAによる決定麻痺（Decision Paralysis）の解明。 | **L1** 単一推奨Quick Start（Primary CTA）の明示、代替手法の段階的隔離 |
| **`[REF-USERPILOT2026]`**| コピー・便益工学 | Userpilot (2026) | FABモデル。Feature（機能） $\rightarrow$ Advantage（動作機序） $\rightarrow$ Benefit（読者利得）の3段結合。 | **L2** 機能リストにおけるFAB 3要素因果結合の義務化 |
| **`[REF-KANDA2016]`**  | コピー・課題解決 | 神田昌典 (2016) | 新PASONAの法則。煽り（Agitation）を親近感・技術文脈理解（Affinity）へ昇華。 | **L1/L3** 不安煽りの完全禁止、読者の開発文脈への共感と根本原因提示 |
| **`[REF-SALESCOPY2026]`**| コピー・構成 | The Sales Copy (2026) | 4Pの法則（Picture, Promise, Proof, Push）。 | **L1/L3/L5** 展望・約束・客観的証拠・行動喚起の一貫結合 |
| **`[REF-COPYHACKERS2015]`**| コピー・型 | Joanna Wiebe (2015) | Every Copywriting Formula Ever。構造化されたメッセージフレームワーク。 | **L1/L2** 目的に応じたドキュメント構成テンプレートの適用 |
| **`[REF-HUME1739]`**   | 形式論理・哲学 | David Hume (1739) | 事実命題（is）から客観的導出なしに規範命題（ought）を導く論理的誤謬。 | **L4/L5** ヒュームのギロチン（客観的条件付き因果文への正規化） |
| **`[REF-PENG2011]`**   | 実証再現性 | Roger D. Peng (2011) | 再現可能な研究の自己完結性、および決定論的テストオラクル。 | **L5** 単体実行可能コマンド、決定論的期待出力の明記 |
| **`[REF-NAAM]`**       | 思考基盤 | Yuzuko Underson (NaaM) | Numbers are a Mirage（文脈なき単独数値は幻影）。4要素因果文脈の結合。 | **L5** NaaM 4要素ベンチマークタプル（環境・データ・比較・分散） |

---

## 2. 書誌情報詳細 (Bibliographic References)

### 2.1 GitHub README & OSS 実証研究
1. **`[REF-PRANA2019]`**: Gede Artha Azriadi Prana, Christoph Treude, Ferdian Thung, Thushari Atapattu, David Lo. "Categorizing the Content of GitHub README Files". *Empirical Software Engineering*, Vol. 24, pp. 1296–1327 (2019). DOI: [10.1007/s10664-018-9660-3](https://doi.org/10.1007/s10664-018-9660-3) / arXiv: [1802.06997](https://arxiv.org/abs/1802.06997).
2. **`[REF-SITTHI2023]`**: Supavas Sitthithanasakul, Bodin Chinthanet, Raula Gaikovina Kula, Natthakit Netsiwarawichian, Pattara Leelaprute, Bundit Manaskasemsak, Arnon Rungsawang, Kenichi Matsumoto. "Do Developers Present Proficient Code Snippets in Their README Files? An Analysis of PyPI Libraries in GitHub". *Journal of Information Processing*, Vol. 31, pp. 679–688 (2023). DOI: [10.2197/ipsjjip.31.679](https://doi.org/10.2197/ipsjjip.31.679).
3. **`[REF-ABDUL2024]`**: Ashraf Abdulmunim Abdulmajeed. "A Software Engineering Perspective on Documentation Quality: Predicting Newcomer Attraction in Open-Source Projects". *Statistics, Optimization and Information Computing*, Vol. x, pp. 1–24 (2026).
4. **`[REF-HELLMAN2023]`**: Jazlyn Hellman, Eunbee Jang, Christoph Treude, Chenzhun Huang, Jin L.C. Guo. "Describing GitHub Repositories". *SSRN Electronic Journal* (2023). SSRN: [4543196](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4543196).
5. **`[REF-GAUGHAN2025]`**: Matthew Gaughan, Kaylea Champion, Sohyeon Hwang, Aaron Shaw. "The Introduction of README and CONTRIBUTING Files in Open Source Software Development". arXiv: [2502.18440](https://arxiv.org/abs/2502.18440) (2025).
6. **`[REF-FRONCH2023]`**: Felipe Fronchetti, David C. Shepherd, Igor Wiese, Christoph Treude, Marco Aurélio Gerosa, Igor Steinmacher. "Do CONTRIBUTING Files Provide Information about OSS Newcomers’ Onboarding Barriers?". *ESEC/FSE 2023*, pp. 1–13 (2023). DOI: [10.1145/3611643.3616288](https://doi.org/10.1145/3611643.3616288).
7. **`[REF-FOUNDJEM]`**: Armstrong Foundjem, Ellis E. Eghan, Bram Adams. "Onboarding vs. Diversity, Productivity, and Quality – Empirical Study of the OpenStack Ecosystem". *3611643.3616288*.
8. **`[REF-DANTAS2023]`**: Carlos Eduardo C. Dantas et al. "How do Developers Improve Code Readability? An Empirical Study of Pull Requests". arXiv: [2309.02594](https://arxiv.org/abs/2309.02594) (2023).

### 2.2 信頼性・シグナリング & 説得工学
9. **`[REF-ALLEN1991]`**: Mike Allen. "Meta-Analysis Comparing the Persuasiveness of One-Sided and Two-Sided Messages". *Western Journal of Speech Communication*, Vol. 55, No. 4, pp. 390–404 (1991). DOI: [10.1080/10570319109374395](https://doi.org/10.1080/10570319109374395).
10. **`[REF-OKEFE1999]`**: Daniel J. O'Keefe. "How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages". *Annals of the International Communication Association*, Vol. 22, No. 1, pp. 209–249 (1999). DOI: [10.1080/23808985.1999.11678963](https://doi.org/10.1080/23808985.1999.11678963).
11. **`[REF-KAMINS1989]`**: Michael A. Kamins, Meribeth J. Brand, Stuart A. Hoeke, John C. Moe. "Two-Sided Versus One-Sided Celebrity Endorsements: The Impact on Advertising Effectiveness and Credibility". *Journal of Advertising*, Vol. 18, No. 2, pp. 4–10 (1989). DOI: [10.1080/00913367.1989.10673146](https://doi.org/10.1080/00913367.1989.10673146).
12. **`[REF-PARAM2026]`**: Ranindya Paramitha, Christian Kästner, Laurie Williams. "A Lemon Market in Open-Source Software? A Call to Action for Software Supply Chain Research". arXiv: [2608.20678](https://arxiv.org/abs/2608.20678) (2026).
13. **`[REF-ASA2026]`**: Asa Romeo Asa, Johanna Pangeiko Nautwima. "Corporate digital responsibility and consumer trust: a signaling theory perspective". *Cogent Business & Management*, Vol. 13, No. 1, 2607753 (2026). DOI: [10.1080/23311975.2025.2607753](https://doi.org/10.1080/23311975.2025.2607753).
14. **`[REF-TSOY2012]`**: Mikhail Tsoy, D. Sandy Staples. "Role of reputation cues in trust formation for a developer's decision to join Open Source Software projects". *Proceedings of the International Conference on Information Systems (ICIS)* (Queen's University).
15. **`[REF-RUBIN2023]`**: Eran Rubin, Izak Benbasat. "Explaining Explainable Systems: A Toulmin-Based Model and Evaluation of Trustworthiness". *ACM Transactions on Management Information Systems*, Vol. 14, No. 4, Article 35 (2023). DOI: [10.1145/3580479](https://doi.org/10.1145/3580479).
16. **`[REF-REED2005]`**: Chris Reed, Glenn Rowe. "Translating Toulmin, Diagramming Argument & Pollock's Undercutter". *Argumentation*, Vol. 19, pp. 267–286 (2005).
17. **`[REF-NABWIRE2026A]`**: Sharon Nabwire, Eunice Agyei et al. "Evaluating the Influence of Persuasive Systems Design on Continuance Intention and Perceived Effectiveness". (2026).
18. **`[REF-NABWIRE2026B]`**: Sharon Nabwire, Renata Savian Colvero de Oliveira et al. "Enhancing the perceived effectiveness of health behaviour change support systems through transparency in persuasive systems design". (2026).
19. **`[REF-RAHMAN2024]`**: Parinda Rahman, Ifeoma Adaji. "Designing Ethical Persuasive Technologies: Requirements and Framework". *ACM Conversational User Interfaces* (2024). DOI: [10.1145/3701571.3703385](https://doi.org/10.1145/3701571.3703385).
20. **`[REF-RAHMAN2025]`**: Parinda Rahman. "Ethics and Trust in Persuasive Technology Design". Ph.D. Thesis, University of British Columbia (2025).
21. **`[REF-BENNER2022]`**: Dennis Benner, Sofia Marlena Schöbel, Andreas Janson, Jan Marco Leimeister. "How to Achieve Ethical Persuasive Design: A Review and Theoretical Propositions for Information Systems". *AIS Transactions on Human-Computer Interaction*, Vol. 14, No. 4, pp. 548–577 (2022). DOI: [10.17705/1thci.00179](https://doi.org/10.17705/1thci.00179).
22. **`[REF-CEMILOGLU2021]`**: Deniz Cemiloglu, Raian Ali. "Explainable Persuasion in Interactive Design". *IEEE International Conference on Systems, Man, and Cybernetics (SMC)* (2021).
23. **`[REF-AMGOUD2009]`**: Leila Amgoud. "Argumentation for Decision Making". In: Iyad Rahwan, Guillermo R. Simari (Eds.), *Argumentation in Artificial Intelligence*, Chapter 15, pp. 301–320, Springer-Verlag Berlin Heidelberg (2009). DOI: [10.1007/978-0-387-98197-0_15](https://doi.org/10.1007/978-0-387-98197-0_15).

### 2.3 段階的開示・情報設計 & 認知負荷
24. **`[REF-MURALI2025]`**: Deepa Muralidhar et al. "Operationalizing Selective Transparency in Clinical AI". (2025).
25. **`[REF-SPRING2020]`**: Aaron Springer, Steve Whittaker. "Progressive Disclosure and the Transparency Paradox in AI-Assisted Decision Making". *ACM Transactions on Computer-Human Interaction*, Vol. 27, No. 4, pp. 1–32 (2020). DOI: [10.1145/3374218](https://doi.org/10.1145/3374218).
26. **`[REF-ANIK2026]`**: Ariful Islam Anik, Andrea Bunt. "Information Depth and Progressive Disclosure in Explainable Interfaces". *ACM Transactions on Interactive Intelligent Systems* (2026). DOI: [10.1145/3742413.3789087](https://doi.org/10.1145/3742413.3789087).
27. **`[REF-NIELSEN2006]`**: Jakob Nielsen. "Progressive Disclosure". *Nielsen Norman Group Articles* (2006).
28. **`[REF-HORTON2006]`**: Sarah Horton. *Access by Design: A Guide to Universal Usability for Web Designers*. New Riders (2006). DOI: [10.1145/1133219.1133221](https://doi.org/10.1145/1133219.1133221).
29. **`[REF-PROCTER2001]`**: Chris Procter, Judith Symonds. "Designing for web site usability". (2001).
30. **`[REF-MATTYAS2020]`**: Dóra Mattyasovszky-Philipp, Bálint Molnár. "Architectural approach to cognitive information systems". (2020).
31. **`[REF-STOREY1997]`**: Margaret-Anne D. Storey, F. David Fracchia, Hausi A. Müller. "Cognitive Design Elements to Support the Construction of a Mental Model During Software Exploration". *Journal of Systems and Software* (1997).
32. **`[REF-COWAN2001]`**: Nelson Cowan. "The Magical Number 4 in Short-Term Memory: A Reconsideration of Mental Storage Capacity". *Behavioral and Brain Sciences*, Vol. 24, No. 1, pp. 87–185 (2001).
33. **`[REF-DURAN2022]`**: Rodrigo Duran, Albina Zavgorodniaia, Juha Sorva. "Cognitive Load Theory in Computing Education Research: A Review". *ACM Transactions on Computing Education* (2022). DOI: [10.1145/1180639.1180831](https://doi.org/10.1145/1180639.1180831).
34. **`[REF-SWEL2011]`**: John Sweller, Paul Ayres, Slava Kalyuga. *Cognitive Load Theory*. Springer New York (2011).
35. **`[REF-SU2012]`**: Moon Ting Su, Ewan Tempero, John Hosking, John Grundy. "An Eye-Tracking Study on How Developers Read Architectural Documentation". (2012).
36. **`[REF-PAECH2016]`**: Barbara Paech et al. "The Role of Method Chains and Comments in Software Readability and Comprehension: An Experiment". *IEEE Transactions on Software Engineering* (2016).
37. **`[REF-KALYUGA2011]`**: Slava Kalyuga. "Cognitive Load Theory: How to Manage Working Memory Load in Instructional Design". *Information Systems Journal* (2011).

### 2.4 論理学・形式証明
38. **`[REF-JACQUETTE2008]`**: Dale Jacquette. "Mathematical Proof and Discovery: Reductio ad Absurdum". *Informal Logic*, Vol. 28, No. 3, pp. 242–261 (2008).
39. **`[REF-JANSEN2007]`**: Henrike Jansen. "Refuting a Standpoint by Appealing to Its Outcomes: Reductio ad Absurdum vs. Argument from Consequences". *Informal Logic*, Vol. 27, No. 3, pp. 249–266 (2007).
40. **`[REF-RUSHBY2009]`**: John Rushby. "Software Verification and System Assurance". *7th IEEE International Conference on Software Engineering and Formal Methods (SEFM)*, pp. 3–10 (2009).
41. **`[REF-PRAWITZ2018]`**: Dag Prawitz. "The Fundamental Problem of General Proof Theory". *Studia Logica*, Vol. 107, pp. 11–29 (2019, Online 2018). DOI: [10.1007/s11225-018-9785-9](https://doi.org/10.1007/s11225-018-9785-9).
42. **`[REF-VONPLATO2020]`**: Jan von Plato. "The Development of Proof Theory". *Stanford Encyclopedia of Philosophy* (2008 / substantive revision 2020).
43. **`[REF-BAIER2024]`**: Daniel Baier, Dirk Beyer et al. "Software Verification with CPAchecker 3.0: Tutorial and User Guide". *Formal Methods (FM 2024)*, LNCS 14934, pp. 543–570 (2025).
44. **`[REF-KNIGHT2010]`**: Xiang Yin, John Knight. "Practical Certification: Formal Methods and the Structural Correspondence Hypothesis". *NASA Formal Methods (NFM 2010)* (20100018552).
45. **`[REF-SIEG1998]`**: Wilfried Sieg, John Byrnes. "Normal Natural Deduction Proofs (in classical logic)". *Studia Logica*.

### 2.5 CVR・離脱防止 & コピー・LPの型
46. **`[REF-NIELSEN2018]`**: Jakob Nielsen. "Scrolling and Attention: Increasing Engagement Below the Fold". *Nielsen Norman Group Research Reports* (2018).
47. **`[REF-MULLIN2023]`**: Shanelle Mullin. "Above the Fold vs. Below the Fold: How To Encourage Scrolling". *CXL Institute* (2023).
48. **`[REF-SHAPIRO2020]`**: Julian Shapiro. "Startup Handbook: Landing Page Copywriting & Conversion Optimization". (2020).
49. **`[REF-DRY2020]`**: Harry Dry. "Rewriting Landing Pages: 10 Rules for Converting Copy". *Marketing Examples* (2020).
50. **`[REF-UNBOUNCE2022]`**: Unbounce. "High-Converting Landing Pages: Anatomy, Structure & Design Guidelines". (2022).
51. **`[REF-USERPILOT2026]`**: Userpilot. "Features, Advantages & Benefits: The FAB Model for Product Onboarding". (2026).
52. **`[REF-KANDA2016]`**: 神田昌典. 『稼ぐ言葉の法則――「新・PASONAの法則」と売れる公式41』. ダイヤモンド社 (2016).
53. **`[REF-SALESCOPY2026]`**: The Sales Copy. "4Pの法則：LP、セールスレターの構成で迷ったらこれ" (2026).
54. **`[REF-COPYHACKERS2015]`**: Joanna Wiebe. "Every Copywriting Formula Ever: The Ultimate Guide to High-Converting Copy". *Copyhackers* (2015).

### 2.6 哲学的公理・実証再現性基盤
55. **`[REF-HUME1739]`**: David Hume. *A Treatise of Human Nature*. Book III, Part I, Section I (1739).
56. **`[REF-PENG2011]`**: Roger D. Peng. "Reproducible Research in Computational Science". *Science*, Vol. 334, No. 6060, pp. 1226–1227 (2011). DOI: [10.1126/science.1213847](https://doi.org/10.1126/science.1213847).
57. **`[REF-NAAM]`**: Yuzuko Underson. "NaaM (Numbers are a Mirage) 思考フレームワーク：文脈なき単独数値の排斥と4要素因果タプル". (2026).
