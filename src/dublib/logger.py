import logging

__IS_STYLER_AVAILABLE: bool = False

try:
	from .cli.text_styler import TextStyler
	__IS_STYLER_AVAILABLE = True
except ImportError:
	pass

class ColorFormatter(logging.Formatter):
	"""Форматировщик вывода в консоль с поддержкой цветов."""

	def format(self, record: logging.LogRecord) -> str:
		"""
		Форматирует записи с поддержкой цветной палитры.

		:param record: Запись лога.
		:type record: LogRecord
		:return: Текст сообщения.
		:rtype: str
		"""

		styler: TextStyler = TextStyler()
		message: str = super().format(record)

		message = styler.convert(message)

		match record.levelno:
			case logging.WARNING: message = styler.convert(f"[yellow]{message}[/yellow]")
			case logging.ERROR: message = styler.convert(f"[red]{message}[/red]")

		return message

LOGS_HANDLER = logging.StreamHandler()

if __IS_STYLER_AVAILABLE:
	LOGS_HANDLER.setFormatter(ColorFormatter("[bold][%(name)s][/bold] %(levelname)s: %(message)s"))
else:
	LOGS_HANDLER.setFormatter(logging.Formatter("[%(name)s] %(levelname)s: %(message)s"))
