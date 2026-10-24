import inspect

from dublib.validators import ValidableTypes, types

def test_ValidableTypes():
	"""Check is all validators in `ValidableTypes` enumeration."""

	target_classes: tuple[type[object], ...] = tuple(
		cls
		for _, cls in inspect.getmembers(types, inspect.isclass)
		if cls.__module__ == types.__name__
	)

	enum_values: set[type] = {item.value for item in ValidableTypes}
	enum_names: set[str] = {item.name for item in ValidableTypes}

	for cls in target_classes:
		assert cls in enum_values
		assert cls.__name__ in enum_names
