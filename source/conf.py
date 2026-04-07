# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'スライド公開サイト'
copyright = '2024, sion908 lab'
author = 'sion908'

# LaTeX の docclass 設定
latex_docclass = {'manual': 'jsbook'}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "oembedpy.adapters.sphinx",
    'sphinx_revealjs',
    'sphinx.ext.githubpages',
    'sphinxemoji.sphinxemoji',
    "sphinxext.opengraph",
    "sphinx_design",
    "sphinxext.opengraph",
    "atsphinx.qrcode",
    "sphinx_nekochan",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'default'

# Standard HTML (index.rst) settings
html_static_path = ['slides/shared/_static', 'slides/shared/_image', "_static"]
html_css_files = ['portfolio.css', "custom.css"]

# PWA and SEO files
html_extra_path = ['_static/manifest.json', '_static/icons', '_static/robots.txt', '_static/icons/favicon.ico', '_static/sitemap.xml']

# Reveal.jsプレゼンテーションで使う静的ファイルを管理しているフォルダを指定
revealjs_static_path = [
    'slides/shared/_static',
    'slides/shared/_image',
]

revealjs_css_files = []

revealjs_script_plugins = [
    # Reveal.js組み込みのシンタックスハイライトプラグインを使う
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "RevealCustomControls",
        "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/plugin.js"
    },
]

# Reveal.jsのベーステーマを変更
# revealjs_style_theme = 'sky'

# Reveal.jsプレゼンテーションで使うCSSファイルを指定
revealjs_css_files = [
    'portfolio.css',
    'layout.css',
    'footnotes.css',
    "revealjs/plugin/highlight/zenburn.css",
]

revealjs_script_conf = {  # プラグインの有効化
    # "customcontrols": {
    #     "controls": [
    #         {
    #             "title": "Go to GitHub",
    #             "icon": '<i class="fa fa-github"></i>',
    #             "action": "location.href = 'https://github.com/attakei/slides/';",
    #         },
    #     ]
    # },
}

# sphinx-nekochan フッター設定
nekochan_footer = {
    "text": "slide.sion908.tech",
    "link": "https://slide.sion908.tech",
    "target": "_blank",
}
