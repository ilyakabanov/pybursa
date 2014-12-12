from django.contrib import admin

from pybursa.admin import BaseModelAdmin
from courses.models import Course, Address


@admin.register(Course)
class CourseAdmin(BaseModelAdmin):

    if len(Course.LANG_CHOICES) < 5:
        radio_fields = {'lang': admin.HORIZONTAL}

    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'start_date', 'end_date', 'slug']
    list_display_links = ['name', 'slug']
    list_filter = ['lang', 'start_date', 'end_date']
    search_fields = ['name']
    ordering = ['start_date', 'end_date', 'name']


@admin.register(Address)
class AddressAdmin(BaseModelAdmin):

    list_display = ['country', 'city', 'street', 'home', 'zcode']
    list_display_links = ['country', 'city', 'street', 'home']
    list_editable = ['zcode']
    list_filter = ['country', 'city']
    search_fields = ['country', 'city', 'street', 'home']
    ordering = ['country']
