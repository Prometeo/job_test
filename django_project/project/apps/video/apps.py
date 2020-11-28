from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VideosConfig(AppConfig):
    name = "video"
    verbose_name = _("Videos")
