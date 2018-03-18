from typing import List, Tuple

from django.urls.resolvers import URLPattern


class AdminSite:
    def __init__(self, name: str='admin') -> None: ...

    # def check(
    #     self,
    #     app_configs: Optional[Iterable[AppConfig]],
    # ) -> List[CheckMessage]: ...

    # def register(self, model_or_iterable, admin_class=None, **options):

    # def unregister(self, model_or_iterable):

    # def is_registered(self, model):

    # def add_action(self, action, name=None):

    # def disable_action(self, name):

    # def get_action(self, name):

    # @property
    # def actions(self):

    # @property
    # def empty_value_display(self):

    # @empty_value_display.setter
    # def empty_value_display(self, empty_value_display):

    # def has_permission(self, request):

    # def admin_view(self, view, cacheable=False):

    def get_urls(self) -> List[URLPattern]: ...

    @property
    def urls(self) -> Tuple[List[URLPattern], str, str]: ...

    # def each_context(self, request):

    # def password_change(self, request, extra_context=None):

    # def password_change_done(self, request, extra_context=None):

    # def i18n_javascript(self, request, extra_context=None):

    # def logout(self, request, extra_context=None):

    # def login(self, request, extra_context=None):

    # def get_app_list(self, request):

    # def index(self, request, extra_context=None):

    # def app_index(self, request, app_label, extra_context=None):


site: AdminSite
