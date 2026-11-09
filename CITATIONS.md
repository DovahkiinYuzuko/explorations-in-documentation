# 参考文献公式目録 (CITATIONS & Traceability Matrix)

本ドキュメントは、「ドキュメント論─個人的な自由研究」およびエージェントスキル `doc-refine` の設計基盤となった全学術文献・理論モデルの公式文献目録（Bibliography）である。
各文献の書誌情報（DOI / 掲載誌）、抽出された実証データ、およびドキュメント工学フレームワーク（5層アーキテクチャ）への直接的な作用（Informed Insights & Applied Mechanisms）を記録する。

---

## 1. 導出・作用トレーサビリティマトリクス (Traceability Matrix)

| 文献ID | 領域 | 主要文献・著者 | 抽出実測データ・理論モデル | doc-refine への直接の作用 |
| :--- | :--- | :--- | :--- | :--- |
| **`[REF-PRANA2019]`** | GitHub/OSS実証 | Prana et al. (2019) | 393リポジトリ解析。Why欠落率74.3%、When欠落率78.6%。 | **L1** Why配置（目的の明示）、**L3** 制約セクション（What-Not）必須化 |
| **`[REF-SITTHI2023]`** | GitHub/OSS実証 | Sitthithanasakul et al. (2023) | PyPI 1,620件解析。スニペットの92%がBasic構文（Level A: 基本構文）。 | **L1** Quick Start Basic構文規範（Level A強制、技巧的構文排除） |
| **`[REF-ABDUL2024]`** | GitHub/OSS実証 | Abdulmajeed (2026) | 717リポジトリCatBoost/SHAP解析。README長が静的ドキュメント要因中第1位（平均SHAP 0.420）。中程度の長さでピークに達する非線形関係。 | **L1** ファーストビュー（50行以内）、**L2** 3層情報分離（過長ドキュメントの分割） |
| **`[REF-HELLMAN2023]`**| GitHub/OSS実証 | Hellman et al. (2023) | GitHub概要欄の実態調査。高品質リポジトリから創発した **LSP（Language, Software technology, Purpose）** パターンが読者に最も好まれることを実証。 | **L1** LSP One-Liner規範（Language + Software technology + Purpose による機能事実の定義） |
| **`[REF-GAUGHAN2025]`**| GitHub/OSS実証 | Gaughan et al. (2025) | 初版README中央値160語。煩雑な誓約（CLA等）は新規参入者を激減させる。 | **L1/L2** 初動の認知的摩擦・不安喚起の排除規約 |
| **`[REF-ALLEN1991]`** | 説得工学 | Allen (1991) | メタ分析（$N=7,547$）。反論なし両面提示 $r=-.060$ vs 反論あり $r=.076$。 | **L3** 反論あり両面提示（3連タプル構文）の義務化 |
| **`[REF-OKEFE1999]`**  | 説得工学 | O'Keefe (1999) | メタ分析（$N=20,111$）。非広告文書において反論なき弱点開示は説得力を破壊（$r=-.069$）。 | **L3** トレードオフ・解消ロジック併記の必須化 |
| **`[REF-KAMINS1989]`** | シグナリング | Kamins et al. (1989) | 開示実験（$t=3.27, p<.005$）。「中程度の重要度」の弱点開示のみ信頼性最大化。 | **L3** 開示制約の3水準分類（致命的欠陥/中程度/些細） |
| **`[REF-PARAM2026]`**  | 信頼性・シグナリング | Paramitha et al. (2026) | 252検索ソース＋870 Redditスレッドの大規模レビュー。スター数・DL数等の安価な信頼シグナル（Cheap Signals）の崩壊とレモン市場化を実証。 | **L3/L5** 安価な自称主張・誇張の排除、再現可能な決定論的検証（Costly Signals）の義務化 |
| **`[REF-RUBIN2023]`**  | 論証モデル | Eran Rubin & Benbasat (2023) | 3実験研究。Toulminモデルの各要素（Data, Warrant, Backing, Rebuttal）の結合が能力・誠実性・善意の知覚を有意に向上させる。 | **L3/L4** 論証結合構文（Claim-Data-Warrant-Backing-Rebuttal） |
| **`[REF-RAHMAN2025]`** | 説得工学 | Rahman (2025) | PLS-SEM分析。ユーザーの信頼には透明性（Transparency）と自律性（Autonomy）が決定的な影響を及ぼし、欺瞞的ダークパターンは信頼を破壊する。 | **L3** 深層の透明性とオプトアウト手順の義務化 |
| **`[REF-MURALI2025]`** | 段階的開示 | Muralidhar et al. (2025) | 臨床AI診断システムにおける選択的透明性実験。オンデマンドな段階的開示（Progressive Disclosure）が情報過負荷を防ぎ、推論理解を促進する。 | **L2** 3層アーキテクチャ（Tier 1〜3）、オンデマンドな情報開示 |
| **`[REF-SPRING2020]`** | 段階的開示 | Springer & Whittaker (2020) | 4つの実証実験。透明性の逆説（細かな誤りの即時開示が初期不信を招く現象）。初期はシンプルなヒューリスティックを提示し、詳細はオンデマンドで開示する。 | **L2** 深層詳細・全フラグ一覧のオンデマンド隔離 |
| **`[REF-ANIK2026]`**   | 段階的開示・情報設計 | Anik & Bunt (2026) | 32名被験者実験。ユーザーは認知負荷が高くても詳細で完全な情報（Information Depth）を強く好む。段階的開示が学習の知覚を有意に向上させる。 | **L2** 情報を削らず深さを保った上での階層的段階開示（SoC × Progressive Disclosure） |
| **`[REF-COWAN2001]`**  | 認知負荷 | Cowan (2001) | 未知情報に対する純粋な作業記憶容量（注意の焦点）は $4 \pm 1$（中央値4）。 | **L2** 単一見出し直下の並列項目数上限（$\le 4$ 個） |
| **`[REF-SWEL2011]`**   | 認知負荷 | Sweller et al. (2011) / Kalyuga (2011)| 相互依存情報の空間的分離による注意分割効果（Split-Attention）と外在性認知負荷（ECL）の急増。 | **L2** 空間的一体化（コード内注釈・直近対比表） |
| **`[REF-SU2012]`**     | 情報設計 | Su, Tempero, Hosking, Grundy (2012) | アーキテクチャ文書における情報採餌（Information Foraging）行動調査。読者は目次や構造的手がかりを起点に探索する。 | **L2** 構造的目次（TOC）基準（H2見出し4個以上で必須） |
| **`[REF-BORST2016]`**  | ドキュメント可読性 | Börstler & Paech (2016) | 字面をなぞったトートロジー説明は主観的可読性の錯覚を生むが理解度寄与ゼロ。 | **L4** 偽の可読性・トートロジー排除（前提・副作用記述） |
| **`[REF-HUME1739]`**   | 形式論理・哲学 | David Hume (1739) | 事実命題（is）から客観的導出なしに規範命題（ought）を導く論理的誤謬。 | **L4/L5** ヒュームのギロチン（客観的条件付き因果文への正規化） |
| **`[REF-JANSEN2007]`** | 論証モデル | Jansen (2007) / Jacquette (2008)| 背理法（論理矛盾による否定）と結果論証（不利益による回避）の峻別。 | **L4** 背理法とトレードオフの峻別（絶対的不可能偽装の排除） |
| **`[REF-RUSHBY2009]`** | 形式検証 | Rushby (2009) / Knight & Yin (2010)| 高信頼システムの保証論証における Claim + Argument + Evidence の3層分離。 | **L4** Assurance Case 3層分離（主張・論証・証拠） |
| **`[REF-PENG2011]`**   | 実証再現性 | Peng (2011) / Adzic (2011) | 再現可能な研究の自己完結性、および決定論的テストオラクル。 | **L5** 単体実行可能コマンド、決定論的期待出力の明記 |
| **`[REF-NAAM]`**       | 思考基盤 | Yuzuko Underson (NaaM) | Numbers are a Mirage（文脈なき単独数値は幻影）。4要素因果文脈の結合。 | **L5** NaaM 4要素ベンチマークタプル（環境・データ・比較・分散） |
| **`[REF-NIELSEN2018]`**| CVR・視線誘導 | Jakob Nielsen (2018) | NNGroupアイトラッキング（13万点固着解析）。閲覧時間の57%がAbove the Fold、74%が上位2画面に集中。 | **L1** ファーストビュー集中設計（50行以内の密度最大化）、**L2** 視覚動線制御 |
| **`[REF-MULLIN2023]`** | CVR・視線誘導 | Shanelle Mullin (2023) | Google視認性データ73% vs 44%、NNGroup平均格差84%。False Floor（騙しの床）による離脱。 | **L2** 視覚的連続性（Foldをまたぐ目次・見出しの覗かせ、孤立境界線禁止） |
| **`[REF-SHAPIRO2020]`**| 離脱防止・LP | Julian Shapiro (2020) | Adoption Rate = Utility - (Labor + Confusion)。5秒テスト（What/Why/Howの即答性）。 | **L1** 5秒テスト適合性監査、専門用語・探索労力の極小化 |
| **`[REF-DRY2020]`**    | コピー・表現 | Harry Dry (2020) | Jargon（抽象的メタファー）の排除と具体的動作・入出力事実への正規化。 | **L1/L4** 抽象的形容詞の排除、平易な字義通り名詞・動詞規範 |
| **`[REF-UNBOUNCE2022]`**| CVR・離脱防止 | Unbounce (2022) | 競合するマルチCTAによる決定麻痺（Decision Paralysis）の解明。 | **L1** 単一推奨Quick Start（Primary CTA）の明示、代替手法の段階的隔離 |
| **`[REF-USERPILOT2026]`**| コピー・便益工学 | Userpilot (2026) | FABモデル。Feature（機能） $\rightarrow$ Advantage（動作機序） $\rightarrow$ Benefit（読者利得）の3段結合。 | **L2** 機能リストにおけるFAB 3要素因果結合の義務化 |
| **`[REF-KANDA2016]`**  | コピー・課題解決 | 神田昌典 (2016) | 新PASONAの法則。煽り（Agitation）を親近感・技術文脈理解（Affinity）へ昇華、CVR 2.8倍。 | **L1/L3** 不安煽りの完全禁止、読者の開発文脈への共感と根本原因提示 |
| **`[REF-FRONCH2023]`** | GitHub/OSS実証 | Fronchetti et al. (2023) | 65%にCONTRIBUTING欠落、新人の主要障壁（タスク選定・環境構築）の75%以上が放置。 | **L2/L3** オンボーディング導線、ローカルテスト再現手順の明示 |
| **`[REF-FOUNDJEM]`**   | GitHub/OSS実証 | Foundjem et al. (ICSE) | オンボーディング充実によるバグ14%減少、PR受容率13.5%向上、定着率35%延長。 | **L1〜L5** ドキュメント品質投資によるプロジェクト保守性向上 |
| **`[REF-DANTAS2023]`** | GitHub/OSS実証 | Dantas et al. (2023) | PR可読性改善370件分析。開発者の83.8%が可読性を重視、直感性・モジュール化・冗長性排除。 | **L4** サンプルコードの直感的命名と冗長性排除 |

---

## 2. 書誌情報詳細 (Bibliographic References)

### 2.1 GitHub README & OSS 実証研究
1. **`[REF-PRANA2019]`**: Gede Artha Azriadi Prana, Christoph Treude, Ferdian Thung, Thushari Atapattu, David Lo. "Categorizing the Content of GitHub README Files". *Empirical Software Engineering*, Vol. 24, pp. 1296–1327 (2019). DOI: [10.1007/s10664-018-9660-3](https://doi.org/10.1007/s10664-018-9660-3) / arXiv: [1802.06997](https://arxiv.org/abs/1802.06997).
2. **`[REF-SITTHI2023]`**: Supavas Sitthithanasakul, Bodin Chinthanet, Raula Gaikovina Kula, Natthakit Netsiwarawichian, Pattara Leelaprute, Bundit Manaskasemsak, Arnon Rungsawang, Kenichi Matsumoto. "Do Developers Present Proficient Code Snippets in Their README Files? An Analysis of PyPI Libraries in GitHub". *Journal of Information Processing*, Vol. 31, pp. 679–688 (2023). DOI: [10.2197/ipsjjip.31.679](https://doi.org/10.2197/ipsjjip.31.679).
3. **`[REF-ABDUL2024]`**: Ashraf Abdulmunim Abdulmajeed. "A Software Engineering Perspective on Documentation Quality: Predicting Newcomer Attraction in Open-Source Projects". *Statistics, Optimization and Information Computing*, Vol. x, pp. 1–24 (2026).
4. **`[REF-HELLMAN2023]`**: Jazlyn Hellman, Eunbee Jang, Christoph Treude, Chenzhun Huang, Jin L.C. Guo. "Describing GitHub Repositories". *SSRN Electronic Journal* (2023). SSRN: [4543196](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4543196).
5. **`[REF-GAUGHAN2025]`**: Matthew Gaughan, Kaylea Champion, Sohyeon Hwang, Aaron Shaw. "The Introduction of README and CONTRIBUTING Files in Open Source Software Development". arXiv: [2502.18440](https://arxiv.org/abs/2502.18440) (2025).
6. **`[REF-FRONCH2023]`**: Felipe Fronchetti, David C. Shepherd, Igor Wiese, Christoph Treude, Marco Aurélio Gerosa, Igor Steinmacher. "Do CONTRIBUTING Files Provide Information about OSS Newcomers’ Onboarding Barriers?". *ESEC/FSE 2023*, pp. 1–13 (2023). DOI: [10.1145/3611643.3616288](https://doi.org/10.1145/3611643.3616288).
7. **`[REF-FOUNDJEM]`**: Armstrong Foundjem, Ellis E. Eghan, Bram Adams. "Onboarding vs. Diversity, Productivity, and Quality – Empirical Study of the OpenStack Ecosystem". *ICSE*.
8. **`[REF-DANTAS2023]`**: Carlos Eduardo C. Dantas et al. "How do Developers Improve Code Readability? An Empirical Study of Pull Requests". arXiv: [2309.02594](https://arxiv.org/abs/2309.02594) (2023).

### 2.2 信頼性・シグナリング & 説得工学
6. **`[REF-ALLEN1991]`**: Mike Allen. "Meta-Analysis Comparing the Persuasiveness of One-sided and Two-sided Messages". *Western Journal of Speech Communication*, Vol. 55, No. 4, pp. 390–404 (1991). DOI: [10.1080/10570319109374395](https://doi.org/10.1080/10570319109374395).
7. **`[REF-OKEFE1999]`**: Daniel J. O'Keefe. "How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages". *Annals of the International Communication Association*, Vol. 22, No. 1, pp. 209–249 (1999). DOI: [10.1080/23808985.1999.11678963](https://doi.org/10.1080/23808985.1999.11678963).
8. **`[REF-KAMINS1989]`**: Michael A. Kamins, Meribeth J. Brand, Stuart A. Hoeke, John C. Moe. "Two-Sided Versus One-Sided Celebrity Endorsements: The Impact on Advertising Effectiveness and Credibility". *Journal of Advertising*, Vol. 18, No. 2, pp. 4–10 (1989). DOI: [10.1080/00913367.1989.10673146](https://doi.org/10.1080/00913367.1989.10673146).
9. **`[REF-PARAM2026]`**: Ranindya Paramitha, Christian Kästner, Laurie Williams. "The Software Supply Chain as a Market for Lemons: A Multivocal Review of Trust Signal Collapse". arXiv: [2608.20678](https://arxiv.org/abs/2608.20678) (2026). DOI: [10.48550/arXiv.2608.20678](https://doi.org/10.48550/arXiv.2608.20678).
10. **`[REF-RUBIN2023]`**: Eran Rubin, Izak Benbasat. "Using Toulmin’s Argumentation Model to Enhance Trust in Analytics-Based Advice Giving Systems". *ACM Transactions on Management Information Systems (TMIS)*, Vol. 14, No. 3, Article 22, pp. 1–28 (2023). DOI: [10.1145/3580479](https://doi.org/10.1145/3580479).
11. **`[REF-RAHMAN2025]`**: Parinda Rahman. "Exploring Ethics and Trust in Persuasive Technologies". Master's Thesis, University of British Columbia (2025).

### 2.3 段階的開示・認知負荷・情報設計
12. **`[REF-MURALI2025]`**: Deepa Muralidhar, Rafik Belloum, Ashwin Ashok. "Operationalizing Selective Transparency using Progressive Disclosure in Artificial Intelligence Clinical Diagnosis Systems". Preprint: HAL [hal-05331557v2](https://hal.science/hal-05331557v2) (2025).
13. **`[REF-SPRING2020]`**: Aaron Springer, Steve Whittaker. "Progressive Disclosure: When, Why, and How Do Users Want Algorithmic Transparency Information?". *ACM Transactions on Interactive Intelligent Systems (TiiS)*, Vol. 10, No. 4, Article 29, pp. 1–32 (2020). DOI: [10.1145/3374218](https://doi.org/10.1145/3374218).
14. **`[REF-ANIK2026]`**: Ariful Islam Anik, Andrea Bunt. "Designing Effective Training Dataset Explanations: The Impact of Information Depth and Progressive Disclosure". *31st International Conference on Intelligent User Interfaces (IUI '26)*, pp. 1–16 (2026). DOI: [10.1145/3742413.3789087](https://doi.org/10.1145/3742413.3789087).
15. **`[REF-COWAN2001]`**: Nelson Cowan. "The magical number 4 in short-term memory: A reconsideration of mental storage capacity". *Behavioral and Brain Sciences*, Vol. 24, No. 1, pp. 87–114 (2001). DOI: [10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922).
16. **`[REF-SWEL2011]`**: John Sweller, Paul Ayres, Slava Kalyuga. *Cognitive Load Theory*. Springer New York (2011). DOI: [10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4).
17. **`[REF-SU2012]`**: Moon Ting Su, Ewan Tempero, John Hosking, John Grundy. "A Study of Architectural Information Foraging in Software Architecture Documents". *IEEE/IFIP WICSA/ECSA 2012*, pp. 141–150 (2012). DOI: [10.1109/WICSA-ECSA.212.22](https://doi.org/10.1109/WICSA-ECSA.212.22).
18. **`[REF-BORST2016]`**: Jürgen Börstler, Barbara Paech. "The Role of Method Chains and Comments in Software Readability and Comprehension—An Experiment". *IEEE Transactions on Software Engineering*, Vol. 42, No. 9, pp. 886–898 (2016). DOI: [10.1109/TSE.2016.2527791](https://doi.org/10.1109/TSE.2016.2527791).

### 2.4 論理学・形式検証・実証再現性
19. **`[REF-HUME1739]`**: David Hume. *A Treatise of Human Nature*. John Noon, London (1739). Book III, Part I, Section I ("Moral Distinctions not deriv'd from Reason").
20. **`[REF-JANSEN2007]`**: Henrike Jansen. "Refuting a Standpoint by Appealing to Its Outcomes: Reductio ad Absurdum vs. Argument from Consequences". *Informal Logic*, Vol. 27, No. 3, pp. 249–266 (2007).
21. **`[REF-RUSHBY2009]`**: John Rushby. "Software Verification and System Assurance". *7th IEEE International Conference on Software Engineering and Formal Methods (SEFM)*, pp. 3–10 (2009).
22. **`[REF-PENG2011]`**: Roger D. Peng. "Reproducible Research in Computational Science". *Science*, Vol. 334, No. 6060, pp. 1226–1227 (2011). DOI: [10.1126/science.1213847](https://doi.org/10.1126/science.1213847).
23. **`[REF-NAAM]`**: Yuzuko Underson. "Numbers are a Mirage (NaaM) Framework: 7-Layer Causal Audit for Technical Metrics". Personal Research Archive (2026).

### 2.5 視線誘導・CVR・離脱防止工学
24. **`[REF-NIELSEN2018]`**: Jakob Nielsen. "Scrolling and Attention". *Nielsen Norman Group (NNGroup)* (2018). URL: https://www.nngroup.com/articles/scrolling-and-attention/
25. **`[REF-MULLIN2023]`**: Shanelle Mullin. "Mastering above the fold: how to encourage scrolling (and converting)". *CXL* (2023).
26. **`[REF-SHAPIRO2020]`**: Julian Shapiro. *Startup Handbook: Landing Page Copywriting* / *My step-by-step guide to landing pages that convert* (2020).
27. **`[REF-DRY2020]`**: Harry Dry. "Rewriting landing pages with a pro copywriter". *Copywriting Examples* (2020).
28. **`[REF-UNBOUNCE2022]`**: Unbounce. "How to Build a High-Converting Landing Page: Anatomy, Structure & Design" (2022).

### 2.6 コピーライティング・便益工学・課題解決構成
29. **`[REF-USERPILOT2026]`**: Userpilot. "Features, Advantages & Benefits: FAB Model + Examples" (2026). URL: https://userpilot.com/blog/features-advantages-benefits/
30. **`[REF-KANDA2016]`**: 神田昌典. 『稼ぐ言葉の法則――「新・PASONAの法則」と売れる公式41』. ダイヤモンド社 (2016).
31. **`[REF-SALESCOPY2026]`**: The Sales Copy. "4Pの法則：LP、セールスレターの構成で迷ったらこれ" (2026). URL: https://thesalescopy.com/4p/
32. **`[REF-WIEBE2015]`**: Joanna Wiebe. "Every Copywriting Formula Ever (or The Ultimate Guide to No-Pain Copywriting)". *Copyhackers* (2015).
33. **`[REF-FARN2014]`**: Demian Farnworth. "Master This Copywriting Formula to Dominate Any Social Media Platform". *Copyblogger* (2014).
