from typing import Callable, Any, Dict

class Operation:
    ...

_MigrationCode = Callable[[Any, Any], None]

class RunPython:
    def __init__(
        self, code: _MigrationCode, reverse_code: _MigrationCode = None,
        atomic: bool = None, hints: Dict = None, elidable: bool = False
    ) -> None: ...
    
    noop: _MigrationCode
