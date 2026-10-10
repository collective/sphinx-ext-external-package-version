.. module:: collective.sphinxextexternalpackageversion
   :synopsis: Sphinx extension to show the version of an external package through a special syntax in the documentation.

TODO: move what is to be moved from here to README.rst of the package.

To get the latest stable version of a GitHub repository that is in a release on GitHub, place `{{ version x/y }}` in your documentation, where `x/y` is the title of the GitHub repository, x is the owner, y is the actual repository name. Example:

Here is a code block:

```
The latest version of nvm is {{ version nvm-sh/nvm }}.
```

will output as of the time of writing this documentation:

```
The latest version of nvm is 0.40.8.
```

TODO: in the output above, make the version number always up-to-date.
TODO: Make a way to escape the special syntax.

Note that this works through a RegEx and will work in code blocks and included files too. This works only for public repos that actually have a release.

# How to use

In your `conf.py` file, add the following line to the `extensions` list:

```python
"collective.sphinxextexternalpackageversion"
```

after installing the package with 'uv':

TODO
