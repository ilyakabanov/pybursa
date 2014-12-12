# -*- coding: utf8 -*-

from django.contrib import admin

from pybursa.admin import BaseModelAdmin
from students.models import Student, Dossier


@admin.register(Student)
class StudentAdmin(BaseModelAdmin):

    if len(Student.PACKAGE_CHOICES) < 5:
        radio_fields = {'package': admin.VERTICAL}


@admin.register(Dossier)
class DossierAdmin(BaseModelAdmin):

    if len(Dossier.COLOR_CHOICES) < 5:
        radio_fields = {'color': admin.VERTICAL}
