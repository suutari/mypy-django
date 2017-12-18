from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.resolvers import URLConf
from django.db.models import Model
from typing import Optional, Dict, Any, Union, List

def render(
    request: HttpRequest,
    template_name: str,
    context: dict = None,
    content_type: str = None,
    status: int = None,
    using: str = None,
) -> HttpResponse: ...

def reverse(
    viewname: str, urlconf: URLConf = None,
    args: List[Union[str, int]] = None, kwargs: Dict[str, Any] = None,
    current_app: str = None,
) -> None: ...

def redirect(to: Union[str, Model], permanent: bool = False, *args, **kwargs) -> HttpResponseRedirect: ...
