# Validators
This module contains validators and converters set that can be used with [pydantic](https://github.com/pydantic/PYDANTIC) models.

## How to use
If fast validation enabled by validator, target type value validation is always true. In `convert()` accepts target type value it always returned value as it, without conversion.

```Python
from dublib.validators import types

types.Float.validate("1") # True
types.Float.validate("-2.66") # True

types.Float.convert(1) # 1.0
types.Float.convert("1") # 1.0
types.Float.convert("test") # Undefined behavior, no validation!

types.Float.parse("123") # 123.0
types.Float.parse("test") # ValidationError
```

## Custom validator
For custom validator creation define class ingerited from `BaseValidator` and specify generic type. Than override next methods. Method `parse()` uses `convert()` and `validate()` together, there are wrappers for protected `_convert()` and `_validate()`. 

```Python
# types.py
from collections.abc import Buffer
from typing import Any, SupportsIndex, SupportsInt, override

from dublib.validators.base import BaseValidator
from dublib.validators.exceptions import ConversionError

class Digit(BaseValidator[int]):
	"""Validator: digit."""

	@classmethod
	@override
	def _export_fast_validation_state(cls) -> bool:

		return False

	@staticmethod
	@override
	def _export_target_type() -> type[int]:

		return int

	@staticmethod
	@override
	def _convert(value: Any) -> int:

		if isinstance(value, str | Buffer | SupportsInt | SupportsIndex):
			return int(value)

		raise ConversionError(value, int)

	@staticmethod
	@override
	def _validate(value: Any) -> bool:

		if isinstance(value, str):
			return value.isdigit() and len(value) == 1

		if isinstance(value, int | Buffer | SupportsInt | SupportsIndex):
			return int(value) in range(0, 10)

		return False
```

## pydantic
Validators can be used with [pydantic](https://github.com/pydantic/PYDANTIC) models as annotated types.

```Python
from typing import Annotated

from pydantic import BaseModel

from dublib.validators import types

class Model(BaseModel):

	domain: Annotated[str, types.Domain]

```

## Terminalyzer
Module [Terminalyzer](./cli/terminalyzer.md) uses validators to parsing CLI parameters values.

```Python
# main.py
from dublib.cli.terminalyzer import Terminalyzer, Command
from dublib.validators import ValidableType

from . import types

class CustomValidableType(ValidableType):
	Digit = types.Digit

# Terminalyzer commands models groups initialization…

model.base.add_argument(CustomValidableType.Zero)
```

## Types
```{eval-rst}
.. automodule:: dublib.validators.types
	:members:
```