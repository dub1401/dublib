from enum import Enum

class MessageType(Enum):
	"""Messages type."""

	Debug = "debug"
	Info = "info"
	Warning = "warning"
	Error = "error"
	Critical = "critical"
