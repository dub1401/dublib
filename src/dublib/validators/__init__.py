from enum import Enum

from . import types

class ValidableType(Enum):
	"""Validable type."""

	Any = types.Any
	Alpha = types.Alpha
	Base64 = types.Base64
	Bool = types.Bool
	Datetime = types.Datetime
	Domain = types.Domain
	Email = types.Email
	ExistingDirPath = types.ExistingDirPath
	ExistingFilePath = types.ExistingFilePath
	ExistingPath = types.ExistingPath
	Float = types.Float
	Integer = types.Integer
	IPv4 = types.IPv4
	IPv6 = types.IPv6
	Path = types.Path
	UnsignedInteger = types.UnsignedInteger
	URL = types.URL
	Version = types.Version
	VersionsRange = types.VersionsRange
