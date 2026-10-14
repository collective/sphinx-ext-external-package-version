# The latest stable version name of a GitHub repo is available in the docs
# through a special syntax: {{ version gh_owner/gh_repo_name }}.
# The version is found only at build time. For a given repo used in the docs,
# the latest version is found only once because we cache the version name.

import re

import requests

gh_version_cache = {}


def sub_replace_func(match):
    owner = match.group("owner")
    repo = match.group("repo")
    name = f"{owner}/{repo}"
    if name not in gh_version_cache:
        gh_version_cache[name] = latest_release_for_github_repo(name)
    return gh_version_cache[name]


sub_pattern = (
    r"(?<!\{\{)\{\{(\s*)version(\s+)(?P<owner>\S+)\/(?P<repo>\S+)(\s*)\}\}(?!\}\})"
)


def latest_gh_replace(app, docname, source):
    result = source[0]
    result = re.sub(sub_pattern, sub_replace_func, result)
    source[0] = result


def latest_gh_include_replace(app, relative_path, parent_docname, content):
    return latest_gh_replace(app, parent_docname, content)


def latest_release_for_github_repo(repo):
    latest_release_url = "https://api.github.com/repos/" + repo + "/releases/latest"
    try:
        response = requests.get(latest_release_url)
        response.raise_for_status()
        commit = response.json()
        return commit["name"]
    except requests.RequestException as e:
        print(f"GET request error: {e.response.status_code} - {e.response.reason}")


def setup(app):
    app.connect("source-read", latest_gh_replace)
    app.connect("include-read", latest_gh_include_replace)
    return {
        "version": "1.0.0",
    }
