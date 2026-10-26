import os
import sys
import tomllib
from typing import Any

import commonmark
from sphinx.application import Sphinx

work_dir: str = os.path.abspath("..")
lib_data: dict[str, Any] | None = None
readme_copyright_years: str | None = None

sys.path.insert(0, os.path.abspath("../src"))

with open(f"{work_dir}/pyproject.toml", "rb") as reader:
	lib_data = tomllib.load(reader)

with open(f"{work_dir}/README.md", encoding = "utf-8") as reader:
	readme_copyright_years = reader.readlines()[-1].strip().split()[-1].rstrip("_.")

project = "dublib"
copyright = f"{readme_copyright_years}, dub1401"  # noqa: A001
author = "dub1401"
release = lib_data["project"]["version"]

extensions = [
	"myst_parser",
	"sphinx.ext.autodoc",
	"sphinx.ext.viewcode",
]

source_suffix = {
	".md": "markdown",
	".rst": "restructuredtext",
}

templates_path = ['_templates']
exclude_patterns = [
	"README.md",
]

html_theme = "sphinx_rtd_theme"

# Render Markdown docstrings into reStructuredText.
def _docstring(app: Sphinx, what: str, name: str, obj: Any, options: dict[str, Any], lines: list[str]):  # noqa: ARG001

	md: str = "\n".join(lines)
	ast = commonmark.Parser().parse(md)
	rst: str = commonmark.ReStructuredTextRenderer().render(ast)
	lines.clear()
	lines.extend(rst.splitlines())

def setup(app: Sphinx):

	app.connect("autodoc-process-docstring", _docstring)
