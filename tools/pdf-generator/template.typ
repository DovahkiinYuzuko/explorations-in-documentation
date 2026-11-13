// 論文プレプリント風 Typst テンプレート
// 和欧混植: 欧文 Libertinus / New Computer Modern + 和文 Noto CJK JP

#let paper_template(
  title: "無題",
  author: "Yuzuko Underson (DovahkiinYuzuko)",
  date_str: "",
  abstract_body: none,
  body,
) = {
  // 基本文書設定
  set document(
    title: title,
    author: author,
  )

  set page(
    paper: "a4",
    margin: (top: 23mm, bottom: 23mm, left: 26mm, right: 26mm),
    header: context {
      let page_num = counter(page).get().first()
      if page_num > 1 [
        #set text(
          font: "Noto Sans CJK JP",
          size: 7.8pt,
          fill: luma(110),
        )
        #set par(justify: false)
        #let short_title = title.split("：").at(0)
        #grid(
          columns: (1fr, auto),
          align: (left, right),
          [#short_title],
          [#author],
        )
        #v(2pt)
        #line(length: 100%, stroke: 0.4pt + luma(190))
      ]
    },
    footer: context {
      set text(
        font: "Noto Sans CJK JP",
        size: 8.5pt,
        fill: luma(100),
      )
      align(center)[
        — #counter(page).display("1 / 1", both: true) —
      ]
    },
  )

  // 本文テキスト設定（和欧混植）
  set text(
    lang: "ja",
    region: "jp",
    font: ("Libertinus Serif", "Noto Serif CJK JP"),
    size: 10.5pt,
    fill: luma(25),
    top-edge: "ascender",
    bottom-edge: "descender",
  )

  set par(
    justify: true,
    leading: 0.65em,
    spacing: 1.1em,
    first-line-indent: 0pt,
  )

  // 数式内の日本語テキストにも和文フォントが効くようフォールバックを設定
  show math.equation: set text(
    font: ("New Computer Modern Math", "Libertinus Serif", "Noto Serif CJK JP"),
  )

  // 見出し設定（ゴシック体 + 孤立防止）
  show heading: it => {
    set text(
      font: "Noto Sans CJK JP",
      fill: luma(15),
    )
    block(sticky: true, it)
  }

  show heading.where(level: 1): it => {
    v(1.4em, weak: true)
    set text(size: 13.4pt, weight: "bold")
    block(sticky: true)[
      #it.body
      #v(-4pt)
      #line(length: 100%, stroke: 0.8pt + luma(60))
    ]
    v(0.55em, weak: true)
  }

  show heading.where(level: 2): it => {
    v(1.1em, weak: true)
    set text(size: 11.8pt, weight: "bold")
    block(sticky: true, it.body)
    v(0.35em, weak: true)
  }

  show heading.where(level: 3): it => {
    v(0.85em, weak: true)
    set text(size: 10.5pt, weight: "bold", fill: luma(45))
    block(sticky: true, it.body)
    v(0.25em, weak: true)
  }

  // リスト設定
  set list(indent: 1.0em, body-indent: 0.5em, spacing: 0.55em)
  set enum(indent: 1.0em, body-indent: 0.5em, spacing: 0.55em)

  // 引用ブロック（外枠は境界でのみ分割可、内側の Original と 日本語訳+出所 は build_pdf.py で個別 keep）
  show quote.where(block: true): it => {
    v(0.4em, weak: true)
    block(
      width: 100%,
      breakable: true,
      fill: rgb("#f8fafc"),
      stroke: (left: 2.5pt + rgb("#475569")),
      inset: (left: 10pt, right: 9pt, top: 7pt, bottom: 7pt),
      radius: (right: 2pt),
    )[
      #set text(size: 9.3pt, fill: luma(35))
      #set par(leading: 0.58em, spacing: 0.6em)
      #it.body
    ]
    v(0.4em, weak: true)
  }

  // コードブロック・インラインコード
  show raw.where(block: true): it => {
    v(0.4em, weak: true)
    block(
      width: 100%,
      breakable: false,
      fill: rgb("#f6f8fa"),
      stroke: 0.5pt + rgb("#d0d7de"),
      inset: 8pt,
      radius: 3pt,
    )[
      #set text(
        font: ("DejaVu Sans Mono", "Noto Sans CJK JP"),
        size: 8.5pt,
      )
      #set par(leading: 0.6em)
      #it
    ]
    v(0.4em, weak: true)
  }

  show raw.where(block: false): it => box(
    fill: rgb("#f1f5f9"),
    inset: (x: 3pt, y: 0pt),
    outset: (y: 2pt),
    radius: 2pt,
  )[
    #set text(
      font: ("DejaVu Sans Mono", "Noto Sans CJK JP"),
      size: 8.8pt,
    )
    #it
  ]

  // 学術論文風テーブル（Booktabs スタイル）
  set table(
    stroke: (x, y) => (
      top: if y == 0 { 1.1pt + luma(30) } else if y == 1 { 0.7pt + luma(80) } else { 0.3pt + luma(210) },
      bottom: 1.1pt + luma(30),
    ),
    inset: (x: 7pt, y: 6pt),
    fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else { none },
  )

  show table.cell.where(y: 0): set text(
    font: "Noto Sans CJK JP",
    weight: "bold",
    size: 9pt,
  )

  show table: set text(size: 8.8pt)
  show table: set par(justify: false)

  // 図表のキャプション見出しを日本語化＋ページ跨ぎ分割防止
  set figure(supplement: [図])
  show figure: set block(breakable: false)
  show figure.caption: set text(
    font: "Noto Sans CJK JP",
    size: 8.8pt,
    fill: luma(70),
  )

  // 外部 URL リンクのみ青色＋下線（目次などのページ内リンクは通常表示）
  show link: it => {
    if type(it.dest) == str {
      underline(
        offset: 2pt,
        stroke: 0.6pt + rgb("#1d4ed8"),
        text(fill: rgb("#1d4ed8"), it),
      )
    } else {
      it
    }
  }
  set footnote.entry(
    separator: line(length: 35%, stroke: 0.5pt + luma(130)),
    gap: 0.5em,
  )

  // 水平線
  show line: it => it

  // === 1ページ目冒頭: タイトルブロック ===
  block(width: 100%, below: 1.0em)[
    #set text(font: "Noto Sans CJK JP")
    #text(size: 8.5pt, fill: luma(100), tracking: 0.08em)[
      TECHNICAL RESEARCH PAPER / SSoT: PAPER.md
    ]
    #v(0.35em)
    #text(size: 17.0pt, weight: "bold", fill: luma(10))[
      #set par(leading: 0.5em, justify: false)
      #title
    ]
    #v(0.65em)
    #grid(
      columns: (1fr, auto),
      align: (left, right),
      text(size: 9.5pt, fill: luma(50))[著者: #author],
      if date_str != "" { text(size: 9pt, fill: luma(90))[生成日: #date_str] },
    )
    #v(0.3em)
    #line(length: 100%, stroke: 1.2pt + luma(30))
  ]

  // === 要旨 (Abstract) ===
  if abstract_body != none [
    #block(
      width: 100%,
      fill: rgb("#f8fafc"),
      stroke: (top: 0.6pt + luma(160), bottom: 0.6pt + luma(160)),
      inset: (x: 11pt, y: 9pt),
      below: 1.1em,
    )[
      #text(
        font: "Noto Sans CJK JP",
        size: 10pt,
        weight: "bold",
        fill: luma(20),
      )[要旨 (Abstract)]
      #v(0.4em)
      #set text(size: 9.3pt)
      #set par(leading: 0.6em, spacing: 0.7em)
      #abstract_body
    ]
  ]

  // === 2ページ目以降: 自動目次（ページ跨ぎで途切れないよう独立ページ配置） ===
  pagebreak(weak: true)
  block(width: 100%, breakable: false, below: 1.4em)[
    #show outline.entry.where(level: 1): it => block(
      above: 0.7em,
      below: 0.15em,
      strong(it),
    )
    #outline(
      title: text(
        font: "Noto Sans CJK JP",
        size: 11pt,
        weight: "bold",
      )[目次],
      indent: 1.4em,
      depth: 2,
    )
    #v(0.5em)
    #line(length: 100%, stroke: 0.6pt + luma(180))
  ]
  pagebreak(weak: true)

  body
}
