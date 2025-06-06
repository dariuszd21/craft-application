# Copyright 2023-2024 Canonical Ltd.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""Configuration for craft-application documentation."""

import datetime

project = "Craft Application"
author = "Canonical Group Ltd"

copyright = f"2023-{datetime.date.today().year}, {author}"  # noqa: A001

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**venv",
    "base",
    "sphinx-resources",
    "common/README.md",
    "common/craft-application/how-to/build-remotely.rst",
    "common/craft-application/reference/remote-builds.rst",
]

# links to ignore when checking links
linkcheck_ignore = [
    # Ignore releases, since we'll include the next release before it exists.
    "https://github.com/canonical/[a-z]*craft[a-z-]*/releases/.*",
]

extensions = [
    "canonical_sphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxext.rediraffe",
    "pydantic_kitbash",
]

rst_epilog = """
.. include:: /reuse/links.txt
"""


# Canonical-sphinx
ogp_site_url = "https://canonical-craft-application.readthedocs-hosted.com/"
ogp_site_name = project

html_context = {
    "product_page": "github.com/canonical/craft-application",
    "github_url": "https://github.com/canonical/craft-application",
}

# Github config
github_username = "canonical"
github_repository = "craft-application"

intersphinx_mapping = {
    "craft-grammar": ("https://craft-grammar.readthedocs.io/en/latest", None),
    "craft-parts": (
        "https://canonical-craft-parts.readthedocs-hosted.com/en/latest",
        None,
    ),
    "craft-platforms": (
        "https://canonical-craft-platforms.readthedocs-hosted.com/en/latest",
        None,
    ),
}

# Client-side page redirects.
rediraffe_redirects = "redirects.txt"
