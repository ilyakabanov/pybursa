from django.contrib import admin

from courses.models import Course, Address


admin.site.register(Course)
admin.site.register(Address)
