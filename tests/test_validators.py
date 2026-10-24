import inspect
import sys
from datetime import datetime
from pathlib import Path

from packaging.version import Version

from dublib.validators import ValidableTypes, types

def test_All():

	assert types.All.validate("") is True
	assert types.All.convert("") == ""

def test_Alpha():

	assert types.Alpha.validate("en") is True
	assert types.Alpha.validate("ру") is True
	assert types.Alpha.validate("en2") is False
	assert types.Alpha.convert("en") == "en"

def test_Base64():

	assert types.Base64.validate("YWJj") is True
	assert types.Base64.validate("QQ==") is True
	assert types.Base64.validate("YWJjX") is False
	assert types.Base64.validate("QQ=~") is False
	assert types.Base64.convert("YWJj") == "YWJj"


def test_Bool():

	assert types.Bool.validate("trUe") is True
	assert types.Bool.validate("faLse") is True
	assert types.Bool.convert("truE") is True
	assert types.Bool.convert("faLse") is False

def test_Datetime():

	assert types.Datetime.validate("2026-01-01") is True
	assert types.Datetime.validate("2026 13 32") is False
	assert types.Datetime.convert("2026-1-1") == datetime(2026, 1, 1)

def test_Domain():

	assert types.Domain.validate("www.example.com") is True
	assert types.Domain.validate("https://example.com") is False
	assert types.Domain.validate("examplecom") is False
	assert types.Domain.convert("example.com") == "example.com"

def test_Email():

	assert types.Email.validate("test123.mailbox@mailbox.com") is True
	assert types.Email.validate("test@mailbox") is False
	assert types.Email.convert("test123.mailbox@mailbox.com") == "test123.mailbox@mailbox.com"

def test_ExistingDirPath(tmp_path: Path):

	tmp_file: Path = tmp_path / "test.txt"
	tmp_file_str: str = tmp_file.as_posix()
	tmp_file.touch()
	tmp_dir: Path = tmp_path / "test"
	tmp_dir_str: str = tmp_dir.as_posix()
	tmp_dir.mkdir()

	assert types.ExistingDirPath.validate(tmp_file_str) is False
	assert types.ExistingDirPath.validate(tmp_dir_str) is True
	assert types.ExistingDirPath.validate("missing_file.txt") is False
	assert types.ExistingDirPath.validate("missing_dir") is False
	assert types.ExistingDirPath.convert(tmp_dir_str) == tmp_dir

def test_ExistingFilePath(tmp_path: Path):

	tmp_file: Path = tmp_path / "test.txt"
	tmp_file_str: str = tmp_file.as_posix()
	tmp_file.touch()
	tmp_dir: Path = tmp_path / "test"
	tmp_dir_str: str = tmp_dir.as_posix()
	tmp_dir.mkdir()

	assert types.ExistingFilePath.validate(tmp_file_str) is True
	assert types.ExistingFilePath.validate(tmp_dir_str) is False
	assert types.ExistingFilePath.validate("missing_file.txt") is False
	assert types.ExistingFilePath.validate("missing_dir") is False
	assert types.ExistingFilePath.convert(tmp_file_str) == tmp_file

def test_ExistingPath(tmp_path: Path):

	tmp_file: Path = tmp_path / "test.txt"
	tmp_file_str: str = tmp_file.as_posix()
	tmp_file.touch()
	tmp_dir: Path = tmp_path / "test"
	tmp_dir_str: str = tmp_dir.as_posix()
	tmp_dir.mkdir()

	assert types.ExistingPath.validate(tmp_file_str) is True
	assert types.ExistingPath.validate(tmp_dir_str) is True
	assert types.ExistingPath.validate("missing_file.txt") is False
	assert types.ExistingPath.validate("missing_dir") is False
	assert types.ExistingPath.convert(tmp_file_str) == tmp_file
	assert types.ExistingPath.convert(tmp_dir_str) == tmp_dir

def test_Float():

	assert types.Float.validate("1.0") is True
	assert types.Float.validate("1.") is False
	assert types.Float.validate(".1") is False
	assert types.Float.validate("1") is False
	assert types.Float.convert("1.2") == 1.2

def test_Integer():

	assert types.Integer.validate("1") is True
	assert types.Integer.validate("1.0") is False
	assert types.Integer.convert("1") == 1

def test_IPv4():

	assert types.IPv4.validate("192.168.1.1") is True
	assert types.IPv4.validate("256.100.0.1") is False
	assert types.IPv4.convert("192.168.1.1") == "192.168.1.1"

def test_IPv6():

	assert types.IPv6.validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") is True
	assert types.IPv6.validate("2001:0db8:85a3:0000:0000:g82e:0370:7334") is False
	assert types.IPv6.convert("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

def test_Number():

	assert types.Number.validate("1") is True
	assert types.Number.validate("-1") is True
	assert types.Number.validate("1.2") is True
	assert types.Number.validate("-1.2") is True
	assert types.Number.convert("0") == 0
	assert types.Number.convert("-1") == -1
	assert types.Number.convert("1.2") == 1.2
	assert types.Number.convert("-1.2") == -1.2

def test_Path():

	assert types.Path.validate(".") is True
	assert types.Path.validate("/etc") is True
	assert types.Path.validate("/etc/") is True
	assert types.Path.validate("dir") is True

	if sys.platform == "win32":
		assert types.Path.validate("dir:ro") is False
	else:
		assert types.Path.validate("dir:ro") is True

	assert types.Path.convert("") == Path("")
	assert types.Path.convert("dir/") == Path("dir")

def test_UnsignedInteger():

	assert types.UnsignedInteger.validate("1") is True
	assert types.UnsignedInteger.validate("-1") is False
	assert types.UnsignedInteger.validate("1.0") is False
	assert types.UnsignedInteger.validate("-1.0") is False
	assert types.UnsignedInteger.convert("1") == 1

def test_URL():

	assert types.URL.validate("https://www.example.com") is True
	assert types.URL.validate("file:///run/text.txt") is True
	assert types.URL.validate("example.com") is False
	assert types.URL.convert("https://www.example.com") == "https://www.example.com"

def test_Version():

	assert types.Version.validate("v1.0.0-rc.1") is True
	assert types.Version.validate("2026.01.01") is True
	assert types.Version.validate("1..0") is False
	assert types.Version.convert("v1.0.0-rc.1") == Version("1.0.0rc1")

def test_VersionsRange():

	assert types.VersionsRange.validate("<v1.0.0-rc.1") is True
	assert types.VersionsRange.validate(">2026.01.01") is True
	assert types.VersionsRange.validate(">=1.0,<1.1") is True
	assert types.VersionsRange.validate(">=1.0;<1.1") is False
	assert types.VersionsRange.validate(">=1..0;<1.1") is False
	assert Version("v1.0.99") in types.VersionsRange.convert(">=1.0,<1.1")

def test_ValidableTypes():
	"""Check is all validators in `ValidableTypes` enumeration."""

	target_classes: tuple[type[object], ...] = tuple(
		cls
		for _, cls in inspect.getmembers(types, inspect.isclass)
		if cls.__module__ == types.__name__
	)

	enum_values: set[type] = {item.value for item in ValidableTypes}

	for cls in target_classes:
		assert cls in enum_values
