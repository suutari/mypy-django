# Stubs for django.http.cookie (Python 3.5)

from http.cookies import Morsel as Morsel
from http.cookies import SimpleCookie as SimpleCookie
from typing import Dict

cookie_pickles_properly = ...  # type: bool


def parse_cookie(cookie: str) -> Dict[str, str]: ...


__all__ = [
    'Morsel',
    'parse_cookie',
    'SimpleCookie',
]
