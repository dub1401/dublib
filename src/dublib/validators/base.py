from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import PydanticCustomError, core_schema

from .exceptions import ConversionError, ValidationError

class BaseValidator[T](ABC):
	"""Base string validator."""

	#==========================================================================================#
	# >>>>> PYDANTIC INTERACTIONS <<<<< #
	#==========================================================================================#

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
	def __pydantic_validate(cls, value: Any, handler: core_schema.ValidatorFunctionWrapHandler) -> T:
		"""
		Validate value for [pydantic](https://github.com/pydantic/PYDANTIC).

		:param value: Validable value.
		:type value: Any
		:param handler: Validator function wrap handler.
		:type handler: ValidatorFunctionWrapHandler
		:return: Parsed value.
		:rtype: Any
		:raises PydanticCustomError: Validation error.
		"""

		try:
			return cls.parse(handler(value))
		except (ConversionError, ValidationError):
			raise PydanticCustomError("value_error", "Validation with dublib.validators failed.") from None

	#==========================================================================================#
	# >>>>> OVVERIDABLE METHODS <<<<< #
	#==========================================================================================#

	@classmethod
	def _export_fast_validation_state(cls) -> bool:
		"""
		Export fast validation state: skip validation if value already in target type.

		By default disabled for values types `str` and `pathlib.Path`.

		:return: Fast validation state.
		:rtype: bool
		"""

		if issubclass(cls._export_target_type(), Path | str):
			return False

		return True

	@staticmethod
	@abstractmethod
	def _export_target_type() -> type[T]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[T]
		"""

		pass

	@staticmethod
	@abstractmethod
	def _convert(value: Any) -> T:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: T
		"""

		pass

	@staticmethod
	@abstractmethod
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type .

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		pass

	#==========================================================================================#
	# >>>>> PUBLIC METHODS <<<<< #
	#==========================================================================================#

	@classmethod
	def convert(cls, value: Any) -> T:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: T
		:raises ConversionError: Unable convert value to target type.
		"""

		if isinstance(value, cls._export_target_type()):
			return value

		result = cls._convert(value)

		return result

	@classmethod
	def parse(cls, value: Any) -> T:
		"""
		Validate value and convert to target type.

		:param value: Parsable value.
		:type value: Any
		:return: Parsing result.
		:rtype: T
		:raises ValidationError: Validation error.
		"""

		if not cls.validate(value):
			raise ValidationError(value, cls)

		return cls.convert(value)

	@classmethod
	def validate(cls, value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		:param value: Validable value.
		:type value: str
		:return: `True` if value valid.
		:rtype: bool
		"""

		if cls._export_fast_validation_state() and isinstance(value, cls._export_target_type()):
			return True

		return cls._validate(value)
