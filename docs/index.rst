.. module:: collective.sphinxextexternalpackageversion
   :synopsis: Sphinx extension to show the version of an external package through a special syntax in the documentation.

To get the latest stable version of a GitHub repository that is in a release on GitHub, place `{{ version x/y }}` in your documentation, where `x/y` is the title of the GitHub repository, `x` is the owner, `y` is the actual repository name. For example:

Here is a code block:

```
The latest version of nvm is {{ version nvm-sh/nvm }}.
```

will output as of the time of writing this documentation:

```
The latest version of nvm is 0.40.8.
```

Note that this works through a RegEx and will work in code blocks and included files too. This works only for public repos that actually have a release.

Currently there is no way to escape the syntax to show in your docs the literal string `{{ version x/y }}`.

# How to use

**TODO: Check if this works.**

After installing the package with 'uv' link the extension to your Sphinx project:

**TODO**

Then, in your `conf.py` file, add the following string to the `extensions` list:

```python
"collective.sphinxextexternalpackageversion"
```

# How to contribute

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for instructions on how to contribute to this project.
