from django.contrib import admin

from pybursa.admin import BaseModelAdmin
from coaches.models import Coach


@admin.register(Coach)
class CoachAdmin(BaseModelAdmin):

    if len(Coach.ROLE_CHOICES) < 5:
        radio_fields = {'role': admin.VERTICAL}

    list_display = ['name', 'surname', 'date_of_birth', 'role', 'user']
    list_display_links = ['name', 'surname']
    list_filter = ['role', 'date_of_birth']
    search_fields = ['name', 'surname', 'user']
    ordering = ['name']
