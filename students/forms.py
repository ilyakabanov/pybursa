# -*- coding: utf8 -*-

from pybursa.forms import BaseModelForm
from students.models import Student


class StudentForm(BaseModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'date_of_birth',
                  'email', 'phone', 'package', 'dossier']
