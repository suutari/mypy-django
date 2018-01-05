# Stubs for django.utils.decorators (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class classonlymethod(classmethod):
    def __get__(self, instance, cls: Optional[Any] = ...): ...

def method_decorator(decorator, name: str = ...): ...
def decorator_from_middleware_with_args(middleware_class): ...
def decorator_from_middleware(middleware_class): ...
def available_attrs(fn): ...
def make_middleware_decorator(middleware_class): ...

class ContextDecorator:
    def __call__(self, func): ...

class classproperty:
    fget: Any = ...
    def __init__(self, method: Optional[Any] = ...) -> None: ...
    def __get__(self, instance, cls: Optional[Any] = ...): ...
    def getter(self, method): ...
