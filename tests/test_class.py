import json
import os
import pathlib
import tempfile
import textwrap
import unittest
import urllib
import urllib.request as req

from sphinx.application import Sphinx


# This function is a copy of the one in src/collective/sphinxextexternalpackageversion/__init__.py
def latest_release_for_github_repo(repo):
    latest_release_url = "https://api.github.com/repos/" + repo + "/releases/latest"
    try:
        with req.urlopen(latest_release_url) as response:
            commit = json.load(response)
            return commit["name"]
    except urllib.error.HTTPError as e:
        # Handles HTTP errors (e.g., 404, 500)
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        # Handles URL errors (e.g., DNS failure, refused connection)
        print(f"URL Error: {e.reason}")
    except TimeoutError:
        # Handles timeout specifically
        print("Request timed out.")


class TestSphinxExtension(unittest.TestCase):
    def build(self, count=3):
        if count != 3 and count != 1:
            raise ValueError("count must be either 3 or 1")

        self.tmp = tempfile.TemporaryDirectory()
        src = pathlib.Path(self.tmp.name, "src")
        src.mkdir()
        (src / "conf.py").write_text(
            "extensions = ['collective.sphinxextexternalpackageversion']\n"
        )

        if count == 3:
            (src / "index.rst").write_text(
                textwrap.dedent(
                    """
                    A
                    B {{ version nvm-sh/nvm }} C
                    D

                    ```text
                    E
                    F {{ version nvm-sh/nvm }} G
                    H
                    ```
                    
                    .. include:: included.rst
                    """
                )
            )
        elif count == 1:
            (src / "index.rst").write_text(
                textwrap.dedent(
                    """
                    A
                    B {{ verion nvm-sh/nvm }} C
                    D

                    ```text
                    E
                    F { version nvm-sh/nvm }} G
                    H
                    ```
                    
                    .. include:: included.rst
                    """
                )
            )

        (src / "included.rst").write_text(
            textwrap.dedent(
                """
                G
                H {{version nvm-sh/nvm}} I
                J
                """
            )
        )

        out = pathlib.Path(self.tmp.name, "out")

        app = Sphinx(
            str(src),
            str(src),
            str(out),
            str(out / ".doctrees"),
            "html",
            status=None,
        )
        app.build()
        return app

    def tearDown(self):
        self.tmp.cleanup()

    def test_one(self):
        self.build()
        page = pathlib.Path(os.path.join(self.tmp.name, "out", "index.html")).read_text(
            encoding="utf-8"
        )
        self.tearDown()
        self.assertTrue(
            page.count(latest_release_for_github_repo("nvm-sh/nvm")) == 3,
            "Expected 3 occurrences of the version string in the output without syntax errors.",
        )

        self.build(count=1)
        page = pathlib.Path(os.path.join(self.tmp.name, "out", "index.html")).read_text(
            encoding="utf-8"
        )
        self.tearDown()
        self.assertTrue(
            page.count(latest_release_for_github_repo("nvm-sh/nvm")) == 1,
            "Expected 1 occurrence of the version string in the output with two wrong syntaxes.",
        )
