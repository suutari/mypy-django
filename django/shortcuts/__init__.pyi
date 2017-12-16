from django.http.request import HttpRequest as HttpRequest
from django.urls.resolvers import URLConf
from typing import Optional, Dict, Any, Union, List

def render(request: Optional[HttpRequest], template_name: str, context: dict, content_type: str, status: str, using: str) -> str: ...

def reverse(
    viewname: str, urlconf: URLConf = None,
    args: List[Union[str, int]] = None, kwargs: Dict[str, Any] = None,
    current_app: str = None,
) -> None: ...
