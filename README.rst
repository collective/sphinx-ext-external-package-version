``collective.sphinxextexternalpackageversion``
==============================================

.. image:: https://img.shields.io/pypi/v/collective-sphinxextexternalpackageversion
    :target: https://pypi.org/project/collective-sphinxextexternalpackageversion/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/collective-sphinxextexternalpackageversion
    :target: https://pypi.org/project/collective-sphinxextexternalpackageversion/
    :alt: Supported Python versions

.. image:: https://app.readthedocs.org/projects/collective-sphinxextexternalpackageversion/badge/
    :target: https://collective-sphinxextexternalpackageversion.readthedocs.io/en/stable/
    :alt: Documentation status

.. image:: https://github.com/collective/sphinx-ext-external-package-version/actions/workflows/tests.yml/badge.svg?branch=main
    :alt: Build status
    :target: https://github.com/collective/sphinx-ext-external-package-version/actions/workflows/tests.yml

.. image:: https://img.shields.io/pypi/dm/collective-sphinxextexternalpackageversion
    :alt: PyPI monthly downloads

.. image:: https://img.shields.io/github/sponsors/silviubogan
    :target: https://github.com/sponsors/silviubogan
    :alt: GitHub Sponsors

This Collective Sphinx extension, ``collective.sphinxextexternalpackageversion``, shows the version of an external package through a special syntax in the documentation.

You can find the documentation at the following URL: https://collective-sphinxextexternalpackageversion.readthedocs.io/en/stable/ (currently broken).

To get the latest stable version of a GitHub repository that is in a release on GitHub, place ``{{ version x/y }}`` in your documentation, where ``x/y`` is the title of the GitHub repository, ``x`` is the owner, ``y`` is the actual repository name. For example:

Here is a code block::

  The latest version of nvm is {{ version nvm-sh/nvm }}.

This code block will output, as of the time of writing this documentation::

  The latest version of nvm is 0.40.8.

Note that this works through a RegEx and will work in code blocks and included files too. This works only for public repos that actually have a release.

Currently there is no way to escape the syntax to show in your docs the literal string ``{{ version x/y }}``.

How to use
==========

*TODO: Check if this works.*

After installing the package with 'uv' link the extension to your Sphinx project:

*TODO*

Then, in your ``conf.py`` file, add the following string to the ``extensions`` list::

  "collective.sphinxextexternalpackageversion"

How to contribute
=================

See the `CONTRIBUTING.md`_ file for instructions on how to contribute to this project.

Versions
========

See `the changelog here`_.

.. _CONTRIBUTING.md: ./CONTRIBUTING.md
.. _the changelog here: ./CHANGELOG.rst
