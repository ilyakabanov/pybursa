# -*- coding: utf8 -*-

from django.contrib import admin
from django.forms import widgets
from django.db import models


class BaseModelAdmin(admin.ModelAdmin):
    """Базовый класс моделей приложения"""

    formfield_overrides = {
        models.ManyToManyField: {'widget': widgets.CheckboxSelectMultiple},
    }

    save_on_top = True
