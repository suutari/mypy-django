from typing import Any, Tuple, Union

# Remove warnings when importing django.db, happens in migrations
db = None # type: Any

def setup(set_prefix: bool = True) -> None: ...

def get_version(version: Tuple[Union[int, str]] = None) -> str: ...
