from collections.abc import Callable
from types import MappingProxyType
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from rich.console import Console
from rich.style import Style
from rich.table import Table

if TYPE_CHECKING:
	from collections.abc import Sequence

_CONSOLE = Console()

_HTML_TAGS_STYLES: MappingProxyType[str, str] = MappingProxyType({
	"b": "bold",
	"strong": "bold",

	"i": "italic",
	"em": "italic",

	"s": "strike",
	"del": "strike",
	"ins": "strike",
	"strike": "strike",

	"u": "underline",
	"underline": "underline",
})

class TextStyler:
	"""Text styler. Provides [Rich](https://github.com/Textualize/rich) markup into ANSI-styled string conversion and HTML-Rich-ANSI conversion."""

	#==========================================================================================#
	# >>>>> PROPERTIES <<<<< #
	#==========================================================================================#

	@property
	def console(self) -> Console:
		"""Rich console."""

		return _CONSOLE

	#==========================================================================================#
	# >>>>> PRIVATE METHODS <<<<< #
	#==========================================================================================#

	def __extract_rich_styles(self, style: "str | Sequence[str]") -> tuple[str, ...]:
		"""
		Extract Rich styles.

		:param style: Style attribute value.
		:type style: str | Sequence[str]
		:return: Rich styles.
		:rtype: tuple[str, ...]
		"""

		if type(style) is not str:
			style = "".join(style)

		if not style:
			return ()

		rich_styles: list[str] = []
		styles: list[str] = [s.strip() for s in style.split(";") if s.strip()]

		for style in styles:

			if ":" not in style:
				continue

			name, value = map(str.strip, style.split(":", 1))
			name = name.lower()
			value = value.lower()

			match name:

				case "color":
					rich_styles.append(value)

				case "font-weight":
					if value == "bold":
						rich_styles.append("bold")

				case "font-style":
					if value == "italic":
						rich_styles.append("italic")

		return tuple(rich_styles)

	def __parse_style(self, style: "Sequence[str] | str | Style") -> Style:
		"""
		Parse Rich style.

		:param style: Rich style one or several tags.
		:type style: Sequence[str] | str | Style
		:return: Rich style.
		:rtype: Style
		"""

		if isinstance(style, Style):
			return style

		if type(style) is str:
			return Style.parse(style)

		return Style.parse(" ".join(style))

	def __process_node(self, node: PageElement) -> str:
		"""
		Process HTML node into Rich format.

		:param node: HTML node.
		:type node: PageElement
		:return: Processed text.
		:rtype: str
		"""

		if isinstance(node, NavigableString):
			return node.string.replace("[", "\\[")

		if not isinstance(node, Tag):
			return ""

		inner_content: str = "".join(self.__process_node(child) for child in node.children)
		rich_styles: set[str] = set()

		if node.name in _HTML_TAGS_STYLES:
			rich_styles.add(_HTML_TAGS_STYLES[node.name])

		if node.name == "a" and node.has_attr("href"):
			url: str = str(node["href"])
			rich_styles.add(f"link={url}")

		if node.has_attr("style"):
			attr_styles: tuple[str, ...] = self.__extract_rich_styles(node["style"])
			rich_styles.update(attr_styles)

		if rich_styles:
			rich_open_tag_styles: set[str] = rich_styles
			rich_close_tag_styles: set[str] = {style.split("=")[0] for style in rich_styles}

			rich_open_tag: str = " ".join(rich_open_tag_styles)
			rich_close_tag: str = " ".join(rich_close_tag_styles)

			return f"[{rich_open_tag}]{inner_content}[/{rich_close_tag}]"

		return inner_content

	#==========================================================================================#
	# >>>>> PUBLIC METHODS <<<<< #
	#==========================================================================================#

	def convert(self, text: str) -> str:
		"""
		Convert text with Rich markup to ANSI-styled text.

		:param text: Text with markup.
		:type text: str
		:return: ANSI-styled text.
		:rtype: str
		"""

		with self.console.capture() as capture:
			self.console.print(text, end = "")

		return capture.get()

	def convert_from_html(self, text: str) -> str:
		"""
		Convert HTML to ANSI-styled text.

		:param text: HTML,
		:type text: str
		:return: ANSI-styled text.
		:rtype: str
		"""

		text = self.html_to_rich(text)

		return self.convert(text)

	def convert_table(self, table: Table) -> str:
		"""
		Convert Rich table to ANSI-styled text.

		:param text: Rich table.
		:type text: Table
		:return: ANSI-styled text.
		:rtype: str
		"""

		with self.console.capture() as capture:
			self.console.print(table, end = "")

		return capture.get().rstrip("\n")

	def html_to_rich(self, text: str) -> str:
		"""
		Convert HTML to Rich markup.

		Supported prestyled tags: `b`, `i`, `s`, `u` (and its semantic versions).

		Supported functional tags: `a`.

		Supported styles: `color`, `font-weight`, `font-style`.

		:param text: HTML.
		:type text: str
		:return: Text in Rich markup.
		:rtype: str
		"""

		soup = BeautifulSoup(text, "html.parser")

		return "".join(
			self.__process_node(child)
			for child in soup.children
		)

	def make_preset(self, style: "Sequence[str] | str | Style") -> Callable[[str], str]:
		"""
		Make style preset for fast templated stylization.

		:param style: Rich style.
		:type style: Sequence[str] | str | Style
		:return: Lambda-preset, that accepts raw string.
		:rtype: Callable[[str], str]
		"""

		style = self.__parse_style(style)

		return lambda text: self.richify(text, style)

	def richify(self, text: str, style: "Sequence[str] | str | Style") -> str:
		"""
		Generate ANSI-styled text with style.

		:param text: Text for stilization.
		:type text: str
		:param style: Rich style.
		:type style: Sequence[str] | str | rich.style.Style
		:return: Stylized text.
		:rtype: str
		"""

		style = self.__parse_style(style)

		with self.console.capture() as capture:
			self.console.print(text, style = style, end = "")

		return capture.get()
