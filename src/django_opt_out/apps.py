# -*- coding: utf-8
from __future__ import absolute_import

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def setup_app_settings():
    from . import app_settings as defaults
    from django.conf import settings
    for name in dir(defaults):
        if name.isupper() and not hasattr(settings, name):
            setattr(settings, name, getattr(defaults, name))


class DjangoOptOutConfig(AppConfig):
    name = 'django_opt_out'
    verbose_name = _('Messaging Opt-Outs')

    def ready(self):
        setup_app_settings()
