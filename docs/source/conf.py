# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
from pathlib import Path

abs_path = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, abs_path.__str__())

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NotKinoPoiskAPI'
copyright = '2024, Maxim Harder'
author = 'Maxim Harder'
release = '1.0.0'
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx_rtd_theme',
	'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
	'sphinx.ext.napoleon',
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.autosummary',
	'sphinx.ext.extlinks',
	'sphinx.ext.githubpages',
	'sphinx.ext.todo',
	# 'autoapi.extension',
	# 'sphinx_autopackagesummary',
]
autosummary_generate = True
# autoapi_generate_api_docs = False
# autodoc_typehints = 'description'

# autoapi_dirs = [
# 		'../../NotKinoPoiskAPI',
# ]
templates_path = ['_templates']
exclude_patterns = [
	'_build', 'Thumbs.db', '.DS_Store', '__pycache__', '.gitignore', 'changelog.md', 'env.default', 'LICENSE', 'make.bat', 'Makefile', 'manifest.json', 'pyproject.toml',
	'requirements.txt', 'setup.py', '*.pyc'
]

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = "_static/ntkpapi.jpg"
html_favicon = "_static/ntkpapi.jpg"
github_url = "https://github.com/DevCraftClub/NotKinoPoiskAPI"
