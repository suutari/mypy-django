from types import ModuleType
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, Union

from django.http.response import HttpResponse

from .resolvers import URLPattern

_ModuleOrStr = Union[ModuleType, str]
_AppName = Optional[str]
_Namespace = Optional[str]
_IncludeResult = Tuple[ModuleType, _AppName, _Namespace]
_PatternParam = Union[_ModuleOrStr, Sequence[URLPattern]]
_IncludeResultOrPatterns = Tuple[_PatternParam, _AppName, _Namespace]
_ViewType = Callable[..., HttpResponse]


def include(
    arg: Union[_ModuleOrStr, Tuple[_ModuleOrStr, str]],
    namespace: Optional[str]=None,
) -> _IncludeResult: ...


def path(
    route: str,
    view: Union[_ViewType, _IncludeResultOrPatterns],
    kwargs: Optional[Dict[str, Any]]=None,
    name: Optional[str]=None,
) -> URLPattern: ...


def re_path(
    route: str,
    view: Union[_ViewType, _IncludeResultOrPatterns],
    kwargs: Optional[Dict[str, Any]]=None,
    name: Optional[str]=None,
) -> URLPattern: ...
