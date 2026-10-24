from typing import Any

class ConversionError(Exception):
	"""Exception: unable convert value to target type."""

	def __init__(self, value: Any, target_type: type):
		"""
		Exception: unable convert value to target type.

		:param value: Conversible value.
		:type value: Any
		:param target_type: Target type.
		:type target_type: type
		"""

		super().__init__(f"Unable convert {value} to {target_type.__name__} type.")

class ValidationError(Exception):
	"""Exception: unable safely parse value."""

	def __init__(self, value: Any, target_type: type):
		"""
		Exception: unable safely parse value.

		:param value: Parsable value.
		:type value: Any
		:param target_type: Target type.
		:type target_type: type
		"""

		super().__init__(f"Unable safely parse {value} to {target_type.__name__} type.")
