class AlreadyWatchingError(Exception):
	"""Exception: config source already watching."""

	def __init__(self, is_async_watcher: bool):
		"""
		Exception: config source already watching.

		:param is_async_watcher: Is watcher runnd asynchronously.
		:type is_async_watcher: bool
		"""

		super().__init__("Async watcher detected." if is_async_watcher else "Thread watcher detected.")
