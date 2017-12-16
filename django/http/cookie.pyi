# Stubs for django.http.cookie (Python 3.5)

from typing import Dict
import http.cookies
from http.cookies import Morsel

cookie_pickles_properly = ...  # type: bool
SimpleCookie = ... # type: http.cookies.SimpleCookie

def parse_cookie(cookie: str) -> Dict[str, str]: ...
