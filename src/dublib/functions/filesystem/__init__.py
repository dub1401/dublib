import os
import random
import shutil
import tempfile
from collections.abc import Sequence
from os import PathLike
from pathlib import Path

from ..data import to_sequence

def atomic_write(path: PathLike[str] | str, data: bytes):
	"""
	Atomary wtite file by temporary file and `shutil.move()` using.

	Args:
		path (PathLike[str] | str): Path to file.
		data (bytes): Binary data.
	"""

	path = Path(path)
	temp_path: Path | None = None

	try:
		with tempfile.NamedTemporaryFile("wb", delete = False, dir = path.parent) as temp_writer:
			temp_path = Path(temp_writer.name)
			temp_writer.write(data)
			temp_writer.flush()
			os.fsync(temp_writer.fileno())

		os.replace(temp_path, path)

	except Exception:
		if temp_path:
			temp_path.unlink(missing_ok = True)
		raise

def get_random_file(directory: PathLike[str] | str) -> Path | None:
	"""
	Выбирает случайный файл из директории.

	:param directory: Путь к директории.
	:type directory: PathLike[str] | str
	:return: Путь к случайному файлу в директории или `None`, если таковая пуста.
	:rtype: Path
	:raises FileNotFoundError: Директория не существует.
	"""

	DirectoryPath = Path(directory)
	Files = os.listdir(DirectoryPath)
	if not Files: return None
	FilePath = DirectoryPath / random.choice(Files)

	return FilePath

def make_cwd_directories(directories: str | Sequence[str]):
	"""
	Создаёт наборы каталогов в текущей корневой директории скрипта.

	:param directories: Последовательность названий директорий или название конкретной директории.
	:type directories: str | Sequence[str]
	"""

	for Name in to_sequence(directories):
		os.makedirs(Name, exist_ok = True)

def clear_directory(directory: PathLike[str] | str):
	"""
	Удлаляет содержимое директории.

	:param directory: Путь к директории.
	:type directory: PathLike[str] | str
	"""

	DirectoryPath = Path(directory)
	shutil.rmtree(DirectoryPath)
	DirectoryPath.mkdir()
