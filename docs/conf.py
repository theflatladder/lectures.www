# -*- coding: utf-8 -*-
#
# Основы Веб-программирования documentation build configuration file,
# created by sphinx-quickstart on Sun Jan 18 19:36:48 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
from datetime import datetime

import docutils
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.latex import LaTeXBuilder
from sphinx.directives.code import CodeBlock

import itcase_sphinx_theme

sys.path.insert(0, os.path.abspath('.'))

from common import GLOBAL_LINKS  # noqa

links_collection = GLOBAL_LINKS

directives.register_directive('no-code-block', CodeBlock)

# IMAGES
image_types = ['image/png', 'image/svg+xml', 'image/gif', 'image/jpeg']

# Redefine supported_image_types for the HTML and LaTeX builder
LaTeXBuilder.supported_image_types = image_types
StandaloneHTMLBuilder.supported_image_types = image_types


# html_logo = 'info-small.png'
html_favicon = '_static/urfu.ico'
html_sidebars = {
    '**': ['globaltoc.html',
           'searchbox.html',
           'sourcelink.html',
           ],
    'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
html_theme_options = {
    'travis_button': False,
    'github_button': True,
    'github_user': 'ustu',
    'github_repo': 'lectures.www',
    'logo': True,
    'logo_image': 'info-small.png',
    'logo_width': 'auto',
}

# If true, figures, tables and code-blocks are automatically numbered if they
# has caption. For now, it works only with the HTML builder. Default is False.
numfig = True
# A dictionary mapping 'figure', 'table' and 'code-block' to strings that are
# used for format of figure numbers. Default is to use 'Fig. %s' for 'figure',
# 'Table %s' for 'table' and 'Listing %s' for 'code-block'.
numfig_format = {"figure": u"Рис. %s",
                 "table": u"Таблица %s",
                 "code-block": u"Код %s"}


# If true, figures, tables and code-blocks are automatically numbered if they
# has caption. For now, it works only with the HTML builder. Default is False.
numfig = True
# A dictionary mapping 'figure', 'table' and 'code-block' to strings that are
# used for format of figure numbers. Default is to use 'Fig. %s' for 'figure',
# 'Table %s' for 'table' and 'Listing %s' for 'code-block'.
numfig_format = {"figure": u"Рис. %s",
                 "table": u"Таблица %s",
                 "code-block": u"Код %s"}

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'itcase_sphinx_theme',
    'sphinx_links',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# TODO
if 'NO_METRIKA' in os.environ:
    todo_include_todos = True

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Основы Веб-программирования'
copyright = u'2015, uralbash'

release_date = datetime.now().strftime("%Y-%m-%d")

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'ru'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d-%m-%Y'
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['contents.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [itcase_sphinx_theme.get_html_themes_path()]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'itcase'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = '-doc'

# -- Options for LaTeX output ---------------------------------------------
ADDITIONAL_PREAMBLE = """
\\setcounter{tocdepth}{3}
"""

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4papper',
    'wrapperclass': 'scrbook',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
    # 'fontpkg': '\\usepackage[sfdefault]{cabin}',
    # Additional stuff for the LaTeX preamble.
    'preamble': ADDITIONAL_PREAMBLE,
    'figure_align': 'ht',  # htbp
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'lectures.tex',
     u'Основы Веб-программирования',
     u'Свинцов Дмитрий', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = html_logo

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', '-', u'Основы Веб-программирования Documentation',
     u'uralbash', '-', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Основы Веб-программирования'
epub_author = u'uralbash'
epub_publisher = u'uralbash'
epub_copyright = u'2015, uralbash'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'http://docs.python.org/': None,
    'http://docs.sqlalchemy.org/en/latest/': None,
    'http://initd.org/psycopg/docs/': None,

    # Pylons
    'http://pyramid-tm.readthedocs.org/en/latest/': None,
    'http://docs.pylonsproject.org/projects/colander/en/latest/': None,
    'http://docs.pylonsproject.org/projects/pyramid/en/latest/': None,
    'http://docs.pylonsproject.org/projects/pyramid-debugtoolbar/en/latest/':
    None,
    'http://deform.readthedocs.org/en/latest/': None,
    'http://venusian.readthedocs.org/en/latest/': None,
    'http://pyramid-sqlalchemy.readthedocs.org/en/latest/': None,
    'http://docs.webob.org/en/latest/': None,
}


# TODO: сделать через директиву, типа .. note::
def sourcecode(role, rawtext, text, lineno, inliner,
               options={}, content=[]):
    """
    Example:

        See code there :src:`6.www.sync/2.codding/blog/0.paster`.
    """
    # Base URL mainly used by inliner.rfc_reference, so this is correct:
    SOURCE_URL =\
        'https://github.com/ustu/lectures.www/tree/master/sourcecode/'
    ref = SOURCE_URL + text
    set_classes(options)
    node = docutils.nodes.reference(
        rawtext,
        SOURCE_URL + docutils.utils.unescape(text),
        refuri=ref, **options)
    return [node], []


def setup(app):
    """Install the plugin.

    :param app: Sphinx application context.
    """
    if 'NO_METRIKA' not in os.environ:
        app.add_javascript('js/metrika.js')
    app.add_javascript('js/jquery.fancybox.js')
    app.add_stylesheet('css/jquery.fancybox.css')
    app.add_stylesheet('css/todo.css')

    # Add roles
    app.add_role('src', sourcecode)
