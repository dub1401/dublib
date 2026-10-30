import functools
from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound = Callable[..., Any])

def run_before_method(method_name: str)-> Callable[[F], F]:
	"""
	Декоратор: запускает публичный или защищённый метод, не принимающий аргументов, перед выполнением метода экземпляра класса. Запущенный метод имеет доступ к экземпляру.

	:param method_name: Имя метода.
	:type method_name: str
	"""

	if method_name.startswith("__"):
		raise ValueError("Only public and protected methods supported in @run_before_method decorator.")

	def decorator(function: F):

		@functools.wraps(function)
		def wrapper(*args, **kwargs):
			if args:
				Object = args[0]
				Method = getattr(Object, method_name, None)
				if Method and callable(Method):
					Method()

			return function(*args, **kwargs)

		return wrapper

	return decorator
