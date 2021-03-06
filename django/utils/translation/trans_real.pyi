# Stubs for django.utils.translation.trans_real (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import gettext as gettext_module
from typing import Any, Optional

CONTEXT_SEPARATOR: str
accept_language_re: Any
language_code_re: Any
language_code_prefix_re: Any

def reset_cache(**kwargs): ...
def to_locale(language, to_lower: bool = ...): ...
def to_language(locale): ...

class DjangoTranslation(gettext_module.GNUTranslations):
    domain: str = ...
    plural: Any = ...
    def __init__(self, language, domain: Optional[Any] = ..., localedirs: Optional[Any] = ...) -> None: ...
    def merge(self, other): ...
    def language(self): ...
    def to_language(self): ...

def translation(language): ...
def activate(language): ...
def deactivate(): ...
def deactivate_all(): ...
def get_language(): ...
def get_language_bidi(): ...
def catalog(): ...
def do_translate(message, translation_function): ...
def gettext(message): ...
ugettext = gettext

def pgettext(context, message): ...
def gettext_noop(message): ...
def do_ntranslate(singular, plural, number, translation_function): ...
def ngettext(singular, plural, number): ...
ungettext = ngettext

def npgettext(context, singular, plural, number): ...
def all_locale_paths(): ...
def check_for_language(lang_code): ...
def get_languages(): ...
def get_supported_language_variant(lang_code, strict: bool = ...): ...
def get_language_from_path(path, strict: bool = ...): ...
def get_language_from_request(request, check_path: bool = ...): ...
def parse_accept_lang_header(lang_string): ...
