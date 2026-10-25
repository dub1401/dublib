from dataclasses import dataclass

from .codes import BackgroundColor as _BackgroundColorsCode
from .codes import Color as _ColorCode
from .codes import Decoration as _DecorationCode
from .codes import Drop as _DropCode

@dataclass(frozen = True)
class Drop:
	"""Drop ANSI escape sequence."""

	RESET: str = f"\033[{_DropCode.RESET.value}m"

	DEFAULT_COLOR: str = f"\033[{_DropCode.DEFAULT_COLOR.value}m"
	DEFAULT_BACKGROUND: str = f"\033[{_DropCode.DEFAULT_BACKGROUND.value}m"

	DISABLE_BOLD: str = f"\033[{_DropCode.DISABLE_BOLD.value}m"
	DISABLE_ITALIC: str = f"\033[{_DropCode.DISABLE_ITALIC.value}m"
	DISABLE_UNDERLINED: str = f"\033[{_DropCode.DISABLE_UNDERLINED.value}m"
	DISABLE_BLINCKED: str = f"\033[{_DropCode.DISABLE_BLINCKED.value}m"
	DISABLE_THROUGHLINED: str = f"\033[{_DropCode.DISABLE_THROUGHLINED.value}m"
	DISABLE_UPPERLINED: str = f"\033[{_DropCode.DISABLE_UPPERLINED.value}m"

@dataclass(frozen = True)
class Color:
	"""Color ANSI escape sequence."""

	BLACK: str = f"\033[{_ColorCode.BLACK.value}m"
	RED: str = f"\033[{_ColorCode.RED.value}m"
	GREEN: str = f"\033[{_ColorCode.GREEN.value}m"
	YELLOW: str = f"\033[{_ColorCode.YELLOW.value}m"
	BLUE: str = f"\033[{_ColorCode.BLUE.value}m"
	MAGENTA: str = f"\033[{_ColorCode.MAGENTA.value}m"
	CYAN: str = f"\033[{_ColorCode.CYAN.value}m"
	WHITE: str = f"\033[{_ColorCode.WHITE.value}m"
	GRAY: str = f"\033[{_ColorCode.GRAY.value}m"
	BRIGHT_RED: str = f"\033[{_ColorCode.BRIGHT_RED.value}m"
	BRIGHT_GREEN: str = f"\033[{_ColorCode.BRIGHT_GREEN.value}m"
	BRIGHT_YELLOW: str = f"\033[{_ColorCode.BRIGHT_YELLOW.value}m"
	BRIGHT_BLUE: str = f"\033[{_ColorCode.BRIGHT_BLUE.value}m"
	BRIGHT_MAGENTA: str = f"\033[{_ColorCode.BRIGHT_MAGENTA.value}m"
	BRIGHT_CYAN: str = f"\033[{_ColorCode.BRIGHT_CYAN.value}m"
	BRIGHT_WHITE: str = f"\033[{_ColorCode.BRIGHT_WHITE.value}m"

@dataclass(frozen = True)
class BackgroundColor:
	"""Background color ANSI escape sequence."""

	BLACK: str = f"\033[{_BackgroundColorsCode.BLACK.value}m"
	RED: str = f"\033[{_BackgroundColorsCode.RED.value}m"
	GREEN: str = f"\033[{_BackgroundColorsCode.GREEN.value}m"
	YELLOW: str = f"\033[{_BackgroundColorsCode.YELLOW.value}m"
	BLUE: str = f"\033[{_BackgroundColorsCode.BLUE.value}m"
	MAGENTA: str = f"\033[{_BackgroundColorsCode.MAGENTA.value}m"
	CYAN: str = f"\033[{_BackgroundColorsCode.CYAN.value}m"
	WHITE: str = f"\033[{_BackgroundColorsCode.WHITE.value}m"
	GRAY: str = f"\033[{_BackgroundColorsCode.GRAY.value}m"
	BRIGHT_RED: str = f"\033[{_BackgroundColorsCode.BRIGHT_RED.value}m"
	BRIGHT_GREEN: str = f"\033[{_BackgroundColorsCode.BRIGHT_GREEN.value}m"
	BRIGHT_YELLOW: str = f"\033[{_BackgroundColorsCode.BRIGHT_YELLOW.value}m"
	BRIGHT_BLUE: str = f"\033[{_BackgroundColorsCode.BRIGHT_BLUE.value}m"
	BRIGHT_MAGENTA: str = f"\033[{_BackgroundColorsCode.BRIGHT_MAGENTA.value}m"
	BRIGHT_CYAN: str = f"\033[{_BackgroundColorsCode.BRIGHT_CYAN.value}m"
	BRIGHT_WHITE: str = f"\033[{_BackgroundColorsCode.BRIGHT_WHITE.value}m"

@dataclass(frozen = True)
class Decoration:
	"""Набор управляющих последовательностей декораций ANSI."""

	BOLD: str = f"\033[{_DecorationCode.BOLD.value}m"
	ITALIC: str = f"\033[{_DecorationCode.ITALIC.value}m"
	UNDERLINED: str = f"\033[{_DecorationCode.UNDERLINED.value}m"
	BLINKING: str = f"\033[{_DecorationCode.BLINKING.value}m"
	THROUGHLINED: str = f"\033[{_DecorationCode.THROUGHLINED.value}m"
	DOUBLE_UNDERLINED: str = f"\033[{_DecorationCode.DOUBLE_UNDERLINED.value}m"
	UPPERLINED: str = f"\033[{_DecorationCode.UPPERLINED.value}m"
