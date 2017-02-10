from django.apps import AppConfig
from django.conf import settings
from django.forms.widgets import Select, CheckboxInput
from django.contrib.admin import options


class GhosterConfig(AppConfig):
    name = 'ghoster'
    verbose_name = "GHOSTER CMS"
    # CheckboxInput.render = GhosterWidget.slider_checkbox_render
    # from django.db import models
    # options.FORMFIELD_FOR_DBFIELD_DEFAULTS[models.CharField].update({'widget': GhTextInputWidget})




