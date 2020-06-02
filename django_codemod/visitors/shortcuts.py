from typing import Sequence

from libcst import Arg, Call, Name

from django_codemod.constants import DJANGO_20, DJANGO_30
from django_codemod.visitors.base import BaseSimpleFuncRenameTransformer


class RenderToResponseTransformer(BaseSimpleFuncRenameTransformer):
    """
    Resolve deprecation of ``django.shortcuts.render_to_response``.

    Replaces ``render_to_response()`` by ``render()`` and add
    ``request=None`` as the first argument of ``render()``.
    """

    deprecated_in = DJANGO_20
    removed_in = DJANGO_30
    rename_from = "django.shortcuts.render_to_response"
    rename_to = "django.shortcuts.render"

    def update_call_args(self, node: Call) -> Sequence[Arg]:
        return (Arg(value=Name("None")), *node.args)
