# Documentation configuration file.
# Copyright Ashley. 2023.

# Possible configuration values listed at
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = "sphinx-simple-theme"
copyright = "Copyright Ashley. 2023."
author = "Ashley"

# -- General configuration ---------------------------------------------------
extensions = ["sphinx.ext.imgmath", "sphinxcontrib.spelling"]

root_doc = "index"

needs_sphinx = "4.0"

nitpicky = True

numfig = True
numfig_format = {
    "figure": "Figure %s",
    "table": "Table %s",
    "code-block": "Code %s",
    "section": "Section %s"
}

# -- Options for Math --------------------------------------------------------
math_number_all = True
math_eqref_format = "Equation {number}"
math_numfig = False

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx-simple-theme"
html_theme_path = ["../../../sphinx-simple-theme"]

html_title = "Sphinx simple theme"
html_logo = "_static/logo.svg"

html_permalinks_icon = "&#128279"

html_link_suffix = ".html"

# Dictionary with key of empty string is the target of parent element
html_theme_options = {
    "navigation_sections": {
        "Install": {
            "": "installation.html",
            "Quick start": "installation.html#quick-start",
            "Full install": "installation.html#full-install"
        },
        "Options": "options.html",
        "Examples": "examples.html"
    }
}

# -- Spelling options --------------------------------------------------------
spelling_lang = "en_GB"
spelling_show_suggestions = True
