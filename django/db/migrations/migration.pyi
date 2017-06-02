from typing import List, Tuple


class Migration:

    dependencies = ...  # type: List[Tuple[str, str]]


class SwappableTuple(tuple):
    ...


def swappable_dependency(value):
    ...
