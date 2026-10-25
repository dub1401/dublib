from types import MappingProxyType

from dublib.cli.text_styler import TextStyler

from .types import MessageType

__COLORS: MappingProxyType[MessageType | None, str | None] = MappingProxyType({
	MessageType.Debug: "gray",
	MessageType.Info: "white",
	MessageType.Error: "red",
	MessageType.Warning: "yellow",
	MessageType.Critical: "red",
	None: None,
})

def generate_message(text: str, message_type: MessageType | None = None, origin: str | None = None, colorize: bool = True) -> str:
	"""
	Generate styled message.

	:param text: Message text.
	:type text: str
	:param message_type: Message type.
	:type message_type: MessageType | None
	:param origin: Message origin.
	:type origin: str | None
	:return: Styled message in format: `[{ORIGIN}:{TYPE}] {MESSAGE}`.
	:rtype: str
	"""

	origin_part: str = origin or ""
	type_part: str = message_type.name.lower() if message_type else ""
	separator: str = ":" if origin_part and type_part else ""

	message: str = f"{type_part}{separator}{origin_part}"

	if message:
		if message_type: message = f"[{message}]"
		text = f" {text}"

	message += text

	if not colorize:
		return message

	color: str | None = __COLORS[message_type]

	if not color:
		return message

	return TextStyler().convert(f"[{color}]{message}[/{color}]")
