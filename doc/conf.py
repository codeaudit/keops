#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# KeOps documentation build configuration file, created by
# sphinx-quickstart on Thu Sep 13 14:50:06 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys, os
import sphinx_gallery
from recommonmark.transform import AutoStructify

from pykeops import __version__
if __version__ == "???" : __version__ = "0.1.7"

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.insert(0, os.path.abspath('sphinxext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.napoleon',
]

sphinx_gallery_conf = {
     # path to your examples scripts
     'examples_dirs': ['../pykeops/examples', '../pykeops/tutorials', '../pykeops/benchmarks'],
     # path where to save gallery generated examples
     'gallery_dirs': ['./_auto_examples', '_auto_tutorials', '_auto_benchmarks'],
}

# Generate the API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False
autodoc_member_order = 'alphabetical'

def skip(app, what, name, obj, would_skip, options):
    if name == "__call__":
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

# Include the example source for plots in API docs
# plot_include_source = True
# plot_formats = [("png", 90)]
# plot_html_show_formats = False
# plot_html_show_source_link = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'KeOps'

#import time
#copyright = '2018-{}, Benjamin Charlier, Jean Feydy, Joan A. Glaunès'.format(time.strftime("%Y"))

copyright = '2018-2019, Benjamin Charlier, Jean Feydy, Joan A. Glaunès.'
author = 'Benjamin Charlier, Jean Feydy, Joan A. Glaunès.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "KeOps"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "KeOps documentation"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/logo/logo.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'KeOpsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'KeOps.tex', 'KeOps Documentation',
     'Benjamin Charlier, Jean Feydy, Joan A. Glaunès', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'keops', 'KeOps Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'KeOps', 'KeOps Documentation',
     author, 'KeOps', 'One line description of project.',
     'Miscellaneous'),
]

def setup(app):
    app.add_stylesheet('theme_override.css')
