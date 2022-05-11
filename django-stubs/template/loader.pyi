from typing import Any, Dict, List, Optional, Union

from django.http.request import HttpRequest
from django.template.base import Template
from django.template.exceptions import (  # noqa: F401
    TemplateDoesNotExist as TemplateDoesNotExist,
)

from . import engines as engines  # noqa: F401

def get_template(template_name: str, using: Optional[str] = ...) -> Template: ...
def select_template(
    template_name_list: Union[List[str], str], using: Optional[str] = ...
) -> Template: ...
def render_to_string(
    template_name: Union[List[str], str],
    context: Optional[Dict[str, Any]] = ...,
    request: Optional[HttpRequest] = ...,
    using: Optional[str] = ...,
) -> str: ...
