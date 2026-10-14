"""Minimal Sphinx 8.1.3 compatibility smoke test."""

import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import requests


# This function is a copy of the one in src/collective/sphinxextexternalpackageversion/__init__.py
def latest_release_for_github_repo(repo):
    latest_release_url = "https://api.github.com/repos/" + repo + "/releases/latest"
    try:
        response = requests.get(latest_release_url)
        response.raise_for_status()
        commit = response.json()
        return commit["name"]
    except requests.RequestException as e:
        print(f"GET request error: {e.response.status_code} - {e.response.reason}")


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

    (src / "included.rst").write_text(
        textwrap.dedent(
            """
            G
            H {{version nvm-sh/nvm}} I
            J
            """
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
    page = (out / "index.html").read_text(encoding="utf-8")
    assert page.count(latest_release_for_github_repo("nvm-sh/nvm")) == 3
    return result


if __name__ == "__main__":
    main()
