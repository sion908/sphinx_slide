# Configuration file for the Sphinx documentation builder.
project = 'comming soon...'
copyright = '2024, sion908'
author = 'sion908'

extensions = [
    "oembedpy.adapters.sphinx",
    'sphinx.ext.githubpages',
    'sphinx_revealjs',
    'sphinxemoji.sphinxemoji',
    "sphinx_design",
    "sphinx_revealjs.ext.screenshot",
    "sphinxext.opengraph",
    "atsphinx.qrcode",
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
