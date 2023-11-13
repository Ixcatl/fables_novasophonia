# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Us Who Remain: TTRPG Rulebook'
copyright = '2023, Ixcatl'
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
    'hoverxref.extension',
    'sphinx_tabs.tabs',
    'sphinx_favicon'
]

hoverxref_auto_ref = True
hoverxref_sphinxtabs = True
hoverxref_domains = ["py"]
hoverxref_roles = [
    "option",
    # Documentation pages
    # Not supported yet: https://github.com/readthedocs/sphinx-hoverxref/issues/18
    "doc",
    # Glossary terms
    "term"
]
hoverxref_role_types = {
    "mod": "modal",  # for Python Sphinx Domain
    "doc": "modal",  # for whole docs
    "class": "tooltip",  # for Python Sphinx Domain
    "ref": "tooltip",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "term": "tooltip"  # for glossaries
}

sphinx_tabs_disable_tab_closing = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_book_theme'
html_title = 'Us Who Remain: TTRPG Rulebook'
html_theme_options = {
    'display_version': False
    # "use_download_button": False,
    # "use_fullscreen_button": False,
    # "show_toc_level": 2
}

favicons = [
   {
      "sizes": "16x16",
      "href": "favicon-16x16.ico",  # use a local file in _static
   },
   {
      "rel": "apple-touch-icon",
      "sizes": "180x180",
      "href": "favicon-180x180.ico"
   }
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
