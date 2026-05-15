# Configuration file for the Sphinx documentation builder.
project = 'Geeks Who Drink in Nagasaki'
copyright = '2026, sion908'
author = 'sion908'

# matplotlibフォント設定（sphinxext.opengraph用）
import matplotlib.font_manager as fm
import os

# ローカルフォントのパスを追加
font_dir = os.path.join(os.path.dirname(__file__), '../../_static/fonts')
for font_file in ['HackGen-Regular.ttf', 'HackGen-Bold.ttf']:
    font_path = os.path.join(font_dir, font_file)
    if os.path.exists(font_path):
        fm.fontManager.addfont(font_path)

extensions = [
    "oembedpy.adapters.sphinx",
    'sphinx.ext.githubpages',
    'sphinx_revealjs',
    'sphinxemoji.sphinxemoji',
    "sphinx_design",
    "sphinx_revealjs.ext.screenshot",
    "sphinxext.opengraph",
    "atsphinx.qrcode",
    "sphinx_nekochan",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# Reveal.js設定
revealjs_static_path = ['../shared/_static', '../shared/_image']

revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
]

revealjs_style_theme = 'league'

revealjs_css_files = [
    'portfolio.css',
    'layout.css',
    'footnotes.css',
    "revealjs/plugin/highlight/zenburn.css",
]

# sphinxext.opengraph 設定
ogp_social_cards = {
    "enable": True,
    "font": "HackGen",
}

# sphinx-nekochan フッター設定
nekochan_footer = {
    "text": "slide.sion908.tech",
    "link": "https://slide.sion908.tech",
    "target": "_blank",
}
