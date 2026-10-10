import pathlib
import tempfile
import unittest

from sphinx.application import Sphinx


class OneTestCase(unittest.TestCase):
    def build(self):
        self.tmp = tempfile.TemporaryDirectory()
        src = pathlib.Path(self.tmp.name, "src")
        src.mkdir()
        (src / "conf.py").write_text(
            "extensions = ['collective.sphinxextexternalpackageversion']\n"
        )

        (src / "index.rst").write_text("""
        .. module:: collective.sphinxextexternalpackageversion
        A
        B {{ version nvm-sh/nvm }} C
        D

        ```text
        E
        F {{ version nvm-sh/nvm }} G
        H
        ```
        ```{include} included.rst
        ```
        """)

        (src / "included.rst").write_text("""
        G
        H {{version nvm-sh/nvm}} I
        J
        """)

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
        page = (self.tmp / "html").read_text(encoding="utf-8")
        self.assertTrue(
            page.count("0.40.8") == 3,
            "Expected 3 occurrences of the version string in the output.",
        )
