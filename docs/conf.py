import os
import sys
from datetime import datetime

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath('..'))

# Project information
project = 'Music Insights'
author = 'Biell Guembri'
copyright = f'{datetime.now().year}, {author}'
release = '1.0.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',  # Automatically generate documentation from docstrings
    'sphinx.ext.viewcode',  # Add links to source code
    'sphinx_rtd_theme',     # Use the Read the Docs theme
]

# Theme
html_theme = 'sphinx_rtd_theme'

# Options for autodoc
autodoc_default_options = {
    'members': True,
    'special-members': '__init__',
    'undoc-members': True,
    'show-inheritance': True,
}