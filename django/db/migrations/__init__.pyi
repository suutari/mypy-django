from .migration import Migration, swappable_dependency
# XXX: from .operations import *

from .operations.fields import AddField, AlterField, RemoveField, RenameField

from .operations.models import (
    AddIndex, AlterIndexTogether, AlterModelManagers, AlterModelOptions,
    AlterModelTable, AlterOrderWithRespectTo, AlterUniqueTogether, CreateModel,
    DeleteModel, RemoveIndex, RenameModel,
)
