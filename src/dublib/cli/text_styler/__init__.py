from collections.abc import Sequence
from types import MappingProxyType
from typing import cast

from ...functions.data import to_sequence
from . import codes, escapes
from .fast_styler import FastStyler as FastStyler

#==========================================================================================#
# >>>>> СТИЛИЗАЦИЯ ИЗ HTML <<<<< #
#==========================================================================================#

__SUPPORTED_TAGS = MappingProxyType({
	"b": (escapes.Decoration.BOLD, escapes.Drop.DISABLE_BOLD),
	"i": (escapes.Decoration.ITALIC, escapes.Drop.DISABLE_ITALIC),
	"u": (escapes.Decoration.UNDERLINED, escapes.Drop.DISABLE_UNDERLINED),
	"s": (escapes.Decoration.THROUGHLINED, escapes.Drop.DISABLE_THROUGHLINED),
})

def get_styled_text_from_html(text: str) -> str:
	"""
	Преобразовывает теги HTML в управляющие последовательности ANSI.

	Поддерживаемые теги: `b`, `i`, `u`, `s`.

	:param text: Стилизуемый текст.
	:type text: str
	:return: Стилизованный текст.
	:rtype: str
	"""

	for Tag in __SUPPORTED_TAGS.keys():
		text = text.replace(f"<{Tag}>", __SUPPORTED_TAGS[Tag][0])
		text = text.replace(f"</{Tag}>", __SUPPORTED_TAGS[Tag][1])

	return text

#==========================================================================================#
# >>>>> ОСНОВНОЙ КЛАСС <<<<< #
#==========================================================================================#

class TextStyler:
	"""Стилизатор текста."""

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	@property
	def decorations(self) -> tuple[codes.Decoration, ...] | None:
		"""Набор кодов декораций."""

		return self.__Decorations

	@property
	def text_color(self) -> codes.Color | None:
		"""Код цвета текста."""

		return self.__TextColor

	@property
	def background_color(self) -> codes.BackgroundColor | None:
		"""Код цвета фона."""

		return self.__BackgroundColor

	@property
	def is_autoreset(self) -> bool:
		"""Состояние переключателя: нужно ли добавлять последовательность сброса стилей в конец строки."""

		return self.__Autoreset

	#==========================================================================================#
	# >>>>> ПУБЛИЧНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(
			self,
			decorations: codes.Decoration | Sequence[codes.Decoration] | None = None,
			text_color: codes.Color | None = None,
			background_color: codes.BackgroundColor | None = None,
			autoreset: bool = True,
		):
		"""
		Стилизатор текста.

		:param decorations: Код декорации или набор кодов декораций.
		:type decorations: Codes.Decorations | Sequence[Codes.Decorations] | None
		:param text_color: Код цвета текста.
		:type text_color: Codes.Colors | None
		:param background_color: Код цвета фона.
		:type background_color: Codes.BackgroundsColors | None
		:param autoreset: Указывает, нужно ли добавить последовательность сброса стилей в конец строки.
		:type autoreset: bool
		"""

		self.__Decorations: tuple[codes.Decoration, ...] | None = cast("tuple[codes.Decoration, ...]", to_sequence(decorations)) if decorations else None
		self.__TextColor = text_color
		self.__BackgroundColor = background_color
		self.__Autoreset = autoreset

	def build_ansi_escape(self, codes: Sequence[codes.BackgroundColor | codes.Color | codes.Decoration | codes.Drop]) -> str:
		"""
		Строит управляющую последовательность из кодов.

		:param codes: Код ANSI или набор кодов из предоставляемых перечислений.
		:type codes: Sequence[Codes.BackgroundsColors | Codes.Colors | Codes.Decorations | Codes.Drops]
		:return: Управляющая последовательность.
		:rtype: str
		"""

		CodesStrings: tuple[str, ...] = tuple(str(Element.value) for Element in codes)
		CodesString = ";".join(CodesStrings)

		return f"\033[{CodesString}m"

	def get_styled_text(self, text: str) -> str:
		"""
		Возвращает стилизованный с помощью управляющих последовательностей ANSI текст, используя заданные в объекте стили.

		:param text: Стилизуемый текст.
		:type text: str
		:return: Стилизованный текст.
		:rtype: str
		"""

		Codes: list = []
		if self.__Decorations: Codes.extend(self.__Decorations)
		if self.__TextColor: Codes.append(self.__TextColor)
		if self.__BackgroundColor: Codes.append(self.__BackgroundColor)

		text = self.build_ansi_escape(Codes) + text
		if self.__Autoreset: text += escapes.Drop.RESET

		return text

	#==========================================================================================#
	# >>>>> МЕТОДЫ УСТАНОВКИ СТИЛЕЙ <<<<< #
	#==========================================================================================#

	def set_decorations(self, decorations: codes.Decoration | Sequence[codes.Decoration] | None):
		"""
		Задаёт декорации.

		:param decorations: Код декорации или набор кодов декораций.
		:type decorations: Codes.Decorations | Sequence[Codes.Decorations] | None
		"""

		self.__Decorations = cast("tuple[codes.Decoration, ...]", to_sequence(decorations)) if decorations else None

	def set_text_color(self, text_color: codes.Color | None):
		"""
		Задаёт цвет текста.

		:param text_color: Код цвета текста.
		:type text_color: Codes.Colors | None
		"""

		self.__TextColor = text_color

	def set_background_color(self, background_color: codes.BackgroundColor | None):
		"""
		Задаёт цвет фона.

		:param background_color: Код цвета фона.
		:type background_color: Codes.BackgroundsColors | None
		"""

		self.__BackgroundColor = background_color

	def enable_autoreset(self, status: bool):
		"""
		Переключает добавление последовательности сброса стилей в конец строки.

		:param status: Статус добавления последовательности.
		:type status: bool
		"""

		self.__Autoreset = status
