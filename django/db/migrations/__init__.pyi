from .migration import Migration, swappable_dependency  # NOQA
from .operations import *  # NOQA


from .operations import (
    AddIndex, AlterIndexTogether, AlterModelManagers, AlterModelOptions,
    AlterModelTable, AlterOrderWithRespectTo, AlterUniqueTogether, CreateModel,
    DeleteModel, RemoveIndex, RenameModel,
)
