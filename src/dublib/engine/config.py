import asyncio
import logging
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from threading import Thread
from typing import TYPE_CHECKING

from watchfiles import awatch, watch

from ..core import LOGS_HANDLER
from ..exceptions.engine.config import AlreadyWatchingError

if TYPE_CHECKING:
	from pydantic_settings import BaseSettings

#==========================================================================================#
# >>>>> LOGGER INITIALIZATION <<<<< #
#==========================================================================================#

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(LOGS_HANDLER)
LOGGER.setLevel(logging.INFO)

#==========================================================================================#
# >>>>> DATA STRUCTS <<<<< #
#==========================================================================================#

@dataclass
class _Watcher:
	"""Source watcher data."""

	source: Path
	is_watching: bool = False
	task: asyncio.Task | None = None
	thread: Thread | None = None

#==========================================================================================#
# >>>>> MAIN CLASS <<<<< #
#==========================================================================================#

class Config[T: "BaseSettings"]:
	"""Dynamic config."""

	#==========================================================================================#
	# >>>>> PROPERTIES <<<<< #
	#==========================================================================================#

	@property
	def data(self) -> T:
		"""Config data."""

		return self.__data

	@property
	def sources(self) -> tuple[Path, ...]:
		"""Sources paths."""

		return self.__sources

	#==========================================================================================#
	# >>>>> PRIVATE METHODS <<<<< #
	#==========================================================================================#

	async def __watch_async(self, watcher: _Watcher):
		"""
		Watch source file for changes and reload config if edited.

		:param watcher: Source watcher data.
		:type watcher: _Watcher
		"""

		async for _ in awatch(watcher.source):
			if not watcher.is_watching: break
			await asyncio.to_thread(self.reload)
			LOGGER.info(f"Changes detected in source \"{watcher.source}\". Config reloaded.")

	def __watch(self, watcher: _Watcher):
		"""
		Watch source file for changes and reload config if edited.

		:param watcher: Source watcher data.
		:type watcher: _Watcher
		"""

		for _ in watch(watcher.source):
			if not watcher.is_watching: break
			self.reload()
			LOGGER.info(f"Changes detected in source \"{watcher.source}\". Config reloaded.")

		watcher.thread = None

	def __get_sources(self) -> tuple[Path, ...]:
		"""
		Get config sources.

		:return: Sources paths.
		:rtype: tuple[Path, ...]
		"""

		return tuple(
			Path(file)
			for key, file in self.__data.model_config.items()
			if key.endswith("_file") and isinstance(file, str)
		)

	def __get_watcher(self, source: PathLike[str] | str, check_is_watching: bool = True) -> _Watcher:
		"""
		Get config source watcher data.

		:param source: Config source.
		:type source: PathLike[str] | str
		:param check_is_watching: Check is already watching.
		:type check_is_watching: bool
		:return: Source watcher data.
		:rtype: _Watcher
		:raises AlreadyWatchingError: Config source already watching.
		:raises KeyError: Config source not defined in settings model.
		"""

		source = Path(source)
		watcher: _Watcher = self.__watchers[source]

		if check_is_watching:
			self.__is_already_watching(watcher)

		return watcher

	def __is_already_watching(self, watcher: _Watcher):
		"""
		Check is source already watcher.

		:param watcher: Source watcher data.
		:type watcher: _Watcher
		:raises AlreadyWatchingError: Config source already watching.
		"""

		if watcher.is_watching:
			raise AlreadyWatchingError(bool(watcher.task))

	def __load(self) -> T:
		"""
		Load config.

		:return: Config data.
		:rtype: T
		"""

		return self.__model()

	#==========================================================================================#
	# >>>>> SPECIAL METHODS <<<<< #
	#==========================================================================================#

	def __init__(self, model: type[T]):
		"""
		Dynamic config.

		Based on [pydantic-settings](https://github.com/pydantic/pydantic-settings) with sources files changes watchers.

		:param model: Settings model.
		:type model: type[BaseSettings]
		"""

		self.__model: type[T] = model

		self.__data: T = self.__load()
		self.__sources: tuple[Path, ...] = self.__get_sources()
		self.__watchers: dict[Path, _Watcher] = {source: _Watcher(source) for source in self.__sources}

	#==========================================================================================#
	# >>>>> PUBLIC SYNC METHODS <<<<< #
	#==========================================================================================#

	def is_source_watching(self, source: PathLike[str] | str) -> bool:
		"""
		Check is config source watching.

		:param source: Config source.
		:type source: PathLike[str] | str
		:return: `True` if config source watching.
		:rtype: bool
		"""

		return self.__get_watcher(source, check_is_watching = False).is_watching

	def reload(self):
		"""Reload config."""

		self.__data = self.__load()

	def stop_watching(self, source: PathLike[str] | str):
		"""
		Stop config source changes watching.

		Watching will be stopped at next config source changes.

		:param source: Config source.
		:type source: PathLike[str] | str
		:raises KeyError: Source not found in model.
		"""

		watcher: _Watcher = self.__get_watcher(source, check_is_watching = False)

		watcher.is_watching = False

		if watcher.task:
			watcher.task.cancel()

		watcher.task = None
		watcher.thread = None

		LOGGER.info(f"Source \"{watcher.source}\" watching stopped.")

	def stop_watching_all(self):
		"""
		Stop all config sources changes watching.

		Watching will be stopped at next config source changes.
		"""

		for source in self.__sources:
			self.stop_watching(source)

	def watch(self, source: PathLike[str] | str):
		"""
		Start config source changes watching.

		:param source: Config source.
		:type source: PathLike[str] | str
		"""

		watcher: _Watcher = self.__get_watcher(source)

		if watcher.thread and watcher.thread.is_alive():
			return

		watcher.is_watching = True
		watcher.thread = Thread(target = self.__watch, args = (watcher,))
		watcher.thread.start()

		LOGGER.info(f"Start to watching {watcher.source} source in thread.")

	def watch_all(self):
		"""Start all config sources changes watching."""

		for source in self.sources:
			self.watch(source)

	#==========================================================================================#
	# >>>>> PUBLIC ASYNC METHODS <<<<< #
	#==========================================================================================#

	async def watch_all_async(self):
		"""Start all config sources changes watching."""

		for source in self.sources:
			await self.watch_async(source)

	async def watch_async(self, source: PathLike[str] | str):
		"""
		Start config source changes watching.

		:param source: Config source.
		:type source: PathLike[str] | str
		"""

		watcher: _Watcher = self.__get_watcher(source)

		if watcher.task and not watcher.task.done():
			return

		watcher.is_watching = True
		watcher.task = asyncio.create_task(self.__watch_async(watcher))

		LOGGER.info(f"Start to watching \"{watcher.source}\" source asynchronously.")
