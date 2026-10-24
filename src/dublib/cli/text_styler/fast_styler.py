from .escapes import BackgroundColor, Color, Decoration, Drop

#==========================================================================================#
# >>>>> НАБОРЫ БЫСТРЫХ СТИЛИЗАТОРОВ <<<<< #
#==========================================================================================#

class Background:
	"""Набор быстрых фоновых цветов."""

	@property
	def black(self) -> str:
		"""Чёрный."""

		return f"{BackgroundColor.BLACK}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def red(self) -> str:
		"""Красный."""

		return f"{BackgroundColor.RED}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def green(self) -> str:
		"""Зелёный."""

		return f"{BackgroundColor.GREEN}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def yellow(self) -> str:
		"""Жёлтый."""

		return f"{BackgroundColor.YELLOW}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def blue(self) -> str:
		"""Синий."""

		return f"{BackgroundColor.BLUE}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def magenta(self) -> str:
		"""Фиолетовый."""

		return f"{BackgroundColor.MAGENTA}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def cyan(self) -> str:
		"""Бирюзовый."""

		return f"{BackgroundColor.CYAN}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	@property
	def white(self) -> str:
		"""Белый."""

		return f"{BackgroundColor.WHITE}{self.__Styler.plain_text}{Drop.DEFAULT_BACKGROUND}"

	def __init__(self, fast_styler: "FastStyler"):
		"""
		Набор быстрых фоновых цветов.

		:param fast_styler: Быстрый стилизатор.
		:type fast_styler: FastStyler
		"""

		self.__Styler = fast_styler

class Colorize:
	"""Набор быстрых цветов."""

	#==========================================================================================#
	# >>>>> БАЗОВЫЕ ЦВЕТА <<<<< #
	#==========================================================================================#

	@property
	def black(self) -> str:
		"""Чёрный."""

		return f"{Color.BLACK}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def red(self) -> str:
		"""Красный."""

		return f"{Color.RED}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def green(self) -> str:
		"""Зелёный."""

		return f"{Color.GREEN}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def yellow(self) -> str:
		"""Жёлтый."""

		return f"{Color.YELLOW}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def blue(self) -> str:
		"""Синий."""

		return f"{Color.BLUE}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def magenta(self) -> str:
		"""Фиолетовый."""

		return f"{Color.MAGENTA}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def cyan(self) -> str:
		"""Бирюзовый."""

		return f"{Color.CYAN}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def white(self) -> str:
		"""Белый."""

		return f"{Color.WHITE}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	#==========================================================================================#
	# >>>>> СВЕТЛЫЕ ОТТЕНКИ <<<<< #
	#==========================================================================================#

	@property
	def gray(self) -> str:
		"""Серый."""

		return f"{Color.GRAY}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_red(self) -> str:
		"""Светло-красный."""

		return f"{Color.BRIGHT_RED}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_green(self) -> str:
		"""Светло-зелёный."""

		return f"{Color.BRIGHT_GREEN}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_yellow(self) -> str:
		"""Светло-жёлтый."""

		return f"{Color.BRIGHT_YELLOW}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_blue(self) -> str:
		"""Светло-синий."""

		return f"{Color.BRIGHT_BLUE}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_magenta(self) -> str:
		"""Светло-фиолетовый."""

		return f"{Color.BRIGHT_MAGENTA}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_cyan(self) -> str:
		"""Светло-бирюзовый."""

		return f"{Color.BRIGHT_CYAN}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	@property
	def bright_white(self) -> str:
		"""Светло-белый."""

		return f"{Color.BRIGHT_WHITE}{self.__Styler.plain_text}{Drop.DEFAULT_COLOR}"

	#==========================================================================================#
	# >>>>> ПУБЛИЧНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(self, fast_styler: "FastStyler"):
		"""
		Набор быстрых цветов.

		:param fast_styler: Быстрый стилизатор.
		:type fast_styler: FastStyler
		"""

		self.__Styler = fast_styler

class Decorate:
	"""Набор быстрых декораций."""

	@property
	def bold(self) -> str:
		"""Полужирный."""

		return f"{Decoration.BOLD}{self.__Styler.plain_text}{Drop.DISABLE_BOLD}"

	@property
	def italic(self) -> str:
		"""Курсив."""

		return f"{Decoration.ITALIC}{self.__Styler.plain_text}{Drop.DISABLE_ITALIC}"

	@property
	def underlined(self) -> str:
		"""Подчёркнутый."""

		return f"{Decoration.UNDERLINED}{self.__Styler.plain_text}{Drop.DISABLE_UNDERLINED}"

	@property
	def blincked(self) -> str:
		"""Мигающий."""

		return f"{Decoration.BLINKING}{self.__Styler.plain_text}{Drop.DISABLE_BLINCKED}"

	@property
	def throughline(self) -> str:
		"""Перечёркнутый."""

		return f"{Decoration.THROUGHLINED}{self.__Styler.plain_text}{Drop.DISABLE_THROUGHLINED}"

	@property
	def double_underlined(self) -> str:
		"""Дважды подчёркнутый."""

		return f"{Decoration.DOUBLE_UNDERLINED}{self.__Styler.plain_text}{Drop.DISABLE_UNDERLINED}"

	@property
	def upperlined(self) -> str:
		"""Надчёркнутый."""

		return f"{Decoration.UPPERLINED}{self.__Styler.plain_text}{Drop.DISABLE_UPPERLINED}"

	def __init__(self, fast_styler: "FastStyler"):
		"""
		Набор быстрых декораций.

		:param fast_styler: Быстрый стилизатор.
		:type fast_styler: FastStyler
		"""

		self.__Styler = fast_styler

#==========================================================================================#
# >>>>> ОСНОВНЫЕ КЛАССЫ <<<<< #
#==========================================================================================#

class FastStyler:
	"""Быстрый стилизатор текста."""

	#==========================================================================================#
	# >>>>> СВОЙСТВА <<<<< #
	#==========================================================================================#

	@property
	def background(self) -> Background:
		"""Набор быстрых фоновых цветов."""

		return self.__Background

	@property
	def colorize(self) -> Colorize:
		"""Набор быстрых цветов."""

		return self.__Colorize

	@property
	def decorate(self) -> Decorate:
		"""Набор быстрых декораций."""

		return self.__Decorate

	@property
	def plain_text(self):
		"""Нестилизованный текст."""

		return self.__Text

	#==========================================================================================#
	# >>>>> ПУБЛИЧНЫЕ МЕТОДЫ <<<<< #
	#==========================================================================================#

	def __init__(self, text: str):
		"""
		Быстрый стилизатор текста.

		:param text: Стилизуемый текст.
		:type text: str
		"""

		self.__Text = text

		self.__Background = Background(self)
		self.__Colorize = Colorize(self)
		self.__Decorate = Decorate(self)
