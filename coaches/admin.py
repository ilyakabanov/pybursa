from django.contrib import admin

from pybursa.admin import BaseModelAdmin
from coaches.models import Coach


@admin.register(Coach)
class CoachAdmin(BaseModelAdmin):

    if len(Coach.ROLE_CHOICES) < 5:
        radio_fields = {'role': admin.VERTICAL}
