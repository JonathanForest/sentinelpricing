
import hashlib
import importlib.resources
import os

from abc import ABC, abstractmethod
from functools import partialmethod
from typing import IO, Any, Optional


class ModuleFile(ABC):
    """
    Context manager for opening a resource file from a package.

    This class abstracts the details of opening a file resource using
    importlib.resources. It supports opening the file in either text or
    binary mode, and is intended to be used with a "with" statement.

    Strictly speaking this is only necessary when using Sentinel Frameworks
    in modules that you intend to share, as it removes the need to know exactly
    where the file is stored.

    Attributes:
        package: The package that contains the resource.
        name: The name of the resource file.
        mode: The file mode ("t" for text or "b" for binary).
    """

    def __init__(
        self,
        package: Any,
        name: str,
        mode: str = "text",
        expected_md5: str = None
        ) -> None:
        """
        Initialize the ModuleFile context manager.

        Args:
            package: The package where the resource file is located.
            name: The name of the resource file.
            mode: The mode to open the file. Accepts "text" or "t" for text
                mode, and "binary" or "b" for binary mode. Defaults to "text".

        Raises:
            ValueError: If an invalid mode is provided.
        """
        self.package = package
        self.name = name

        self.file: Optional[IO] = None

        if self.expected_md5:
            self.validate_md5(expected_md5)

    def __enter__(self) -> IO:
        """
        Open the resource file and return the file object.

        The file is opened using the appropriate importlib.resources function
        based on the mode specified at initialization.

        Returns:
            A file-like object opened in the specified mode.
        """

        self.file = self.open()

        if self._file is None:
            raise FileNotFoundError()

        return self._file

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Close the resource file upon exiting the context.

        Args:
            exc_type: The exception type, if an exception occurred.
            exc_value: The exception value, if an exception occurred.
            traceback: The traceback, if an exception occurred.
        """
        if self._file is not None:
            self._file.close()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def validate_md5(self, expected_md5):
        pass

class ModuleTextFile(ModuleFile):
    def open(self, **kwargs):
        return importlib.resources.open_text(
                self.package, path, encoding="utf-8", **kwargs
            )

    def open_as_binary(self):
        return importlib.resources.open_binary(
                package, path
            )

    def validate_md5(self, expected_md5):
        with self.open_as_binary() as f:
            if MD5Checker(file) != self.expected_md5:
                raise RuntimeError("")


class ModuleBinaryFile(ModuleFile):
    def open(self):
        return importlib.resources.open_binary(
                package, path
            )

    def validate_md5(self, expected_md5):
        with self as f:
            if MD5Checker(file) != self.expected_md5:
                raise RuntimeError("")