from django.contrib import admin

from pybursa.admin import BaseModelAdmin
from courses.models import Course, Address


@admin.register(Course)
class CourseAdmin(BaseModelAdmin):

    if len(Course.LANG_CHOICES) < 5:
        radio_fields = {'lang': admin.HORIZONTAL}
        
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Address)
class AddressAdmin(BaseModelAdmin):
    pass
