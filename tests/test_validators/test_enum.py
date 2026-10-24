import inspect

from dublib.validators import ValidableType, types

def test_ValidableType():
	"""Check is all validators in `ValidableType` enumeration."""

	target_classes: tuple[type[object], ...] = tuple(
		cls
		for _, cls in inspect.getmembers(types, inspect.isclass)
		if cls.__module__ == types.__name__
	)

	enum_values: set[type] = {item.value for item in ValidableType}
	enum_names: set[str] = {item.name for item in ValidableType}

	for cls in target_classes:
		assert cls in enum_values
		assert cls.__name__ in enum_names
