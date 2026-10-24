from datetime import datetime
from pathlib import Path

from packaging.specifiers import SpecifierSet
from packaging.version import Version

SUPPORTED_TYPES = bool | datetime | float | int | Path | SpecifierSet | str | Version
