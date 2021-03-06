# Stubs for django.utils.jslex (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class Tok:
    num: int = ...
    id: Any = ...
    name: Any = ...
    regex: Any = ...
    next: Any = ...
    def __init__(self, name, regex, next: Optional[Any] = ...) -> None: ...

def literals(choices, prefix: str = ..., suffix: str = ...): ...

class Lexer:
    regexes: Any = ...
    toks: Any = ...
    state: Any = ...
    def __init__(self, states, first) -> None: ...
    def lex(self, text): ...

class JsLexer(Lexer):
    both_before: Any = ...
    both_after: Any = ...
    states: Any = ...
    def __init__(self) -> None: ...

def prepare_js_for_gettext(js): ...
