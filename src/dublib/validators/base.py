from abc import ABC, abstractmethod
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import PydanticCustomError, core_schema

from ..exceptions.validators import ValidationError

class BaseValidator[T](ABC):
	"""Base string validator."""

	@classmethod
	def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
		"""
		Generate [pydantic](https://github.com/pydantic/PYDANTIC) core schema.

		:param source_type: Source type.
		:type source_type: Any
		:param handler: Handler getter.
		:type handler: GetCoreSchemaHandler
		:return: Schema.
		:rtype: core_schema.CoreSchema
		"""

		return core_schema.no_info_wrap_validator_function(
			cls.__pydantic_validate,
			handler(str),
		)

	@classmethod
	def __pydantic_validate(cls, value: str, handler: core_schema.ValidatorFunctionWrapHandler) -> T:
		"""
		Validate value for [pydantic](https://github.com/pydantic/PYDANTIC).

		:param value: Validable value.
		:type value: str
		:param handler: Validator function wrap handler.
		:type handler: ValidatorFunctionWrapHandler
		:return: Parsed value.
		:rtype: Any
		:raises PydanticCustomError: Validation error.
		"""

		try:
			return cls.parse(handler(value))
		except ValidationError:
			raise PydanticCustomError("value_error", "Validation with dublib.validators failed.")

	@staticmethod
	@abstractmethod
	def convert(value: str) -> T:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		pass

	@classmethod
	def parse(cls, value: str) -> T:
		"""
		Validate string and convert to target type.

		:param value: Parsable string.
		:type value: str
		:return: Parsing result.
		:rtype: T
		:raises ValidationError: Validation error.
		"""

		if not cls.validate(value):
			raise ValidationError(value, cls)

		return cls.convert(value)

	@staticmethod
	@abstractmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		pass
