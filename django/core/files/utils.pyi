from typing import Any, Iterable, List, Optional, Tuple, Union


class FileProxyMixin:
    encoding: str
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    newlines: Union[str, Tuple[str, ...], None]
    def read(self, n: int = ...) -> bytes: ...
    def readinto(self, b: Any) -> Optional[int]: ...
    def readline(self, limit: int = -1) -> bytes: ...
    def readlines(self, hint: int = -1) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = 0) -> int: ...
    def tell(self) -> int: ...
    def truncate(self, size: Optional[int] = ...) -> int: ...
    def write(self, s: Union[bytes, bytearray]) -> int: ...
    def writelines(self, lines: List[bytes]) -> None: ...
    def closed(self) -> bool: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def __iter__(self) -> Iterable[bytes]: ...
    def __next__(self) -> bytes: ...
