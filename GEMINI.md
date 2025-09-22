# Profile ✦GEMINI

## GitHub Profile (Implemented)

### GitHub Markdown Limitation

GitHub の README はセキュリティ上インライン CSS (style 属性) や class 指定が無視されるので、border-radius や color: といった装飾は効かない。つまり、次の制約がある:

- ✅ HTML タグ(`<table>`, `<img>`, `<b>`, `<sub>`, `<a>`) が使える
- ❌ `style="..."` , `class="..."` が無視される

### Python によるカード作成

`README.md` における、高機能なカードの作成のため、push 前に `images/cards/` 内にカード (jpg) を作成する python コードを実装する。
カード実装案：

- 画像の右下の端に、赤い直角三角形を描画し、その内部に `images/games/platforms/nintendo-switch.png` (正方形のまま) の付与
- 画像の右下の端に、青い直角三角形を設置し、その内部に `images/games/platforms/steam.png` (円形に) の付与

カード作成は `scripts/` 内に設置した python により行う。(GitHub Actions でこの python の実行と push を行う)

`README.md` の `<table />` 部にそのカードを採用

## Profile Website on Vercel

URL 構成案

- `/`
  Next.js+TailwindCSS で簡素だが機構の施されたプロフィール。
  名称は dracoboost's Blog (dracoboost&apos;s Blog)
  HoHatchの紹介と、ブログの記事一覧を付記。
- `/blog/<BLOG_TITLE>`
  `website/content/<BLOG_TITLE>.md` 由来でブログ生成。
  Markdown Blog にも、`/` の footer を用いる。

プロジェクト構成案

- `npm run dev` により、開発サーバーを起動する。
- `npm run build` により、Vercel 用にサイトを build する。
- `npm run preflight` により、テストを行う。

### `<header>`, `<main>`, `<footer>`

`<header><main><footer>`という構成は、ウェブサイトのトップレベルの構造 (例えば、index.htmlのようなルートのページ) に適している。

例：

```html
<body>
  <header>
    <h1>My Website</h1>
    <nav>...</nav>
  </header>
  <main>
    <article>
      <h2>記事のタイトル</h2>
      <p>記事の内容...</p>
    </article>
  </main>
  <footer>
    <p>© 2025 My Website</p>
  </footer>
</body>
```

`<main>`タグの内部に`<header>`や`<footer>`が存在することは、セクションごとのヘッダーやフッターとして機能するため、これも正しい使い方だ。この場合、それらはページ全体のヘッダーやフッターではなく、ProjectsSectionやBlogSectionといった特定のコンテンツブロックの導入部や末尾を示す。

例：

```html
<main>
  <header>
    <h1>プロフィールのタイトル</h1>
  </header>
  <section>
    <h2>Projects</h2>
    <footer>
      <p>すべてのプロジェクトを見る</p>
    </footer>
  </section>
  <section>
    <h2>Blog</h2>
    <footer>
      <p>すべての記事を見る</p>
    </footer>
  </section>
</main>
```

### Thumbnails

Featured Project HoHatch：`public/images/hohatch/hohatch-og-1200x600.png` を利用する。
Latest Blog Post `content/introducing-hohatch.md`：`public/images/hohatch/hohatch-application-screenshot.jpg` を利用する。

まとめて markdown ブログに用いる、サムネ画像や本文中に貼る画像は、`website/public/` 内に作成したブログ専属のフォルダで一元管理したほうが整理されると考えているが、.md やサムネ・本文画像のパス配置のベストプラクティスはあるか。

### OG Images

X 向け：`public/images/og/dracoboost-og-1200x600.png`
その他向け：`public/images/og/dracoboost-og-1200x630.png`

### Header Image

`/` に設置する header 画像は `public/images/headers/maliss.png` (1600x300) を用いる。

### Background Color

Header Background Color: `#010409`
Main Background Color: `#0d1117`
Footer Background Color: `#010409`

## Development Guidelines

This section provides essential guidelines for contributing to the HoHatch project, covering building, testing, and coding standards.

### Python Virtual Environment

`venv/bin/python3` や `venv/bin/pip` を用いること。決してグローバルの python 環境を汚染しないこと。
`git commit` 前に、`requirements.txt` を `pip freeze` により更新する。

### Language Policy

ソースコードは英語で記載する。

### Comments Policy

- Only write high-value comments if at all. Avoid talking to the user through comments.
- Do not leave removed code as commented out; delete it.
- Write comments in English.

## Code Design Principles

### Service-Oriented Architecture

The backend is structured with a service-oriented architecture, where distinct services handle specific concerns (e.g., configuration, file operations, image processing). This improves modularity, testability, and maintainability.

### Feature Separation

Improve reusability, maintainability, and readability by creating components and structures for frequently occurring structures.

### Ensuring Consistency

Improve readability and maintainability, and strengthen security by ensuring consistency in hash functions, environment variable names, and error handling.

### Step-by-step Debugging

Resolve multiple errors one by one. Identify the root cause.

### Maintainability

Actively structure and modularize code for maintainability.
