from .generator import generate_message
from .types import MessageType

def print_message(text: str, message_type: MessageType | None = None, origin: str | None = None):
	"""
	Print styled message in terminal.

	:param text: Message text.
	:type text: str
	:param message_type: Message type.
	:type message_type: MessageType | None
	:param origin: Message origin.
	:type origin: str | None
	"""

	print(generate_message(text, message_type, origin))

def print_debug(text: str, origin: str | None = None):
	"""
	Print styled **debug** message in terminal.

	:param text: Message text.
	:type text: str
	:param origin: Message origin.
	:type origin: str | None
	"""

	print_message(text, message_type = MessageType.Debug, origin = origin)

def print_info(text: str, origin: str | None = None):
	"""
	Print styled **info** message in terminal.

	:param text: Message text.
	:type text: str
	:param origin: Message origin.
	:type origin: str | None
	"""

	print_message(text, message_type = MessageType.Info, origin = origin)

def print_warning(text: str, origin: str | None = None):
	"""
	Print styled **warning** message in terminal.

	:param text: Message text.
	:type text: str
	:param origin: Message origin.
	:type origin: str | None
	"""

	print_message(text, message_type = MessageType.Warning, origin = origin)

def print_error(text: str, origin: str | None = None):
	"""
	Print styled **error** message in terminal.

	:param text: Message text.
	:type text: str
	:param origin: Message origin.
	:type origin: str | None
	"""

	print_message(text, message_type = MessageType.Error, origin = origin)

def print_critical(text: str, origin: str | None = None):
	"""
	Print styled **critical** message in terminal.

	:param text: Message text.
	:type text: str
	:param origin: Message origin.
	:type origin: str | None
	"""

	print_message(text, message_type = MessageType.Critical, origin = origin)
