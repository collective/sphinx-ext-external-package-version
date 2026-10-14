"""Minimal Sphinx 8.1.3 compatibility smoke test."""

import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path


def main():
    tmp = tempfile.TemporaryDirectory()
    src = Path(tmp.name, "src")
    src.mkdir()
    (src / "conf.py").write_text(
        "extensions = ['collective.sphinxextexternalpackageversion']\n"
    )

    (src / "index.rst").write_text(
        textwrap.dedent(
            """
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
    """,
            encoding="utf-8",
        )
    )

    (src / "included.rst").write_text(
        textwrap.dedent(
            """
    G
    H {{version nvm-sh/nvm}} I
    J
    """,
            encoding="utf-8",
        )
    )

    out = Path(tmp.name, "out")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sphinx",
            "-W",
            "-b",
            "html",
            "-d",
            str(out / ".doctrees"),
            str(src),
            str(out),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    page = (out / "index.html").readtext(encoding="utf-8")
    assert page.count("nvm-sh/nvm") == 3
    return result


if __name__ == "__main__":
    main()
