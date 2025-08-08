# Configuration file for the Sphinx documentation builder.

project = 'MapBoards Documentation'
copyright = "2020-%Y, Icarus Soft Landings, LLC"
author = "Icarus"
release = '1.885'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "rst2pdf.pdfbuilder",
]
autosectionlabel_prefix_document = True
templates_path = ["_templates"]
exclude_patterns = ["**/.*"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_with_keys": "true",
    "body_max_width": "none",
}
html_copy_source = False
html_use_index = False
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sphinx = False
pdf_documents = [("index", "MapBoards", "MapBoards doc", "Icarus")]
