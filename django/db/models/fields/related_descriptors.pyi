# Stubs for django.db.models.fields.related_descriptors (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ForwardManyToOneDescriptor:
    field: Any = ...
    cache_name: Any = ...
    def __init__(self, field_with_rel) -> None: ...
    def RelatedObjectDoesNotExist(self): ...
    def is_cached(self, instance): ...
    def get_queryset(self, **hints): ...
    def get_prefetch_queryset(self, instances, queryset: Optional[Any] = ...): ...
    def get_object(self, instance): ...
    def __get__(self, instance, cls: Optional[Any] = ...): ...
    def __set__(self, instance, value): ...

class ForwardOneToOneDescriptor(ForwardManyToOneDescriptor):
    def get_object(self, instance): ...

class ReverseOneToOneDescriptor:
    related: Any = ...
    cache_name: Any = ...
    def __init__(self, related) -> None: ...
    def RelatedObjectDoesNotExist(self): ...
    def is_cached(self, instance): ...
    def get_queryset(self, **hints): ...
    def get_prefetch_queryset(self, instances, queryset: Optional[Any] = ...): ...
    def __get__(self, instance, cls: Optional[Any] = ...): ...
    def __set__(self, instance, value): ...

class ReverseManyToOneDescriptor:
    rel: Any = ...
    field: Any = ...
    def __init__(self, rel) -> None: ...
    def related_manager_cls(self): ...
    def __get__(self, instance, cls: Optional[Any] = ...): ...
    def __set__(self, instance, value): ...

def create_reverse_many_to_one_manager(superclass, rel): ...

class ManyToManyDescriptor(ReverseManyToOneDescriptor):
    reverse: Any = ...
    def __init__(self, rel, reverse: bool = ...) -> None: ...
    @property
    def through(self): ...
    def related_manager_cls(self): ...

def create_forward_many_to_many_manager(superclass, rel, reverse): ...