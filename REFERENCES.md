# 参考文献公式目録 (REFERENCES & Traceability Matrix)

本ドキュメントは、「ドキュメント論─個人的な自由研究」の全体統括ドキュメント **[`PAPER.md`](./PAPER.md)** およびエージェントスキル `doc-refine` の設計基盤となった学術文献・理論モデル・一次資料の文献目録（Bibliography / References）です。

多角的な学際カテゴリにわたる外部先行研究および基盤公理の書誌情報（DOI / 掲載誌 / 著者）、抽出された実測データ・理論モデル、および **[`PAPER.md`](./PAPER.md)** の各章・仮説モデルへの対応関係を記録しています。

---

## 1. 導出・作用トレーサビリティマトリクス (Traceability Matrix)

| 文献ID | 領域 | 主要文献・著者 | 抽出実測データ・理論モデル | `PAPER.md`（良いドキュメント論）における対応箇所 |
| :--- | :--- | :--- | :--- | :--- |
| **`[REF-PRANA2019]`** | GitHub/OSS実証 | Prana et al. (2019) | 393リポジトリ解析。Why欠落率74.3%、When欠落率78.6%。 | **第2章/第4章** Why（目的・動機）と When（適用条件・境界）の明示 |
| **`[REF-SITTHI2023]`** | GitHub/OSS実証 | Sitthithanasakul et al. (2023) | PyPI 1,620件解析。スニペットの92%がBasic構文（Level A: 基本構文）。 | **第2章** 初動コード例における基本構文（Level A）の優位性と技巧排除 |
| **`[REF-ABDUL2026]`** | GitHub/OSS実証 | Abdulmajeed (2026) | 717リポジトリCatBoost/SHAP解析。README長が静的ドキュメント要因中第1位（平均SHAP 0.420）。中程度の長さでピークに達する非線形関係。 | **第3章** 過短・過長を避けた情報密度の最適化と段階的分離 |
| **`[REF-HELLMAN2023]`**| GitHub/OSS実証 | Hellman et al. (2023) | GitHub概要欄の実態調査。高品質リポジトリから創発した **LSP（Language, Software technology, Purpose）** パターンが読者に最も好まれることを実証。 | **第2章** 抽象語を排した具体的要素（言語・技術・目的）による冒頭定義 |
| **`[REF-GAUGHAN2025]`**| GitHub/OSS実証 | Gaughan et al. (2025) | 初版README中央値160語。煩雑な誓約（CLA等）は新規参入者を激減させる。 | **第2章** 初動の認知的摩擦・参入障壁の低減 |
| **`[REF-FRONCH2023]`** | GitHub/OSS実証 | Fronchetti et al. (2023) | 65%にCONTRIBUTING欠落、新人の主要障壁（タスク選定・環境構築）の75%以上が放置。 | **第2章/第5章** ローカル環境構築と再現テスト手順の明示 |
| **`[REF-FOUNDJEM]`**   | GitHub/OSS実証 | Foundjem et al. (ICSE) | オンボーディング充実によるバグ14%減少、PR受容率13.5%向上、定着率35%延長。 | **第2章** ドキュメント品質がプロジェクト保守性に与える実証効果 |
| **`[REF-DANTAS2023]`** | GitHub/OSS実証 | Dantas et al. (2023) | PR可読性改善370件分析。開発者の83.8%が可読性を重視、直感性・モジュール化・冗長性排除。 | **第4章** サンプルコードの直感的命名と冗長性排除 |
| **`[REF-ALLEN1991]`** | 説得工学 | Allen (1991) | メタ分析（$`N = 7,547`$）。反論なし両面提示 $`r = -.060`$ vs 反論あり $`r = .076`$（有効性約20%向上）。 | **第5章** 反論あり両面提示（制約事実＋設計理由＋回避策）の核となる実証 |
| **`[REF-OKEFE1999]`**  | 説得工学 | O'Keefe (1999) | メタ分析（$`N = 20,111`$）。非広告文書において反論なき弱点開示は説得力を破壊（$`r = -.069`$）、反論ありは有意に向上（$`r = .081`$）。 | **第5章** 単なる弱点列挙の禁止とトレードオフ・解消ロジック併記 |
| **`[REF-KAMINS1989]`** | シグナリング | Kamins et al. (1989) | 開示実験（$`t = 3.27, p < .005`$）。「中程度の重要度」の弱点開示が信頼性と利用意図を最大化。 | **第5章** コア価値を壊さない中程度のトレードオフ開示による信頼獲得 |
| **`[REF-PARAM2026]`**  | 信頼性・シグナリング | Paramitha et al. (2026) | 252検索ソース＋870 Redditスレッドの大規模レビュー。スター数・DL数等の安価な信頼シグナル（Cheap Signals）の崩壊とレモン市場化を実証。 | **第5章** 安価な自称主張（チープトーク）の排除とコスト高シグナルの必然性 |
| **`[REF-ASA2026]`**    | 信頼性・シグナリング | Asa & Nautwima (2026) | コスト高シグナル（Costly signals）による分離均衡。シグナル適合性と模倣困難な誠実性が信頼を形成。 | **第5章** 模倣困難な再現検証手順と境界開示による信頼形成 |
| **`[REF-TSOY2012]`**   | 信頼性・シグナリング | Tsoy & Staples (Queen's) | OSS参加における第三者評価と客観的実績（$`p < .001`$）の信頼形成効果。 | **第5章** 客観的実績・外部検証キューの明示 |
| **`[REF-RUBIN2023]`**  | 論証モデル | Eran Rubin & Benbasat (2023) | 3実験研究。Toulminモデルの各要素（Data, Warrant, Backing, Rebuttal）が能力・誠実さ・好意性の信頼を有意に向上させる。 | **第5章** 例外・境界条件（Rebuttal）の開示による「誠実さ（Integrity）」の獲得 |
| **`[REF-REED2005]`**   | 論証モデル | Chris Reed & Glenn Rowe (2005) | トゥールミンモデルと Pollock の Undercutter（推論の適用境界）の形式化。 | **第5章** 制約開示を「主張の否定」ではなく「成立境界の明示」として位置づける |
| **`[REF-NABWIRE2026A]`**| 説得工学 | Sharon Nabwire et al. (2026a) | PSDにおける透明性と控えめさ（低侵襲性）が知覚説得力の65.6%を説明し継続利用意図を高める。 | **第5章** 押し付けがましさを排した控えめな記述と透明性 |
| **`[REF-NABWIRE2026B]`**| 説得工学 | Sharon Nabwire et al. (2026b) | 透明性が信頼性支援の57.8%を説明し、知覚説得力の69.9%を形成する因果関係の実証。 | **第5章** 内部挙動と前提の透明性による信頼形成 |
| **`[REF-RAHMAN2024]`** | 説得工学 | Parinda Rahman & Ifeoma Adaji (2024)| 倫理的・高信頼な説得技術の設計要件。明確なメッセージとユーザー自律性のバランス。 | **第4章/第5章** 読者の選択の自由（自律性）の尊重 |
| **`[REF-RAHMAN2025]`** | 説得工学 | Rahman (2025) | 人気サイトの95%に存在するダークパターンが信頼を破壊。透明なコミュニケーションと自律性が対抗軸となる。 | **第5章** 強迫的ナッジ・誇大誘導の排除と透明な事実提示 |
| **`[REF-BENNER2022]`** | 説得工学 | Dennis Benner et al. (2022) | 倫理的PSD命題（意図の開示、自律性の保護、検証可能な証拠に基づく議論）。 | **第5章** 意図開示・自律性・検証可能エビデンスの3要件 |
| **`[REF-CEMILOGLU2021]`**| 説得工学 | Deniz Cemiloglu & Raian Ali (2021)| 説明可能な説得（Explainable Persuasion）とインフォームド・コンセント。 | **第5章** 行動を促す際の理由・メカニズムの説明責任 |
| **`[REF-AMGOUD2009]`** | 論証モデル | Leila Amgoud (2009) / Rahwan | 意思決定のための論証理論。賛成・反対理由の評価と反論に対する防御可能性。 | **第5章** メリットだけでなく反対理由（デメリット）への対処による意思決定支援 |
| **`[REF-MURALI2025]`** | 段階的開示 | Muralidhar et al. (2025) | 臨床AI診断システムにおける3層（Summary / Rationale / Exhaustive Evidence）の選択的透明性。 | **第3章** 3層情報アーキテクチャによる認知過負荷防止と監査性の両立 |
| **`[REF-SPRING2020]`** | 段階的開示 | Springer & Whittaker (2020) | 4つの実証実験。透明性の逆説（初期の過剰な詳細露出が不信を招く現象）とオンデマンド開示の優位性。 | **第3章** 初期はシンプルなメンタルモデルを提示し、詳細はオンデマンドで開示する |
| **`[REF-ANIK2026]`**   | 段階的開示・情報設計 | Anik & Bunt (2026) | 32名被験者実験。ユーザーは認知負荷が高くても詳細で完全な情報（High Information Depth）を強く好む。段階的開示が学習の知覚を有意に向上（$`p < .05`$）。 | **第3章** 情報を削らず深さを保った上での段階的開示（グルーピング × SoC） |
| **`[REF-NIELSEN2006]`**| 段階的開示 | Jakob Nielsen (2006) | Progressive Disclosure。初見時は基本・必須機能のみ、高度なオプションは要求に応じて開示。 | **第3章** 最短動線（Happy Path）と詳細リファレンスの階層分離 |
| **`[REF-HORTON2006]`** | 情報設計 | Sarah Horton (2006) | "Designing Beneath the Surface of the Web" / *Access by Design*。主要なナラティブフローと副次的詳細・構造の分離。 | **第3章** 表層リンクや付録分離による思考フローの維持 |
| **`[REF-PROCTER2001]`**| 情報設計 | Chris Procter & Judith Symonds (2001)| Webユーザビリティと情報階層。一貫した構造的手がかりによるナビゲーション破綻防止。 | **第3章** 一貫した見出し構造と階層化 |
| **`[REF-MATTYAS2020]`**| 情報設計 | Dóra Mattyasovszky-Philipp et al. (2020)| 認知的情報システムにおけるモデル駆動型アーキテクチャと視点（Viewpoint）の分離。 | **第3章** 読者の関心空間に応じた情報レイヤーの分離（SoC） |
| **`[REF-STOREY1997]`** | 認知設計 | Margaret-Anne Storey et al. (1997) | ソフトウェア探索におけるメンタルモデル構築支援（複数の抽象レベルと大域的文脈の維持）。 | **第3章** 局所的詳細を見ても迷子にならない大域ナビゲーション |
| **`[REF-COWAN2001]`**  | 認知負荷 | Cowan (2001) | 未知情報に対する純粋なワーキングメモリ容量（注意の焦点）は $`4 \pm 1`$（中央値4）。 | **第3章** フラットな並列項目の抑制と意味的グループ化（チャンキング） |
| **`[REF-DURAN2022]`**  | 認知負荷 | Rodrigo Duran et al. (2022) | 計算機科学教育における認知負荷理論（ICLとECL）の体系的レビュー、およびOviatt (2006) の構造化効果。 | **第3章** 見せ方の不手際による外在性認知負荷（ECL）の最小化 |
| **`[REF-SWEL2011]`**   | 認知負荷 | Sweller et al. (2011) / Kalyuga (2011)| 相互依存情報の空間的分離による注意分割効果（Split-Attention）と外在性認知負荷（ECL）の急増。 | **第3章** コードと注釈・コマンドと出力の空間的一体化 |
| **`[REF-SU2012]`**     | 情報設計 | Su, Tempero, Hosking, Grundy (2012) | アーキテクチャ文書における情報採餌（Information Foraging）行動調査。読者は目次や見出しを起点に跳躍探索する。 | **第3章** 情報の手がかり（Information Scent）としての構造的目次（TOC）と見出し |
| **`[REF-PAECH2016]`**  | ドキュメント可読性 | Jürgen Börstler & Barbara Paech (2016) | 104名被験者実験。「主観的な読みやすさ」と「客観的な理解度」に有意な相関がないことを実証（およびGarousi 2015の実態調査）。 | **第3章** 字面をなぞるだけのトートロジー解説の排除と、前提・副作用の記述 |
| **`[REF-KALYUGA2011]`**| 認知負荷 | Slava Kalyuga (2011) | 専門性逆転効果（Expertise Reversal Effect）。初心者向けの丁寧すぎる説明は熟達者の理解を阻害する。 | **第3章** 初心者向け導入と熟達者向け詳細を段階的開示で分離する理論的根拠 |
| **`[REF-JACQUETTE2008]`**| 論理学 | Dale Jacquette (2008) | 背理法（Reductio ad Absurdum）の演繹的構造と前提への責任帰属。 | **第4章** 代替案の矛盾を示す背理法的説明と前提条件の明示 |
| **`[REF-JANSEN2007]`** | 論理学 | Henrike Jansen (2007) | 背理法（論理的不可能性）と結果論証（因果的な望ましくない影響・トレードオフ）の厳格な峻別。 | **第4章** 単なる工学的トレードオフを「論理的破綻」と誇張する誤謬の排除 |
| **`[REF-RUSHBY2009]`** | 形式検証 | John Rushby (2009) | Assurance Case 3層分離（Claims + Arguments + Evidence）と全称命題の限定（Caveats）。 | **第5章** 主張・論証・証拠の結合と、測定環境・前提の但し書き（Caveats） |
| **`[REF-PRAWITZ2018]`**| 証明論 | Dag Prawitz (2018) | 推論の妥当性と証明の認識論的力（Epistemic Power）。 | **第4章** トートロジーではない妥当な推論ステップによる納得感の形成 |
| **`[REF-VONPLATO2020]`**| 証明論 | Jan von Plato (SEP 2020) | ゲンツェンの自然演繹、迂回（hillock/detours）の除去と正規形（Normal Form）。 | **第4章** 不要な前置き（迂回）や未定義語彙の唐突な出現の排除 |
| **`[REF-BAIER2024]`**  | 形式検証 | Daniel Baier et al. (CPAchecker, 2024)| 証拠生成（Witness Validation）と反例（Counterexample）可視化。 | **第5章** 第三者が手元で検証可能な証跡（Witness：実行コマンドとテスト）の提示 |
| **`[REF-KNIGHT2010]`** | 形式検証 | Xiang Yin & John Knight (NASA NFM 2010)| 構造的一致仮説（Structural Matching Hypothesis）と部分証明。 | **第4章** ドキュメント構造と実際のソフトウェア構造の相似性（Isomorphism） |
| **`[REF-SIEG1998]`**   | 証明論 | Wilfried Sieg & John Byrnes | 自然演繹における戦略的証明探索（Intercalation Calculus：前提と結論の間隙架橋）。 | **第4章** 読者の前提から結論へと至る段階的な論理の架橋 |
| **`[REF-NIELSEN2018]`**| CVR・視線誘導 | Jakob Nielsen (2018) | NNGroupアイトラッキング（13万点固着解析）。閲覧時間の57%がAbove the Fold、74%が上位2画面に集中。 | **第2章** 最初の画面（ファーストビュー）における情報伝達と迷いの排除 |
| **`[REF-MULLIN2023]`** | CVR・視線誘導 | Shanelle Mullin (2023) | Google視認性データ73% vs 44%、NNGroup平均格差84%。False Floor（偽の床）による離脱。 | **第2章** 視覚的終端の錯覚（False Floor）の排除とスクロール動線の維持 |
| **`[REF-SHAPIRO2020]`**| 離脱防止・LP | Julian Shapiro (2020) | Adoption Rate = Desire - (Labor + Confusion)。5秒テスト（What/Why/Howの即答性）。 | **第2章** 探索労力と混乱の極小化、冒頭5秒でのWhat/Why/Howの提示 |
| **`[REF-DRY2020]`**    | コピー・表現 | Harry Dry (2020) | Jargon（抽象的メタファー）の排除と具体的動作・入出力事実への正規化。 | **第2章** 抽象的な宣伝文句を排し、字義通りの名詞と動詞で定義する |
| **`[REF-UNBOUNCE2022]`**| CVR・離脱防止 | Unbounce (2022) | 競合するマルチCTAによる決定麻痺（Decision Paralysis）の解明。 | **第2章** 初動における単一推奨手順の提示と代替手法の段階的分離 |
| **`[REF-USERPILOT2026]`**| コピー・便益工学 | Userpilot (2026) | FABモデル。Feature（機能） $`\rightarrow`$ Advantage（動作機序） $`\rightarrow`$ Benefit（読者利得）の3段結合。 | **第4章** 機能スペックの羅列ではなく、動作の仕組みから読者の便益へつなぐ因果鎖 |
| **`[REF-KANDA2016]`**  | コピー・課題解決 | 神田昌典 (2016) | 新PASONAの法則。煽り（Agitation）を親近感・技術文脈理解（Affinity）へ昇華。 | **第4章** 不安煽りを排し、前提となる不便への共感（Affinity）から解決策を導く |
| **`[REF-SALESCOPY2026]`**| コピー・構成 | The Sales Copy (2026) | 4Pの法則（Picture, Promise, Proof, Push）と証拠の階層。 | **第5章** 主張（Promise）に対する客観的証拠（Proof）の結合 |
| **`[REF-COPYHACKERS2015]`**| コピー・型 | Joanna Wiebe (2015) | Every Copywriting Formula Ever。構造化されたメッセージフレームワーク（BAB等）。 | **第4章** 導入前の課題から導入後の状態へつなぐ論理的架け橋 |
| **`[REF-HUME1739]`**   | 形式論理・哲学 | David Hume (1739) | 事実命題（is）から客観的導出なしに規範命題（ought）を導く論理的誤謬。 | **第4章** ヒュームのギロチン（「〜すべき」という説教を排し、仕様事実と条件付き因果文で語る） |
| **`[REF-PENG2011]`**   | 実証再現性 | Roger D. Peng (2011) | 再現可能な研究の自己完結性、および決定論的テストオラクル。 | **第5章** 読者の手元で追試・再現できるコマンドとコード資産の提示 |
| **`[REF-LU2018]`**     | GitHub/絵文字実証 | Xuan Lu et al. (2018) | GitHub README における絵文字使用の主意図は Content emphasis（34.25%）と階層リスト（5.50%）。 | **第2章** 書き手が視覚的強調を狙って絵文字を導入する実態 |
| **`[REF-RONG2023]`**   | GitHub/絵文字実証 | Shiyue Rong (2023) | PR 41.87%・Issue 47.12% が Visual Enhancement 目的である一方、開発者は感情表現と主観認識。 | **第2章** 書き手の主観的認識と実リポジトリの視覚強調用途の乖離 |
| **`[REF-BORGO]`**      | 視覚探索・メタファー | Rita Borgo et al. | 視覚的メタファーは記憶保持を助け得る一方、結合探索（conjunction search）を誘発し探索速度を有意に遅延。 | **第2章/第3章** 視覚要素による記憶保持と探索速度のトレードオフ |
| **`[REF-LIU2026]`**    | 視覚探索・意味的距離 | Yunguo Liu et al. (2026) | $`N = 372`$ 実験。意味的距離が近いアイコンほど高速認識され、文化的背景との交互作用も有意。 | **第2章** アイコンの意味的距離と文化差による探索効率の変化 |
| **`[REF-LUJIE2024]`**  | 視覚探索・意味的距離 | Deng Lujie et al. (2024) | 24カ国120アイコン分析。具象的で意味的距離が近いほど効率的、抽象・恣意的記号は事前学習が必要。 | **第2章** 具象性と意味的距離が記号認識に与える影響 |
| **`[REF-SILVEN2025]`** | 視覚探索・意味的距離 | Johanna Silvennoinen et al. (2025) | ソフトウェア実装における意味的距離が認知的処理流暢性を決定し、設計不備で誤解を招く。 | **第2章** 機能アイコンの解釈流暢性と誤認識リスク |
| **`[REF-ROY2025]`** | 視覚探索・具象性 | Ankita Roy & Hiroyuki Matsuguma (2025) | 28種UIアイコン調査。ハート等は文化的合意依存であり、抽象アイコンは誤認率が高い。 | **第2章** 文化的合意なき抽象記号の誤認リスク |
| **`[REF-LI2016]`**     | 視覚メタファー | Jie Li et al. (2016) | 転移元概念の干渉属性（Interfering Attributes）が推論に逆効果（Backfire Effects）をもたらす。 | **第2章** 視覚的メタファーによる意図しない連想干渉 |
| **`[REF-SUNG2012]`**   | グラフィックス認知 | Eunmo Sung & Mayer (2012) | 200名4群実験。全画像で Liking 向上（$`d = 0.85\text{–}1.21`$）だが、想起向上は説明的画像（$`d = 0.79`$）のみ（魅惑的は $`d = -0.38`$ 低下傾向）。 | **第3章** 主観的好感度と客観的理解の乖離（Liking ≠ Learning） |
| **`[REF-DANIELSON2012]`**| 装飾グラフィックス | Robert W. Danielson (2012) | 168名実験。テキストと対応しない装飾的グラフィックスは外在的（Extraneous）であり学習を直接助けない。 | **第3章** 装飾的グラフィックスの無関連性と外在性認知負荷 |
| **`[REF-SCHNEIDER2017]`**| 装飾グラフィックス | Sascha Schneider (2017) | テキストと結合の弱い装飾画像が課題無関連な推論要求（ECL）を増大させ学習成績を低下させる。 | **第3章** 弱結合な視覚要素が引き起こす推論負荷 |
| **`[REF-HARPER2009]`** | 視覚的複雑性 | Simon Harper et al. (2009) | Webの視覚的複雑性を認知負荷の潜在的マーカーとして理論化し、読解困難時の逆行注視を整理。 | **第3章** 視覚的複雑性による走査コスト増大 |
| **`[REF-YADAV2026]`**  | UI認知負荷 | Anamika Yadav (2026) | 乱雑なデザインや紛らわしいアイコンが外在性認知負荷の直接的発生源となることをレビュー。 | **第3章** 視覚的クラッターの抑制 |
| **`[REF-SANCHEZ2006]`**| 魅惑的詳細効果 | Sanchez & Wiley (2006) | 視線計測実験。魅惑的詳細による理解低下は注意制御が弱い低WMC読者（初学者等）に集中。 | **第3章** 装飾的視覚要素が初学者・低WMC読者に与える非対称な負荷 |
| **`[REF-TIGWELL2020]`**| アクセシビリティ | Garreth W. Tigwell et al. (2020) | 視覚障害者58名＋インタビュー11名。絵文字記述子が文脈を分断しデジタルデバイドを再構築。 | **第3章** 音声・点字環境における絵文字の認知摩擦と配置配慮 |
| **`[REF-OSU2026]`**    | アクセシビリティ | Oregon State Univ. (2026) | 絵文字のALT記述子読み上げ仕様、箇条書きバレット反復問題、意図と記述子の乖離を整理。 | **第3章** スクリーンリーダー環境での反復・乖離ノイズ |
| **`[REF-KERDAR2024]`** | アクセシビリティ | Sara Hamideh Kerdar et al. (2024) | 49文献レビュー。代替テキスト欠如や標準リスト構造からの逸脱による視覚障害者への障壁を特定。 | **第3章** 標準リスト構造遵守と代替情報提供の重要性 |
| **`[REF-ZHANG2025]`**  | AIアライメント | Xuanchang Zhang et al. (2025) | RLHF選好モデルが絵文字・太字等に強いバイアスを示し、1%未満の混入で選好反転が発生。 | **第1章/第5章** 生成AIにおける視覚フォーマット・バイアスの再生産 |
| **`[REF-GLIKSON2018]`**| 社会的知覚 | Ella Glikson et al. (2018) | 3実験。フォーマル設定でスマイリーは温かさを増さず有能さ評価を低下させ情報共有を阻害。 | **第5章** フォーマル文脈における有能さ知覚の低下 |
| **`[REF-LI2019]`**     | 社会的知覚 | Xueni Li et al. (2019) | 交換規範（タスク志向）の受信者では絵文字使用により有能さ低下を介して満足度が低下。 | **第5章** 交換規範と共同体規範による受け止め方の分岐 |
| **`[REF-VAREBERG2023]`**| 社会的知覚 | Kyle R. Vareberg et al. (2023) | 368名実験（$`F = 34.59, p < .001`$）。絵文字使用により親近感は向上するが有能さ・信頼性が低下。 | **第5章** 信頼性（Credibility）と親近感のトレードオフ |
| **`[REF-VRIELINK2025]`**| 社会的知覚 | Esmee Vrielink (2025) | Email/Teams/WhatsApp追試。全チャネルで温かさは向上し、有能さ・適切性への悪影響は認められず。 | **第5章** チャネル・時代条件による受容差の両面提示 |
| **`[REF-HILLBERG2018]`**| クロスプラットフォーム | Hannah M. Hillberg et al. (2018) | 710名調査。25%超がOS間描画差異を未認識、20%が他OS表示を見て投稿を後悔・編集意図を報告。 | **第5章** 描画差異の不可視性による意図せぬ印象変化 |
| **`[REF-MILLER2017]`** | 解釈多義性 | Hannah Miller et al. (2017) | 2,482名実験。テキスト文脈を添えても絵文字の誤解ポテンシャルは単独提示とほぼ同等。 | **第5章** テキスト文脈による多義性解消の限界 |

---

## 2. 書誌情報詳細 (Bibliographic References)

### 2.1 GitHub README & OSS 実証研究
1. **`[REF-PRANA2019]`**: Gede Artha Azriadi Prana, Christoph Treude, Ferdian Thung, Thushari Atapattu, David Lo. "Categorizing the Content of GitHub README Files". *Empirical Software Engineering*, Vol. 24, pp. 1296–1327 (2019). DOI: [10.1007/s10664-018-9660-3](https://doi.org/10.1007/s10664-018-9660-3) / arXiv: [1802.06997](https://arxiv.org/abs/1802.06997).
2. **`[REF-SITTHI2023]`**: Supavas Sitthithanasakul, Bodin Chinthanet, Raula Gaikovina Kula, Natthakit Netsiwarawichian, Pattara Leelaprute, Bundit Manaskasemsak, Arnon Rungsawang, Kenichi Matsumoto. "Do Developers Present Proficient Code Snippets in Their README Files? An Analysis of PyPI Libraries in GitHub". *Journal of Information Processing*, Vol. 31, pp. 679–688 (2023). DOI: [10.2197/ipsjjip.31.679](https://doi.org/10.2197/ipsjjip.31.679).
3. **`[REF-ABDUL2026]`**: Ashraf Abdulmunim Abdulmajeed. "A Software Engineering Perspective on Documentation Quality: Predicting Newcomer Attraction in Open-Source Projects". *Statistics, Optimization and Information Computing*, Vol. x, pp. 1–24 (2026).
4. **`[REF-HELLMAN2023]`**: Jazlyn Hellman, Eunbee Jang, Christoph Treude, Chenzhun Huang, Jin L.C. Guo. "Describing GitHub Repositories". *SSRN Electronic Journal* (2023). SSRN: [4543196](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4543196).
5. **`[REF-GAUGHAN2025]`**: Matthew Gaughan, Kaylea Champion, Sohyeon Hwang, Aaron Shaw. "The Introduction of README and CONTRIBUTING Files in Open Source Software Development". arXiv: [2502.18440](https://arxiv.org/abs/2502.18440) (2025).
6. **`[REF-FRONCH2023]`**: Felipe Fronchetti, David C. Shepherd, Igor Wiese, Christoph Treude, Marco Aurélio Gerosa, Igor Steinmacher. "Do CONTRIBUTING Files Provide Information about OSS Newcomers’ Onboarding Barriers?". *ESEC/FSE 2023*, pp. 1–13 (2023). DOI: [10.1145/3611643.3616288](https://doi.org/10.1145/3611643.3616288).
7. **`[REF-FOUNDJEM]`**: Armstrong Foundjem, Ellis E. Eghan, Bram Adams. "Onboarding vs. Diversity, Productivity, and Quality – Empirical Study of the OpenStack Ecosystem". *Proceedings of the 43rd International Conference on Software Engineering (ICSE '21)*, pp. 1033–1045 (2021). DOI: [10.1109/ICSE43902.2021.00097](https://doi.org/10.1109/ICSE43902.2021.00097).
8. **`[REF-DANTAS2023]`**: Carlos Eduardo C. Dantas et al. "How do Developers Improve Code Readability? An Empirical Study of Pull Requests". arXiv: [2309.02594](https://arxiv.org/abs/2309.02594) (2023).

### 2.2 信頼性・シグナリング & 説得工学
9. **`[REF-ALLEN1991]`**: Mike Allen. "Meta-Analysis Comparing the Persuasiveness of One-Sided and Two-Sided Messages". *Western Journal of Speech Communication*, Vol. 55, No. 4, pp. 390–404 (1991). DOI: [10.1080/10570319109374395](https://doi.org/10.1080/10570319109374395).
10. **`[REF-OKEFE1999]`**: Daniel J. O'Keefe. "How to Handle Opposing Arguments in Persuasive Messages: A Meta-Analytic Review of the Effects of One-Sided and Two-Sided Messages". *Annals of the International Communication Association*, Vol. 22, No. 1, pp. 209–249 (1999). DOI: [10.1080/23808985.1999.11678963](https://doi.org/10.1080/23808985.1999.11678963).
11. **`[REF-KAMINS1989]`**: Michael A. Kamins, Meribeth J. Brand, Stuart A. Hoeke, John C. Moe. "Two-Sided Versus One-Sided Celebrity Endorsements: The Impact on Advertising Effectiveness and Credibility". *Journal of Advertising*, Vol. 18, No. 2, pp. 4–10 (1989). DOI: [10.1080/00913367.1989.10673146](https://doi.org/10.1080/00913367.1989.10673146).
12. **`[REF-PARAM2026]`**: Ranindya Paramitha, Christian Kästner, Laurie Williams. "The Software Supply Chain as a Market for Lemons: A Multivocal Review of Trust Signal Collapse". arXiv: [2608.20678](https://arxiv.org/abs/2608.20678) (2026).
13. **`[REF-ASA2026]`**: Asa Romeo Asa, Johanna Pangeiko Nautwima. "Corporate digital responsibility and consumer trust: a signaling theory perspective". *Cogent Business & Management*, Vol. 13, No. 1, 2607753 (2026). DOI: [10.1080/23311975.2025.2607753](https://doi.org/10.1080/23311975.2025.2607753).
14. **`[REF-TSOY2012]`**: Mikhail Tsoy, D. Sandy Staples. "Role of reputation cues in trust formation for a developer's decision to join Open Source Software projects". *Proceedings of the International Conference on Information Systems (ICIS)* (Queen's University).
15. **`[REF-RUBIN2023]`**: Eran Rubin, Izak Benbasat. "Using Toulmin's Argumentation Model to Enhance Trust in Analytics-Based Advice Giving Systems". *ACM Transactions on Management Information Systems*, Vol. 14, No. 3, Article 22, pp. 1–28 (2023). DOI: [10.1145/3580479](https://doi.org/10.1145/3580479).
16. **`[REF-REED2005]`**: Chris Reed, Glenn Rowe. "Translating Toulmin, Diagramming Argument & Pollock's Undercutter". *Argumentation*, Vol. 19, pp. 267–286 (2005).
17. **`[REF-NABWIRE2026A]`**: Sharon Nabwire, Eunice Agyei et al. "Evaluating the influence of persuasive systems design on continuance intention, perceived effectiveness, and weight loss". *Digital Health*, Vol. 12, pp. 1–18 (2026). DOI: [10.1177/20552076261461365](https://doi.org/10.1177/20552076261461365).
18. **`[REF-NABWIRE2026B]`**: Sharon Nabwire, Renata Savian Colvero de Oliveira et al. "Enhancing the perceived effectiveness of health behaviour change support systems through transparency in persuasive systems design". *Behaviour & Information Technology*, Vol. 45, No. 18, pp. 4431–4445 (2026). DOI: [10.1080/0144929X.2026.2638915](https://doi.org/10.1080/0144929X.2026.2638915).
19. **`[REF-RAHMAN2024]`**: Parinda Rahman, Ifeoma Adaji. "Designing Ethical and Trustworthy Persuasive Technologies". *International Conference on Mobile and Ubiquitous Multimedia (MUM '24)*, pp. 1–3 (2024). DOI: [10.1145/3701571.3703385](https://doi.org/10.1145/3701571.3703385).
20. **`[REF-RAHMAN2025]`**: Parinda Rahman. "Ethics and Trust in Persuasive Technology Design". Ph.D. Thesis, University of British Columbia (2025).
21. **`[REF-BENNER2022]`**: Dennis Benner, Sofia Marlena Schöbel, Andreas Janson, Jan Marco Leimeister. "How to Achieve Ethical Persuasive Design: A Review and Theoretical Propositions for Information Systems". *AIS Transactions on Human-Computer Interaction*, Vol. 14, No. 4, pp. 548–577 (2022). DOI: [10.17705/1thci.00179](https://doi.org/10.17705/1thci.00179).
22. **`[REF-CEMILOGLU2021]`**: Deniz Cemiloglu, Raian Ali. "Explainable Persuasion in Interactive Design". *IEEE International Conference on Systems, Man, and Cybernetics (SMC)* (2021).
23. **`[REF-AMGOUD2009]`**: Leila Amgoud. "Argumentation for Decision Making". In: Iyad Rahwan, Guillermo R. Simari (Eds.), *Argumentation in Artificial Intelligence*, Chapter 15, pp. 301–320, Springer-Verlag Berlin Heidelberg (2009). DOI: [10.1007/978-0-387-98197-0_15](https://doi.org/10.1007/978-0-387-98197-0_15).

### 2.3 段階的開示・情報設計 & 認知負荷
24. **`[REF-MURALI2025]`**: Deepa Muralidhar, Rafik Belloum, Ashwin Ashok. "Operationalizing selective transparency using progressive disclosure in artificial intelligence clinical diagnosis systems". HAL: [hal-05331557v2](https://hal.science/hal-05331557v2) (2025).
25. **`[REF-SPRING2020]`**: Aaron Springer, Steve Whittaker. "Progressive Disclosure: When, Why, and How Do Users Want Algorithmic Transparency Information?". *ACM Transactions on Interactive Intelligent Systems*, Vol. 10, No. 4, Article 29, pp. 1–32 (2020). DOI: [10.1145/3374218](https://doi.org/10.1145/3374218).
26. **`[REF-ANIK2026]`**: Ariful Islam Anik, Andrea Bunt. "Designing Effective Training Dataset Explanations: The Impact of Information Depth and Progressive Disclosure". *31st International Conference on Intelligent User Interfaces (IUI '26)*, pp. 1–16 (2026). DOI: [10.1145/3742413.3789087](https://doi.org/10.1145/3742413.3789087).
27. **`[REF-NIELSEN2006]`**: Jakob Nielsen. "Progressive Disclosure". *Nielsen Norman Group Articles* (2006).
28. **`[REF-HORTON2006]`**: Sarah Horton. "Designing Beneath the Surface of the Web". *Proceedings of the 2006 International Cross-Disciplinary Workshop on Web Accessibility (W4A '06)*, pp. 1–5 (2006). DOI: [10.1145/1133219.1133221](https://doi.org/10.1145/1133219.1133221) (および *Access by Design: A Guide to Universal Usability for Web Designers*, New Riders, 2006).
29. **`[REF-PROCTER2001]`**: Chris Procter, Judith Symonds. "Designing for web site usability". (2001).
30. **`[REF-MATTYAS2020]`**: Dóra Mattyasovszky-Philipp, Bálint Molnár. "An Architectural Approach to Cognitive Information Systems". *Acta Polytechnica Hungarica*, Vol. 17, No. 2, pp. 237–253 (2020). DOI: [10.12700/APH.17.2.2020.2.13](https://doi.org/10.12700/APH.17.2.2020.2.13).
31. **`[REF-STOREY1997]`**: Margaret-Anne D. Storey, F. David Fracchia, Hausi A. Müller. "Cognitive Design Elements to Support the Construction of a Mental Model During Software Exploration". *Journal of Systems and Software* (1997).
32. **`[REF-COWAN2001]`**: Nelson Cowan. "The Magical Number 4 in Short-Term Memory: A Reconsideration of Mental Storage Capacity". *Behavioral and Brain Sciences*, Vol. 24, No. 1, pp. 87–185 (2001).
33. **`[REF-DURAN2022]`**: Rodrigo Duran, Albina Zavgorodniaia, Juha Sorva. "Cognitive Load Theory in Computing Education Research: A Review". *ACM Transactions on Computing Education*, Vol. 22, No. 4, Article 40, pp. 1–27 (2022). DOI: [10.1145/3483843](https://doi.org/10.1145/3483843) (および併録一次資料: Sharon Oviatt. "Human-Centered Design Meets Cognitive Load Theory: Designing Interfaces that Help People Think". *ACM Multimedia '06*, pp. 871–880 (2006). DOI: [10.1145/1180639.1180831](https://doi.org/10.1145/1180639.1180831)).
34. **`[REF-SWEL2011]`**: John Sweller, Paul Ayres, Slava Kalyuga. *Cognitive Load Theory*. Springer New York (2011).
35. **`[REF-SU2012]`**: Moon Ting Su, Ewan Tempero, John Hosking, John Grundy. "A study of architectural information foraging in software architecture documents". *Joint Working IEEE/IFIP Conference on Software Architecture and European Conference on Software Architecture (WICSA/ECSA)*, pp. 141–150 (2012). DOI: [10.1109/WICSA-ECSA.212.22](https://doi.org/10.1109/WICSA-ECSA.212.22).
36. **`[REF-PAECH2016]`**: Jürgen Börstler, Barbara Paech. "The Role of Method Chains and Comments in Software Readability and Comprehension—An Experiment". *IEEE Transactions on Software Engineering*, Vol. 42, No. 9, pp. 886–898 (2016). DOI: [10.1109/TSE.2016.2527791](https://doi.org/10.1109/TSE.2016.2527791).
37. **`[REF-KALYUGA2011]`**: Slava Kalyuga. "Informing: A Cognitive Load Perspective". *Informing Science: The International Journal of an Emerging Transdiscipline*, Vol. 14, pp. 33–45 (2011). DOI: [10.28945/1349](https://doi.org/10.28945/1349).

### 2.4 論理学・形式証明
38. **`[REF-JACQUETTE2008]`**: Dale Jacquette. "Mathematical Proof and Discovery: Reductio ad Absurdum". *Informal Logic*, Vol. 28, No. 3, pp. 242–261 (2008).
39. **`[REF-JANSEN2007]`**: Henrike Jansen. "Refuting a Standpoint by Appealing to Its Outcomes: Reductio ad Absurdum vs. Argument from Consequences". *Informal Logic*, Vol. 27, No. 3, pp. 249–266 (2007).
40. **`[REF-RUSHBY2009]`**: John Rushby. "Software Verification and System Assurance". *7th IEEE International Conference on Software Engineering and Formal Methods (SEFM)*, pp. 3–10 (2009).
41. **`[REF-PRAWITZ2018]`**: Dag Prawitz. "The Fundamental Problem of General Proof Theory". *Studia Logica*, Vol. 107, pp. 11–29 (2019, Online 2018). DOI: [10.1007/s11225-018-9785-9](https://doi.org/10.1007/s11225-018-9785-9).
42. **`[REF-VONPLATO2020]`**: Jan von Plato. "The Development of Proof Theory". *Stanford Encyclopedia of Philosophy* (2008 / substantive revision 2020).
43. **`[REF-BAIER2024]`**: Daniel Baier, Dirk Beyer et al. "Software Verification with CPAchecker 3.0: Tutorial and User Guide". *Formal Methods (FM 2024)*, LNCS 14934, pp. 543–570 (2025). DOI: [10.1007/978-3-031-71177-0_30](https://doi.org/10.1007/978-3-031-71177-0_30).
44. **`[REF-KNIGHT2010]`**: Xiang Yin, John Knight. "Formal Verification of Large Software Systems". *NASA Formal Methods Symposium (NFM 2010)*, NASA/CP-2010-216215 (20100018552) (2010).
45. **`[REF-SIEG1998]`**: Wilfried Sieg, John Byrnes. "Normal Natural Deduction Proofs (in classical logic)". *Studia Logica*.

### 2.5 CVR・離脱防止 & コピー・LPの型
46. **`[REF-NIELSEN2018]`**: Jakob Nielsen. "Scrolling and Attention: Increasing Engagement Below the Fold". *Nielsen Norman Group Research Reports* (2018).
47. **`[REF-MULLIN2023]`**: Shanelle Mullin. "Above the Fold vs. Below the Fold: How To Encourage Scrolling". *CXL Institute* (2023).
48. **`[REF-SHAPIRO2020]`**: Julian Shapiro. "Startup Handbook: Landing Page Copywriting & Conversion Optimization". (2020).
49. **`[REF-DRY2020]`**: Harry Dry. "Rewriting landing pages with a pro copywriter". *Marketing Examples* (2020).
50. **`[REF-UNBOUNCE2022]`**: Unbounce. "High-Converting Landing Pages: Anatomy, Structure & Design Guidelines". (2022).
51. **`[REF-USERPILOT2026]`**: Userpilot. "Features, Advantages & Benefits: The FAB Model for Product Onboarding". (2026).
52. **`[REF-KANDA2016]`**: 神田昌典. 『稼ぐ言葉の法則――「新・PASONAの法則」と売れる公式41』. ダイヤモンド社 (2016).
53. **`[REF-SALESCOPY2026]`**: The Sales Copy. "4Pの法則：LP、セールスレターの構成で迷ったらこれ" (2026).
54. **`[REF-COPYHACKERS2015]`**: Joanna Wiebe. "Every Copywriting Formula Ever: The Ultimate Guide to High-Converting Copy". *Copyhackers* (2015).

### 2.6 哲学的公理・実証再現性基盤
55. **`[REF-HUME1739]`**: David Hume. *A Treatise of Human Nature*. Book III, Part I, Section I (1739).
56. **`[REF-PENG2011]`**: Roger D. Peng. "Reproducible Research in Computational Science". *Science*, Vol. 334, No. 6060, pp. 1226–1227 (2011). DOI: [10.1126/science.1213847](https://doi.org/10.1126/science.1213847).

### 2.7 視覚効果・グラフィック・絵文字認知研究
57. **`[REF-LU2018]`**: Xuan Lu, Yanbin Cao, Zhenpeng Chen, Xuanzhe Liu. "A First Look at Emoji Usage on GitHub: An Empirical Study". arXiv: [1812.04863](https://arxiv.org/abs/1812.04863) (2018).
58. **`[REF-RONG2023]`**: Shiyue Rong. "Why Do Developers Use Emojis in GitHub? An Empirical Study". UC Irvine MS Thesis, `qt18p2s3c3` (2023).
59. **`[REF-BORGO]`**: Rita Borgo, Alfie Abdul-Rahman, Farhan Mohamed, Philip W. Grant, Irene Reppa, Luciano Floridi, Min Chen. "An Empirical Study on Using Visual Metaphors in Visualization". *IEEE Transactions on Visualization and Computer Graphics*.
60. **`[REF-LIU2026]`**: Yunguo Liu, Zizhen Liu, Xuelin Tang, Rang Meng. "Effects of icon semantic distance and cultural background on visual search efficiency in vehicle control interfaces". *Scientific Reports*, 16: 7066 (2026). DOI: [10.1038/s41598-026-37943-8](https://doi.org/10.1038/s41598-026-37943-8).
61. **`[REF-LUJIE2024]`**: Deng Lujie, Chunhua Lin, Qiong Liao, Shuicai Qiu. "The effects of icon design features on user perception and preference: A case study of icons for Covid-19". *PLOS ONE*, 19(9): e0305290 (2024). DOI: [10.1371/journal.pone.0305290](https://doi.org/10.1371/journal.pone.0305290).
62. **`[REF-SILVEN2025]`**: Johanna Silvennoinen et al. "Icons for Software Implementations of Interactive Multiobjective Optimization Methods: A Semantic Distance Study". *Journal of Multi-Criteria Decision Analysis*, 32: e70010 (2025). DOI: [10.1002/mcda.70010](https://doi.org/10.1002/mcda.70010).
63. **`[REF-ROY2025]`**: Ankita Roy & Hiroyuki Matsuguma. "Interface Iconography, Intricacies and Relationships in Contemporary Digital Realms". *International Journal of Asia Digital Art and Design*, Vol. 29, S1, pp. 76–85 (2025).
64. **`[REF-LI2016]`**: Jie Li, Kang Zhang et al. "The impact of metaphors on information visualization". *Journal of Visualization*, 19: 533–548 (2016). DOI: [10.1007/s12650-016-0371-9](https://doi.org/10.1007/s12650-016-0371-9).
65. **`[REF-SUNG2012]`**: Eunmo Sung, Richard E. Mayer. "When graphics improve liking but not learning from online lessons". *Computers in Human Behavior*, 28(5), pp. 1618–1625 (2012).
66. **`[REF-DANIELSON2012]`**: Robert William Danielson. "THE EFFECT OF DECORATIVE GRAPHICS ON EXPOSITORY TEXT COMPREHENSION". Master's Thesis, California State University, Chico (2012).
67. **`[REF-SCHNEIDER2017]`**: Sascha Schneider. "The impact of decorative pictures on learning with media". Doctoral dissertation, Faculty of Humanities, Technische Universität Chemnitz (2017).
68. **`[REF-HARPER2009]`**: Simon Harper, Eleni Michailidou, Robert Stevens. "Toward a Definition of Visual Complexity as an Implicit Measure of Cognitive Load". *ACM Transactions on Applied Perception (TAP)*, Vol. 6, No. 2, Article 10 (2009). DOI: [10.1145/1498700.1498704](https://doi.org/10.1145/1498700.1498704).
69. **`[REF-YADAV2026]`**: Anamika Yadav. "A Review Study of Cognitive Load in Website and Mobile Application User Interface Design". *Journal Publication of International Research for Engineering and Management (JOIREM)*, Vol. 4, Issue 4, pp. 1–6 (2026).
70. **`[REF-SANCHEZ2006]`**: Christopher A. Sanchez, Jennifer Wiley. "An examination of the seductive details effect in terms of working memory capacity". *Memory & Cognition*, 34(2), pp. 344–355 (2006).
71. **`[REF-TIGWELL2020]`**: Garreth W. Tigwell, Benjamin M. Gorman, Rachel Menzies. "Emoji Accessibility for Visually Impaired People". *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (CHI '20)*, Paper 140, pp. 1–14 (2020). DOI: [10.1145/3313831.3376267](https://doi.org/10.1145/3313831.3376267).
72. **`[REF-OSU2026]`**: Oregon State University College of Health. "Best Practices for Emoji Accessibility". *Digital Accessibility Guidelines* (2026-02-12).
73. **`[REF-KERDAR2024]`**: Sara Hamideh Kerdar, Liane Bächler, Britta Marleen Kirchhoff. "The accessibility of digital technologies for people with visual impairment and blindness: a scoping review". *Discover Computing*, Vol. 27, Article 14 (2024). DOI: [10.1007/s10791-024-09460-7](https://doi.org/10.1007/s10791-024-09460-7).
74. **`[REF-ZHANG2025]`**: Xuanchang Zhang, Wei Xiong, Lichang Chen, Tianyi Zhou, Heng Huang, Tong Zhang. "From Lists to Emojis: How Format Bias Affects Model Alignment". arXiv: [2409.11704](https://arxiv.org/abs/2409.11704) (2025).
75. **`[REF-GLIKSON2018]`**: Ella Glikson, Arik Cheshin, Gerben A. van Kleef. "The dark side of a smiley: Effects of Smiling Emoticons on Virtual First Impressions". *Social Psychological and Personality Science*, 9(5), pp. 614–625 (2018). DOI: [10.1177/1948550617720269](https://doi.org/10.1177/1948550617720269).
76. **`[REF-LI2019]`**: Xueni (Shirley) Li, Kimmy Wa Chan, Sara Kim. "Service with Emoticons: How Customers Interpret Employee Use of Emoticons in Online Service Encounters". *Journal of Consumer Research*, 45(5), pp. 973–987 (2019). DOI: [10.1093/jcr/ucy016](https://doi.org/10.1093/jcr/ucy016).
77. **`[REF-VAREBERG2023]`**: Kyle R. Vareberg, Olivia Vogt, Maranda Berndt. "Putting your best face forward: How instructor emoji use influences students’ impressions of credibility, immediacy, and liking". *Education and Information Technologies*, 28, pp. 6075–6092 (2023). DOI: [10.1007/s10639-022-11421-w](https://doi.org/10.1007/s10639-022-11421-w).
78. **`[REF-VRIELINK2025]`**: Esmee Vrielink. "From Email to WhatsApp: The Impact of Emojis on Professional Communication Across Channels". Master's Thesis, Tilburg University (2025).
79. **`[REF-HILLBERG2018]`**: Hannah Miller Hillberg, Zachary Levonian, Daniel Kluver, Loren Terveen, Brent Hecht. "What I See is What You Don’t Get: The Effects of (Not) Seeing Emoji Rendering Differences across Platforms". *Proceedings of the ACM on Human-Computer Interaction*, Vol. 2, CSCW, Article 124 (2018). DOI: [10.1145/3274393](https://doi.org/10.1145/3274393).
80. **`[REF-MILLER2017]`**: Hannah Miller, Daniel Kluver, Jacob Thebault-Spieker, Loren Terveen, Brent Hecht. "Understanding Emoji Ambiguity in Context: The Role of Text in Emoji-Related Miscommunication". *Proceedings of the 11th International AAAI Conference on Web and Social Media (ICWSM 2017)*, pp. 152–161 (2017).

---

## 3. 付記：筆者自身の関連ノート

※ **[`PAPER.md`](./PAPER.md)** 第5章の脚注（`[^naam]`）にて言及している、筆者自身の思考フレームワーク（7層モデル：事実の確認 → 合理性の確認 → 時代条件の確認 → 制約の確認 → 普及条件の確認 → 数字の検証 → 再現可能性の確認）の初出記事は以下の通りです。

- Yuzuko Underson. 「[NaaM(Numbers are a Mirage)思考フレームワーク概念定義仕様書](https://note.com/dandy_viper3242/n/na5ceff82ae2e)」. *note* (2026-04-02).

---

## 4. 付記：Web実態観察資料（非査読記事・テンプレート事例）

※ **[`PAPER.md`](./PAPER.md)** 第5章の脚注（`[^web-obs]`）にて「非査読のWeb流通実態の観察例」として言及している資料群（学術的根拠ではなく、マーケティング言説の流入やLLMテンプレート循環の観察事例。ローカル一次資料は `references/絵文字懐疑reference/なぜ絵文字を使うのか/` 配下に格納）は以下の通りです。

- Medium (2025-06-19). *The Power of Emojis in Marketing: Boost Engagement and Strengthen Brand Communication*（スキム文化における視覚的アンカーとしての言説事例）。
- DEV.to (2023-11-27). *How to Boost Your Productivity as a Developer with Emojis*（開発者記事における視覚的手がかりの言説事例）。
- MarkdownTools (2025-09-11). *Markdown Emoji Guide: Complete Reference for Technical Documentation and Content Creation*（技術文書向け絵文字ガイドの主張事例）。
- note (2025-08-25). 『エンジニア向け README作成完全ガイド』（絵文字付き見出しを含むREADMEテンプレート内に `https://claude.ai/chat/LICENSE` のURL痕跡が残留していた実態事例）。
- Zenn (2022-11-21) 『GitHubのREADMEの見た目をイケてる感じにする』、Zenn『技術記事を読んでほしい私が、「伝え方」で気をつけている5つのポイント（具体例つき）』、はてなブログ (2026-06-28) 『GitHub の README をきれいに書く方法まとめ』、decopon-room (2025-08-16) 『GitHubのREADMEで伝わる技術資料を作る方法【Markdown入門つき】』。