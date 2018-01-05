# Stubs for django.utils.autoreload (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

USE_INOTIFY: bool
fd: Any
RUN_RELOADER: bool
FILE_MODIFIED: int
I18N_MODIFIED: int

def gen_filenames(only_new: bool = ...): ...
def clean_files(filelist): ...
def reset_translations(): ...
def inotify_code_changed(): ...
def code_changed(): ...
def check_errors(fn): ...
def raise_last_exception(): ...
def ensure_echo_on(): ...
def reloader_thread(): ...
def restart_with_reloader(): ...
def python_reloader(main_func, args, kwargs): ...
def jython_reloader(main_func, args, kwargs): ...
def main(main_func, args: Optional[Any] = ..., kwargs: Optional[Any] = ...): ...
