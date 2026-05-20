# Configuration file for the Sphinx documentation builder.
project = '技術プレゼンテーション'
copyright = '2024, sion908'
author = 'sion908'

# matplotlibフォント設定（sphinxext.opengraph用）
import matplotlib.font_manager as fm
import os
from pathlib import Path

# ローカルフォントのパスを追加
font_dir = os.path.join(os.path.dirname(__file__), '../../_static/fonts')
for font_file in ['HackGen-Regular.ttf', 'HackGen-Bold.ttf']:
    font_path = os.path.join(font_dir, font_file)
    if os.path.exists(font_path):
        fm.fontManager.addfont(font_path)
        # フォントファミリ名を取得
        font_prop = fm.FontProperties(fname=font_path)
        font_family = font_prop.get_name()
    else:
        font_family = "DejaVu Sans"

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
    "sphinxcontrib.budoux",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'
html_theme = 'league'

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

revealjs_css_files = [
    'portfolio.css',
    'layout.css',
    'footnotes.css',
    "revealjs/plugin/highlight/zenburn.css",
]

# sphinxext.opengraph 設定
ogp_site_url = 'https://slide.sion908.tech/slides/260223_ailt/'
ogp_description_length = 200
ogp_social_cards = {
    "enable": False, # sphinx-revealjsのスクリーンショットを使用するため無効化
}
ogp_image = '_images/ogp/index.png'  # sphinx-revealjsのスクリーンショット画像を使用

# sphinx-revealjs.ext.screenshot設定（OGP画像生成に使用）
revealjs_screenshot_excludes = ["*/?_*", "*/whois"]

# --- Monkey Patch for sphinxext-opengraph ---
# OGPソーシャルカード（PNG画像）と og:description のテキストを
# 本文ではなく .. meta:: :description: から取得するように差し替える。
# __init__.py は起動時に `from ._description_parser import get_description` で
# ローカル変数に束縛するため、モジュール側だけでなく __init__ 側も差し替える。
import docutils.nodes
import sphinxext.opengraph._description_parser as ogp_desc
import sphinxext.opengraph as ogp_init
import sphinxext.opengraph._social_cards as ogp_social

original_get_desc = ogp_desc.get_description

def custom_get_description(doctree, length, known_titles):
    # .. meta:: ディレクティブの description を優先的に取得
    for node in doctree.traverse(docutils.nodes.meta):
        if node.get('name') == 'description':
            return node.get('content')
    # なければ元の挙動（本文からの抽出）にフォールバック
    return original_get_desc(doctree, length, known_titles)

# モジュールの参照とその利用元の両方を置き換える
ogp_desc.get_description = custom_get_description
ogp_init.get_description = custom_get_description

# タイトルの折り返し幅を調整（デフォルトの825から600に減らす）
original_set_page_title_line_width = ogp_social._set_page_title_line_width

def custom_set_page_title_line_width():
    return 600  # デフォルト825から600に減らして折り返しを促進

ogp_social._set_page_title_line_width = custom_set_page_title_line_width

# whoisページではOGP画像を生成しないようにする
original_social_card_for_page = ogp_init.social_card_for_page

def custom_social_card_for_page(config_social, site_name, title, description, pagename, ogp_site_url, ogp_canonical_url, *, srcdir, outdir, config, env):
    # whoisページではOGP画像を生成しない
    if pagename.endswith('whois'):
        return None
    return original_social_card_for_page(config_social, site_name, title, description, pagename, ogp_site_url, ogp_canonical_url, srcdir=srcdir, outdir=outdir, config=config, env=env)

ogp_init.social_card_for_page = custom_social_card_for_page

# sphinx-nekochan フッター設定
nekochan_footer = {
    "text": "slide.sion908.tech",
    "link": "https://slide.sion908.tech",
    "target": "_blank",
}

# sphinxcontrib-budoux設定（日本語の折り返しを改善）
budoux_targets = ["h1", "h2", "h3"]

# sphinxext.opengraph 設定
