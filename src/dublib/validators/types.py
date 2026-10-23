from datetime import datetime
from pathlib import Path as PathlibPath
from typing import cast, override

import dateparser
import validators
from pathvalidate import is_valid_filepath

from .base import BaseValidator

class All(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return True

class Alpha(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return value.isalpha()

class Base64(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			Result = validators.base64(value)
			if type(Result) is bool: return Result
		except validators.ValidationError: pass

		return False

class Bool(BaseValidator[bool]):

	@override
	@staticmethod
	def convert(value: str) -> bool:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: bool
		"""

		value = value.lower()
		if value in ("true",): return True

		return False

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		Buffer = value.lower()

		return Buffer in ("true", "false")

class Datetime(BaseValidator[datetime]):

	@override
	@staticmethod
	def convert(value: str) -> datetime:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: datetime
		"""

		return cast("datetime", dateparser.parse(value))

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			dateparser.parse(value)
			return True
		except (ValueError, TypeError): pass

		return False

class Domain(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			Result = validators.domain(value)
			if type(Result) is bool: return Result
		except validators.ValidationError: pass

		return False

class Email(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			Result = validators.email(value)
			if type(Result) is bool: return Result
		except validators.ValidationError: pass

		return False

class Float(BaseValidator[float]):

	@override
	@staticmethod
	def convert(value: str) -> float:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: float
		"""

		return float(value)

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return value.count("-") <= 1 and value.count(".") == 1 and value.replace(".", "").lstrip("-").isdigit()

class Integer(BaseValidator[int]):

	@override
	@staticmethod
	def convert(value: str) -> int:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: int
		"""

		return int(value)

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return value.count("-") <= 1 and value.lstrip("-").isdigit()

class IPv4(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			Result = validators.ipv4(value)
			if type(Result) is bool: return Result
		except validators.ValidationError: pass

		return False

class IPv6(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) -> str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			Result = validators.ipv6(value)
			if type(Result) is bool: return Result
		except validators.ValidationError: pass

		return False

class Number(BaseValidator[float | int]):

	@override
	@staticmethod
	def convert(value: str) -> float | int:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: float | int
		"""

		return float(value) if "." in value else int(value)

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		if "." in value:
			try:
				float(value)
				return True
			except ValueError: return False

		else:
			try:
				int(value)
				return True
			except ValueError: return False

class Path(BaseValidator[PathlibPath]):

	@override
	@staticmethod
	def convert(value: str) ->  PathlibPath:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: pathlib.Path
		"""

		return PathlibPath(value)

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return is_valid_filepath(value)

class UnsignedInteger(BaseValidator[int]):

	@override
	@staticmethod
	def convert(value: str) ->  int:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: int
		"""

		return int(value)

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return value.isdigit()

class URL(BaseValidator[str]):

	@override
	@staticmethod
	def convert(value: str) ->  str:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: T
		"""

		return value

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		try:
			Result = validators.url(value)
			if type(Result) is bool: return Result
		except validators.ValidationError: pass

		return False

class ValidPath(BaseValidator[PathlibPath]):

	@override
	@staticmethod
	def convert(value: str) ->  PathlibPath:
		"""
		Convert value into target type without validation.

		:param value: Convertible string.
		:type value: str
		:return: Conversion result.
		:rtype: pathlib.Path
		"""

		return PathlibPath(value)

	@override
	@staticmethod
	def validate(value: str) -> bool:
		"""
		Validate is string can be converted into target type.

		:param value: Validable string.
		:type value: str
		:return: `True` if string valid.
		:rtype: bool
		"""

		return PathlibPath(value).exists()
