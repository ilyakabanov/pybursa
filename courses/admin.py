from django.contrib import admin

# Register your models here.
from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'technology', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date', 'technology']
    list_editable = ['start_date', 'end_date']
    search_fields = ['name', 'technology', 'start_date', 'end_date']
    radio_fields = {'technology': admin.HORIZONTAL}
    list_display_links = ['name', 'technology']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)