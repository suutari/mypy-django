from typing import Any

# Remove warnings when importing django.db, happens in migrations
db = None # type: Any

def setup(set_prefix: bool = True) -> None: ...

def get_version(version: Tuple = None) -> str: ...