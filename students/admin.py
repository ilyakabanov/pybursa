# -*- coding: utf8 -*-

from django.contrib import admin

from pybursa.admin import BaseModelAdmin
from students.models import Student, Dossier


@admin.register(Student)
class StudentAdmin(BaseModelAdmin):

    if len(Student.PACKAGE_CHOICES) < 5:
        radio_fields = {'package': admin.VERTICAL}

    list_display = ['name', 'surname', 'date_of_birth', 'package']
    list_display_links = ['name', 'surname']
    list_filter = ['package', 'date_of_birth']
    search_fields = ['name', 'surname']
    ordering = ['name']


@admin.register(Dossier)
class DossierAdmin(BaseModelAdmin):

    if len(Dossier.COLOR_CHOICES) < 5:
        radio_fields = {'color': admin.VERTICAL}

    list_display = ['id', 'color', 'adress']
    list_filter = ['color']
    search_fields = ['id', 'color', 'adress']
    ordering = ['id']
