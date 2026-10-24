import logging

__IS_STYLER_AVAILABLE: bool = False

try:
	from .cli.text_styler import FastStyler, get_styled_text_from_html
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

		Message = super().format(record)

		match record.levelno:
			case logging.WARNING: Message = FastStyler(Message).colorize.yellow
			case logging.ERROR: Message = FastStyler(Message).colorize.red

		return Message

LOGS_HANDLER = logging.StreamHandler()

if __IS_STYLER_AVAILABLE:
	LOGS_HANDLER.setFormatter(ColorFormatter(get_styled_text_from_html("<b>[%(name)s]</b> %(levelname)s: %(message)s")))
else:
	LOGS_HANDLER.setFormatter(logging.Formatter("[%(name)s] %(levelname)s: %(message)s"))
