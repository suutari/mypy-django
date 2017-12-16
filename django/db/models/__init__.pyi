from typing import Any, Type

from django.db.models.deletion import (
    CASCADE as CASCADE, DO_NOTHING as DO_NOTHING, PROTECT as PROTECT, SET as SET, SET_DEFAULT as SET_DEFAULT, SET_NULL as SET_NULL, ProtectedError as ProtectedError,
)

from django.db.models.fields import *


from django.db.models.base import DEFERRED as DEFERRED
from django.db.models.fields.related import (
    ForeignKey as ForeignKey, ForeignObject as ForeignObject,
    # OneToOneField as OneToOneField, ManyToManyField as ManyToManyField,
    # ManyToOneRel as ManyToOneRel, ManyToManyRel as ManyToManyRel, OneToOneRel as OneToOneRel,
)


class Model:
    # TODO:
    objects = ...  # type: Any
    DoesNotExist = ...  # type: Type[Exception]
