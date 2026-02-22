# Sphinx Slides

Sphinxとsphinx-revealjsを使用した複数スライド公開システム。

## 🚀 特徴

- 複数のプレゼンテーションを一元管理
- GitHub Pagesで自動公開
- Reveal.jsベースのモダンなスライド
- 日本語完全対応

## 📁 プロジェクト構成

```
sphinx_slide/
├── source/
│   ├── slides/
│   │   ├── presentation1/     # 技術プレゼンテーション
│   │   │   ├── index.rst
│   │   │   └── conf.py
│   │   ├── presentation2/     # ビジネスプレゼンテーション
│   │   │   ├── index.rst
│   │   │   └── conf.py
│   │   └── shared/            # 共有リソース
│   │       ├── _static/
│   │       └── _image/
│   └── index.rst              # トップページ
├── .github/workflows/
│   └── deploy.yml             # GitHub Pages自動デプロイ
├── Makefile                   # ビルドコマンド
└── requirements.txt           # Python依存関係
```

## 🛠️ セットアップ

### 環境要件

- Python 3.13
- pip

### インストール

```bash
# 仮想環境作成
python3.13 -m venv .venv
source .venv/bin/activate  # macOS/Linux

# 依存関係インストール
pip install -r requirements.txt

# Playwrightインストール（スクリーンショット機能用）
playwright install
```

## 📝 使い方

### ローカルで確認

```bash
# 全スライドをビルド
make all-slides

# ローカルサーバー起動
python -m http.server 8080 --directory build/revealjs
```

http://localhost:8080 で確認できます。

### 個別スライドのビルド

```bash
# 技術プレゼンテーション
make presentation1

# ビジネスプレゼンテーション
make presentation2
```

### 新しいスライドの追加

1. `source/slides/new_presentation/` ディレクトリを作成
2. `index.rst` と `conf.py` を作成
3. `Makefile` に新しいターゲットを追加
4. `source/index.rst` にリンクを追加

## 🚀 デプロイ

masterブランチにpushすると、GitHub Actionsが自動でビルドしGitHub Pagesに公開します。

```bash
git add .
git commit -m "Add new slides"
git push origin master
```

## 📊 公開URL

- トップページ: `https://slide.sion908.tech/`
- 技術スライド: `https://slide.sion908.tech/presentation1/`
- ビジネススライド: `https://slide.sion908.tech/presentation2/`
- ポートフォリオ: `https://portfolio.sion908.tech/`

## 🛠️ 開発

### PDFを画像に変換

`pdftoimg/scr.py` でPDFをJPEG画像に変換できます：

```bash
cd pdftoimg
python scr.py
```

### カスタマイズ

- テーマ: `conf.py` の `html_theme` を変更
- スタイル: `shared/_static/` にCSSファイルを配置
- 画像: `shared/_image/` に画像ファイルを配置

## 📄 ライセンス

MIT License

## 👤 作者

**sion908**

- GitHub: [@sion908](https://github.com/sion908)

---

Built with ❤️ using [Sphinx](https://www.sphinx-doc.org/) and [Reveal.js](https://revealjs.com/)