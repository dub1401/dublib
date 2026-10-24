from types import MappingProxyType

from ..text_styler import TextStyler, codes
from .types import MessageType

__COLORS: MappingProxyType[MessageType | None, codes.Colors | None] = MappingProxyType({
	MessageType.Debug: codes.Colors.Gray,
	MessageType.Info: codes.Colors.White,
	MessageType.Error: codes.Colors.Red,
	MessageType.Warning: codes.Colors.Yellow,
	MessageType.Critical: codes.Colors.Red,
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

	return TextStyler(text_color = __COLORS[message_type]).get_styled_text(message)
