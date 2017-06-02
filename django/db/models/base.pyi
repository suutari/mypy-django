from typing import Any, Type


class Deferred: ...


DEFERRED = Deferred()


class Model:
    # TODO:
    objects = ...  # type: Any
    DoesNotExist = ...  # type: Type[Exception]
