from typing import Any, Callable, Dict, List, Tuple

from django.http.request import QueryDict
from django.http.response import HttpResponse


class WSGIRequest:
    def __init__(self, environ: Dict[str, str]) -> None: ...

    @property
    def GET(self) -> QueryDict: ...

    @property
    def COOKIES(self) -> Dict[str, str]: ...

    @property
    def FILES(self) -> QueryDict: ...

    POST: QueryDict


class WSGIHandler:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def __call__(
        self,
        environ: Dict[str, str],
        start_response: Callable[[str, List[Tuple[str, str]]], None],
    ) -> HttpResponse: ...
