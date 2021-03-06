# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'THAT docs'
copyright = '2021, Anabrid'
author = 'Anabrid'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.mathjax",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

html_sidebars = {
    "**": [
        "logo-text.html",
        "globaltoc.html",
        "localtoc.html",
        "searchbox.html"]
}

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'THAT', # do not show

    # Set you GA account ID to enable tracking

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://project.github.io/project',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://lab.analogparadigm.com/ulmann/the-analog-thing/-/tree/master/documentation/sphinx',
    'repo_name': 'Gitlab',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,
    

    "nav_links": [
        #{"href": "index", "internal": True, "title": "Welcome"},
        #{"href": "basics/index", "internal": True, "title": "Basics"},
        #{"href": "applications/index", "internal": True, "title": "Applications"},
        #{"href": "interfaces/index", "internal": True, "title": "Interfaces"},        
        {'href': 'https://the-analog-thing.org/', 'internal': False, 'title': 'THAT Home'},
        {'href': 'https://shop.anabrid.com/', 'internal': False, 'title': 'THAT Shop'},
        {'href': 'https://analogparadigm.com/', 'internal': False, 'title': 'Analog Paradigm'},
        {'href': 'https://anabrid.com/', 'internal': False, 'title': 'Anabrid'},
    ],
}


html_use_index = True
html_domain_indices = True

# Grouping the document tree into LaTeX files. List of tuples# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
 ('index', 'yourdoc.tex', u'THAT docu', u'anabrid', 'manual'),
]
