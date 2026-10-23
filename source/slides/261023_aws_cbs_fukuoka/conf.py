project = 'AWS Community Builders Kyushu 2026'
copyright = '2026, sion908'
author = 'sion908'

extensions = [
    'oembedpy.adapters.sphinx',
    'sphinx.ext.githubpages',
    'sphinx_revealjs',
    'sphinxemoji.sphinxemoji',
    'sphinx_design',
    'sphinx_revealjs.ext.screenshot',
    'sphinxext.opengraph',
    'atsphinx.qrcode',
    'sphinx_nekochan',
    'sphinxcontrib.budoux',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'ja'
revealjs_static_path = ['../shared/_static', '../shared/_image']
revealjs_script_plugins = [
    {'name': 'RevealHighlight', 'src': 'revealjs/plugin/highlight/highlight.js'},
    {'name': 'RevealNotes', 'src': 'revealjs/plugin/notes/notes.js'},
]
revealjs_style_theme = 'league'
revealjs_css_files = [
    'portfolio.css',
    'layout.css',
    'footnotes.css',
    'revealjs/plugin/highlight/zenburn.css',
]

ogp_site_url = 'https://slide.sion908.tech/slides/261023_aws_cbs_fukuoka/'
ogp_description_length = 200
ogp_social_cards = {'enable': False}
ogp_image = 'https://slide.sion908.tech/slides/261023_aws_cbs_fukuoka/_images/ogp/index.png'
revealjs_screenshot_excludes = ['whois']

def setup(app):
    app.setup_extension('sphinx_revealjs.ext.screenshot')

nekochan_footer = {
    'text': 'slide.sion908.tech',
    'link': 'https://slide.sion908.tech',
    'target': '_blank',
}
budoux_targets = ['h1', 'h2', 'h3']
