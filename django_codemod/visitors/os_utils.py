from django_codemod.constants import DJANGO_2_0, DJANGO_3_0
from django_codemod.visitors.base import BaseSimpleFuncRenameTransformer


class AbsPathTransformer(BaseSimpleFuncRenameTransformer):
    """Resolve deprecation of ``django.utils._os.abspathu``."""

    deprecated_in = DJANGO_2_0
    removed_in = DJANGO_3_0
    rename_from = "django.utils._os.abspathu"
    rename_to = "os.path.abspath"
