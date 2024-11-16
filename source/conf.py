# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2024, sion908'
author = 'sion908'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 使用する拡張としてsphinx-revealjsを新規追加
    'sphinx_revealjs',
    'sphinx.ext.githubpages',
    # 追加: sphinxemojiは2個書くことに注意
    'sphinxemoji.sphinxemoji',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'league'

# Reveal.jsプレゼンテーションで使う静的ファイルを管理しているフォルダを指定
revealjs_static_path = ['_static']

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

]

# Reveal.jsプレゼンテーションで使うCSSファイルを指定
# revealjs_static_pathで指定したフォルダからのパス
revealjs_css_files = [
    'slides.css',
    "revealjs/plugin/highlight/zenburn.css",
]
