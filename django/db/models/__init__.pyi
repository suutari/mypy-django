from typing import Any, Type

from django.db.models.deletion import (
    CASCADE, DO_NOTHING, PROTECT, SET, SET_DEFAULT, SET_NULL, ProtectedError,
)

from django.db.models.fields import *


from django.db.models.base import DEFERRED
from django.db.models.fields.related import (
    ForeignKey, ForeignObject,
    # OneToOneField, ManyToManyField,
    # ManyToOneRel, ManyToManyRel, OneToOneRel,
)


class Model:
    # TODO:
    objects = ...  # type: Any
    DoesNotExist = ...  # type: Type[Exception]
