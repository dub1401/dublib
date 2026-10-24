import sys
from collections.abc import Buffer
from datetime import datetime
from pathlib import Path as PathlibPath
from typing import Any, SupportsFloat, SupportsIndex, SupportsInt, override

import dateparser
import validators
from packaging import specifiers, version
from pathvalidate import is_valid_filepath

from .base import BaseValidator
from .exceptions import ConversionError

class Any(BaseValidator[Any]):
	"""Validator: any value."""

	@staticmethod
	@override
	def _export_target_type() -> type[Any]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[Any]
		"""

		return Any

	@staticmethod
	@override
	def _convert(value: Any) -> Any:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: Any
		"""

		return value

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		return True

	# Overridden to annotate same type returned as passed.
	@classmethod
	def convert[T](cls, value: T) -> T:
		"""
		Convert value into target type without validation.

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: T
		"""

		return cls._convert(value)

class Alpha(BaseValidator[str]):
	"""Validator: string that contains only alpha characters."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		return isinstance(value, str) and value.isalpha()

class Base64(BaseValidator[str]):
	"""Validator: string in Base64 encoding."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		result: bool | None = None

		try:
			result = validators.base64(value)
		except validators.ValidationError:
			pass

		return bool(result)

class Bool(BaseValidator[bool]):
	"""Validator: boolean value or case-insensitive strings `true`, `false`."""

	@staticmethod
	@override
	def _export_target_type() -> type[bool]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[bool]
		"""

		return bool

	@staticmethod
	@override
	def _convert(value: Any) -> bool:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: bool
		"""

		if isinstance(value, str):
			buffer = value.lower()
			if buffer in ("true",): return True
			return False

		return bool(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, str):
			buffer = value.lower()
			return buffer in ("true", "false")

		return False

class Datetime(BaseValidator[datetime]):
	"""Validator: datetime or interpritable string."""

	@staticmethod
	@override
	def _export_target_type() -> type[datetime]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[datetime]
		"""

		return datetime

	@staticmethod
	@override
	def _convert(value: Any) -> datetime:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: datetime
		"""

		if isinstance(value, str):
			buffer = dateparser.parse(value)

			if buffer:
				return buffer

		elif isinstance(value, int | float):
			return datetime.fromtimestamp(value)

		raise ConversionError(value, datetime)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, datetime):
			return True

		if isinstance(value, str):
			try:
				return bool(dateparser.parse(value))
			except (ValueError, TypeError):
				pass

		return False

class Domain(BaseValidator[str]):
	"""Validator: domain."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		result: bool | None = None

		try:
			result = validators.domain(value)
		except validators.ValidationError:
			pass

		return bool(result)

class Email(BaseValidator[str]):
	"""Validator: email."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		result: bool | None = None

		try:
			result = validators.email(value)
		except validators.ValidationError:
			pass

		return bool(result)

class ExistingDirPath(BaseValidator[PathlibPath]):
	"""Validator: existing directory path."""

	@staticmethod
	@override
	def _export_target_type() -> type[PathlibPath]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[Path]
		"""

		return PathlibPath

	@staticmethod
	@override
	def _convert(value: Any) -> PathlibPath:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: Path
		"""

		if isinstance(value, str):
			return PathlibPath(value)

		raise ConversionError(value, PathlibPath)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, PathlibPath | str):
			path = PathlibPath(value)
			return path.exists() and path.is_dir()

		return False

class ExistingFilePath(BaseValidator[PathlibPath]):
	"""Validator: existing file path."""

	@staticmethod
	@override
	def _export_target_type() -> type[PathlibPath]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[Path]
		"""

		return PathlibPath

	@staticmethod
	@override
	def _convert(value: Any) -> PathlibPath:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: Path
		"""

		if isinstance(value, str):
			return PathlibPath(value)

		raise ConversionError(value, PathlibPath)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, PathlibPath | str):
			path = PathlibPath(value)
			return path.exists() and path.is_file()

		return False

class ExistingPath(BaseValidator[PathlibPath]):
	"""Validator: existing path."""

	@staticmethod
	@override
	def _export_target_type() -> type[PathlibPath]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[Path]
		"""

		return PathlibPath

	@staticmethod
	@override
	def _convert(value: Any) -> PathlibPath:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: Path
		"""

		if isinstance(value, str):
			return PathlibPath(value)

		raise ConversionError(value, PathlibPath)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, PathlibPath | str):
			path = PathlibPath(value)
			return path.exists()

		return False

class Float(BaseValidator[float]):
	"""Validator: float."""

	@staticmethod
	@override
	def _export_target_type() -> type[float]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[float]
		"""

		return float

	@staticmethod
	@override
	def _convert(value: Any) -> float:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: float
		"""

		if isinstance(value, str | Buffer | SupportsFloat | SupportsIndex):
			return float(value)

		raise ConversionError(value, float)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, str):
			buffer = value.strip(".")

			return all((
				buffer.count("-") <= 1,
				buffer.count(".") == 1,
				buffer.replace(".", "").lstrip("-").isdigit(),
			))

		if isinstance(value, int):
			return True

		return False

class Integer(BaseValidator[int]):
	"""Validator: integer."""

	@staticmethod
	@override
	def _export_target_type() -> type[int]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[int]
		"""

		return int

	@staticmethod
	@override
	def _convert(value: Any) -> int:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: int
		"""

		if isinstance(value, str | Buffer | SupportsInt | SupportsIndex):
			return int(value)

		raise ConversionError(value, int)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, str):
			return value.count("-") <= 1 and value.lstrip("-").isdigit()

		if isinstance(value, Buffer | SupportsInt | SupportsIndex):
			return True

		return False

class IPv4(BaseValidator[str]):
	"""Validator: IPv4."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		result: bool | None = None

		try:
			result = validators.ipv4(value)
		except validators.ValidationError:
			pass

		return bool(result)

class IPv6(BaseValidator[str]):
	"""Validator: IPv6."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		result: bool | None = None

		try:
			result = validators.ipv6(value)
		except validators.ValidationError:
			pass

		return bool(result)

class Path(BaseValidator[PathlibPath]):
	"""Validator: path."""

	@classmethod
	@override
	def _export_fast_validation_state(cls) -> bool:
		"""
		Export fast validation state: skip validation if value already in target type.

		By default disabled for values types `str` and `pathlib.Path`.

		:return: Fast validation state.
		:rtype: bool
		"""

		return True

	@staticmethod
	@override
	def _export_target_type() -> type[PathlibPath]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[Path]
		"""

		return PathlibPath

	@staticmethod
	@override
	def _convert(value: Any) -> PathlibPath:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: Path
		"""

		if isinstance(value, str):
			return PathlibPath(value)

		raise ConversionError(value, PathlibPath)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, PathlibPath):
			return True

		if isinstance(value, str):
			return is_valid_filepath(value, platform = sys.platform)

		return False

class UnsignedInteger(BaseValidator[int]):
	"""Validator: unsigned integer."""

	@classmethod
	@override
	def _export_fast_validation_state(cls) -> bool:
		"""
		Export fast validation state: skip validation if value already in target type.

		By default disabled for values types `str` and `pathlib.Path`.

		:return: Fast validation state.
		:rtype: bool
		"""

		return False

	@staticmethod
	@override
	def _export_target_type() -> type[int]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[int]
		"""

		return int

	@staticmethod
	@override
	def _convert(value: Any) -> int:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: int
		"""

		if isinstance(value, str | Buffer | SupportsInt | SupportsIndex):
			return int(value)

		raise ConversionError(value, int)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, str):
			return value.isdigit()

		if isinstance(value, Buffer | SupportsInt | SupportsIndex):
			return int(value) >= 0

		if isinstance(value, int):
			return value >= 0

		return False

class URL(BaseValidator[str]):
	"""Validator: URL."""

	@staticmethod
	@override
	def _export_target_type() -> type[str]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[str]
		"""

		return str

	@staticmethod
	@override
	def _convert(value: Any) -> str:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: str
		"""

		return str(value)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		result: bool | None = None

		try:
			result = validators.url(value)
		except validators.ValidationError:
			pass

		return bool(result)

class Version(BaseValidator[version.Version]):
	"""Validator: version."""

	@staticmethod
	@override
	def _export_target_type() -> type[version.Version]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[version.Version]
		"""

		return version.Version

	@staticmethod
	@override
	def _convert(value: Any) -> version.Version:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: version.Version
		"""

		if isinstance(value, str):
			return version.Version(value)

		raise ConversionError(value, version.Version)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, str):
			try:
				version.Version(value)
				return True
			except version.InvalidVersion:
				return False

		return False

class VersionsRange(BaseValidator[specifiers.SpecifierSet]):
	"""Validator: versions range."""

	@staticmethod
	@override
	def _export_target_type() -> type[specifiers.SpecifierSet]:
		"""
		Export target type.

		:return: Target type.
		:rtype: type[specifiers.SpecifierSet]
		"""

		return specifiers.SpecifierSet

	@staticmethod
	@override
	def _convert(value: Any) -> specifiers.SpecifierSet:
		"""
		Convert value into target type without validation. Can raise `ConversionError`.

		Value can't be of the target type, because instance checked on public method wrapper!

		:param value: Convertible value.
		:type value: Any
		:return: Conversion result.
		:rtype: specifiers.SpecifierSet
		"""

		if isinstance(value, str):
			return specifiers.SpecifierSet(value)

		raise ConversionError(value, specifiers.SpecifierSet)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:
		"""
		Validate is value can be converted into target type without data losses.

		Value can't be of the target type if target type is `str`!

		:param value: Validable value.
		:type value: Any
		:return: `True` if value valid.
		:rtype: bool
		"""

		if isinstance(value, str):
			try:
				specifiers.SpecifierSet(value)
				return True
			except specifiers.InvalidSpecifier:
				return False

		return False
