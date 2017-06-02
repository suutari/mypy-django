from .base import Operation

class FieldOperation(Operation):
    def __init__(self, model_name, name) -> None: ...

class AddField(FieldOperation):
    def __init__(self, model_name, name, field, preserve_default: bool = ...) -> None: ...

class RemoveField(FieldOperation):
    ...

class AlterField(FieldOperation):
    def __init__(self, model_name, name, field, preserve_default: bool = ...) -> None: ...

class RenameField(FieldOperation):
    def __init__(self, model_name, old_name, new_name) -> None: ...

