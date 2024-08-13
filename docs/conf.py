# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Us Who Remain: TTRPG Rulebook'
copyright = '2023-2024, by Ixcatl & HKRPG Team'
author = 'Ixcatl'

release = '1.0'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'hoverxref.extension',
    'sphinx_favicon',
    'sphinx_design'
]

autosectionlabel_prefix_document = True


hoverxref_auto_ref = True
hoverxref_domains = [
    'py'
]
hoverxref_roles = [
    'option',
    # Documentation pages
    # Not supported yet: https://github.com/readthedocs/sphinx-hoverxref/issues/18
    'doc',
    # Glossary terms
    'term'
]
hoverxref_role_types = {
    'hoverxref': 'tooltip',
    'mod': 'modal',  # for Python Sphinx Domain
    'doc': 'modal',  # for whole docs
    'class': 'tooltip',  # for Python Sphinx Domain
    'ref': 'tooltip',  # for hoverxref_auto_ref config
    'confval': 'tooltip',  # for custom object
    'term': 'tooltip'  # for glossaries
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme' # sphinx-rtd-theme==1.3.0rc1 sphinx==7.1.2
# html_theme = 'sphinx_book_theme' # sphinx-book-theme==1.0.1 sphinx==6.2.1
html_title = 'Us Who Remain: TTRPG Rulebook'
html_theme_options = {
    'display_version': False,
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': -1,
    'prev_next_buttons_location': 'None'
    # "use_download_button": False,
    # "use_fullscreen_button": False,
    # "show_toc_level": 2
}

html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

favicons = [
   {
      "sizes": "16x16",
      "href": "favicon-16x16.ico"  # use a local file in _static
   },
   {
      "rel": "apple-touch-icon",
      "sizes": "180x180",
      "href": "favicon-180x180.ico"
   }
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
