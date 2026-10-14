"""Minimal Sphinx 8.1.3 compatibility smoke test."""

import json
import subprocess
import sys
import tempfile
import textwrap
import urllib
import urllib.request as req
from pathlib import Path


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
    v = latest_release_for_github_repo("nvm-sh/nvm")
    assert page.count(v) == 3, (
        f"Expected 3 occurrences of {v} in the output, found {page.count(v)}"
    )
    tmp.cleanup()
    return result


if __name__ == "__main__":
    main()
