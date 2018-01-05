# Stubs for django.db.models.fields (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist
from django.db.models.query_utils import RegisterLookupMixin
from typing import Any, Optional

class Empty: ...
class NOT_PROVIDED: ...

BLANK_CHOICE_DASH: Any

class Field(RegisterLookupMixin):
    empty_strings_allowed: bool = ...
    empty_values: Any = ...
    creation_counter: int = ...
    auto_creation_counter: int = ...
    default_validators: Any = ...
    default_error_messages: Any = ...
    system_check_deprecated_details: Any = ...
    system_check_removed_details: Any = ...
    hidden: bool = ...
    many_to_many: Any = ...
    many_to_one: Any = ...
    one_to_many: Any = ...
    one_to_one: Any = ...
    related_model: Any = ...
    description: Any = ...
    name: Any = ...
    verbose_name: Any = ...
    primary_key: Any = ...
    remote_field: Any = ...
    is_relation: Any = ...
    default: Any = ...
    editable: Any = ...
    serialize: Any = ...
    unique_for_date: Any = ...
    unique_for_month: Any = ...
    unique_for_year: Any = ...
    choices: Any = ...
    help_text: Any = ...
    db_index: Any = ...
    db_column: Any = ...
    db_tablespace: Any = ...
    auto_created: Any = ...
    error_messages: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., primary_key: bool = ..., max_length: Optional[Any] = ..., unique: bool = ..., blank: bool = ..., null: bool = ..., db_index: bool = ..., rel: Optional[Any] = ..., default: Any = ..., editable: bool = ..., serialize: bool = ..., unique_for_date: Optional[Any] = ..., unique_for_month: Optional[Any] = ..., unique_for_year: Optional[Any] = ..., choices: Optional[Any] = ..., help_text: str = ..., db_column: Optional[Any] = ..., db_tablespace: Optional[Any] = ..., auto_created: bool = ..., validators: Any = ..., error_messages: Optional[Any] = ...) -> None: ...
    def check(self, **kwargs): ...
    @property
    def rel(self): ...
    def get_col(self, alias, output_field: Optional[Any] = ...): ...
    def cached_col(self): ...
    def select_format(self, compiler, sql, params): ...
    def deconstruct(self): ...
    def clone(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __deepcopy__(self, memodict): ...
    def __copy__(self): ...
    def __reduce__(self): ...
    def get_pk_value_on_save(self, instance): ...
    def to_python(self, value): ...
    def validators(self): ...
    def run_validators(self, value): ...
    def validate(self, value, model_instance): ...
    def clean(self, value, model_instance): ...
    def db_check(self, connection): ...
    def db_type(self, connection): ...
    def rel_db_type(self, connection): ...
    def db_parameters(self, connection): ...
    def db_type_suffix(self, connection): ...
    def get_db_converters(self, connection): ...
    @property
    def unique(self): ...
    concrete: Any = ...
    def set_attributes_from_name(self, name): ...
    model: Any = ...
    def contribute_to_class(self, cls, name, private_only: bool = ...): ...
    # def contribute_to_class(self, cls, name, private_only: bool = ..., virtual_only: Any = ...): ...
    # This commented out signature is the real signature. I couldn't get mypy
    # to unify the child implementations with the parent one, so for now this
    # hack'll suffice.
    def get_filter_kwargs_for_object(self, obj): ...
    def get_attname(self): ...
    def get_attname_column(self): ...
    def get_cache_name(self): ...
    def get_internal_type(self): ...
    def pre_save(self, model_instance, add): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def get_db_prep_save(self, value, connection): ...
    def has_default(self): ...
    def get_default(self): ...
    def get_choices(self, include_blank: bool = ..., blank_choice: Any = ..., limit_choices_to: Optional[Any] = ...): ...
    def value_to_string(self, obj): ...
    flatchoices: Any = ...
    def save_form_data(self, instance, data): ...
    def formfield(self, form_class: Optional[Any] = ..., choices_form_class: Optional[Any] = ..., **kwargs): ...
    def value_from_object(self, obj): ...

class AutoField(Field):
    description: Any = ...
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def rel_db_type(self, connection): ...
    def validate(self, value, model_instance): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def get_prep_value(self, value): ...
    def contribute_to_class(self, cls, name, **kwargs): ...
    def formfield(self, **kwargs): ...

class BigAutoField(AutoField):
    description: Any = ...
    def get_internal_type(self): ...
    def rel_db_type(self, connection): ...

class BooleanField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class CharField(Field):
    description: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class CommaSeparatedIntegerField(CharField):
    default_validators: Any = ...
    description: Any = ...
    system_check_deprecated_details: Any = ...
    def formfield(self, **kwargs): ...

class DateTimeCheckMixin:
    def check(self, **kwargs): ...

class DateField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., auto_now: bool = ..., auto_now_add: bool = ..., **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def pre_save(self, model_instance, add): ...
    def contribute_to_class(self, cls, name, **kwargs): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class DateTimeField(DateField):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def pre_save(self, model_instance, add): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class DecimalField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., max_digits: Optional[Any] = ..., decimal_places: Optional[Any] = ..., **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def validators(self): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def format_number(self, value): ...
    def get_db_prep_save(self, value, connection): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class DurationField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def get_db_converters(self, connection): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class EmailField(CharField):
    default_validators: Any = ...
    description: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs): ...

class FilePathField(Field):
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., path: str = ..., match: Optional[Any] = ..., recursive: bool = ..., allow_files: bool = ..., allow_folders: bool = ..., **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...
    def get_internal_type(self): ...

class FloatField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_prep_value(self, value): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def formfield(self, **kwargs): ...

class IntegerField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def check(self, **kwargs): ...
    def validators(self): ...
    def get_prep_value(self, value): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def formfield(self, **kwargs): ...

class BigIntegerField(IntegerField):
    empty_strings_allowed: bool = ...
    description: Any = ...
    MAX_BIGINT: int = ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class IPAddressField(Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    system_check_removed_details: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_prep_value(self, value): ...
    def get_internal_type(self): ...

class GenericIPAddressField(Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    default_error_messages: Any = ...
    unpack_ipv4: Any = ...
    protocol: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., protocol: str = ..., unpack_ipv4: bool = ..., *args, **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class NullBooleanField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class PositiveIntegerRelDbTypeMixin:
    def rel_db_type(self, connection): ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Any = ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Any = ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class SlugField(CharField):
    default_validators: Any = ...
    description: Any = ...
    allow_unicode: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def formfield(self, **kwargs): ...

class SmallIntegerField(IntegerField):
    description: Any = ...
    def get_internal_type(self): ...

class TextField(Field):
    description: Any = ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def get_prep_value(self, value): ...
    def formfield(self, **kwargs): ...

class TimeField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., auto_now: bool = ..., auto_now_add: bool = ..., **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value): ...
    def pre_save(self, model_instance, add): ...
    def get_prep_value(self, value): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def value_to_string(self, obj): ...
    def formfield(self, **kwargs): ...

class URLField(CharField):
    default_validators: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: Optional[Any] = ..., name: Optional[Any] = ..., **kwargs) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs): ...

class BinaryField(Field):
    description: Any = ...
    empty_values: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_placeholder(self, value, compiler, connection): ...
    def get_default(self): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def value_to_string(self, obj): ...
    def to_python(self, value): ...

class UUIDField(Field):
    default_error_messages: Any = ...
    description: str = ...
    empty_strings_allowed: bool = ...
    def __init__(self, verbose_name: Optional[Any] = ..., **kwargs) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def to_python(self, value): ...
    def formfield(self, **kwargs): ...
