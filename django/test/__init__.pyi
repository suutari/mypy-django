from typing import Dict, Any, TypeVar, Callable
import unittest

class TestCase(unittest.TestCase): ...

_T = TypeVar("_T")

def override_settings(**kwargs: Dict[str, Any]) -> Callable[[_T], _T]: ...
