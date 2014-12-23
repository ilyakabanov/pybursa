# -*- coding: utf8 -*-

from pybursa.forms import BaseModelForm
from coaches.models import Coach


class CoachForm(BaseModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'surname', 'date_of_birth',
                  'email', 'phone', 'role', 'user', 'dossier']
