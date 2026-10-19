# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

if os.environ.get("READTHEDOCS"):
    print()
    print("CWD:", os.getcwd())
    print("Configuration path:", os.path.abspath(__file__))
    print("Environment variables:")
    for key in sorted(os.environ):
        print(f"  {key}={os.environ[key]}")
    print()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "collective-sphinxextexternalpackageversion"
copyright = "2026, Silviu Bogan"
author = "Silviu Bogan"
release = "0.1.0"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
