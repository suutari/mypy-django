from typing import Any, Dict, List, Optional

from .base import BaseCommand


def find_commands(management_dir: str) -> List[str]: ...


def load_command_class(
    app_name: str,
    name: str
) -> BaseCommand: ...


def get_commands() -> Dict[str, str]: ...


def call_command(
    command_name: str,
    *args: Any,
    **options: Any,
) -> str: ...


class ManagementUtility:
    ...


def execute_from_command_line(
    argv: Optional[List[str]]=None
) -> None: ...
