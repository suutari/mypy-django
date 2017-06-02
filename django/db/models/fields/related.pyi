from typing import Any, Optional

from . import Field

class RelatedField(Field): ...

class ForeignObject(RelatedField):
    def __init__(
            self,
            to,
            on_delete,
            from_fields,
            to_fields,
            rel: Optional[Any] = ...,
            related_name: Optional[Any] = ...,
            related_query_name: Optional[Any] = ...,
            limit_choices_to: Optional[Any] = ...,
            parent_link: bool = ...,
            swappable: bool = ...,
            **kwargs
    ) -> None: ...

class ForeignKey(ForeignObject):
    def __init__(
            self,
            to,
            on_delete: Optional[Any] = ...,
            related_name: Optional[Any] = ...,
            related_query_name: Optional[Any] = ...,
            limit_choices_to: Optional[Any] = ...,
            parent_link: bool = ...,
            to_field: Optional[Any] = ...,
            db_constraint: bool = ...,
            **kwargs
    ) -> None: ...
