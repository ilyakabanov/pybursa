from django.contrib import admin
from django.db import models
from students.models import Student, Group

from django.forms.extras.widgets import SelectDateWidget
from django.forms import widgets

#from pybursa.urls import pb_admin_site

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    #fields = ['name', 'surname', 'date_of_birth']
    #exclude = ['surname']
    date_hierarchy = 'date_of_birth'
    #filter_horizontal = ['courses']
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget}, 
    }
    list_display = ['name', 'surname', 'package']
    list_editable = ['surname']
    list_display_links = ['name', 'package']
    list_filter = ['package', 'group', 'courses', 'courses__start_date']
    # ordering = ['package', 'name']
    # preserve_filters = True
    #radio_fields = {"package": admin.HORIZONTAL}
    #raw_id_fields = ['group']
    #readonly_fields = ['date_of_birth']
    #prepopulated_fields = {"slug": ("name",)}
    # list_per_page = 2
    # list_max_show_all = 2
    search_fields = ['name', 'group__name']
    ordering = ['package']
    save_as = True
    save_on_top = True
    fieldsets = [
        (None, {'fields': ['name', 'surname']}),
        ('More information',
               {'fields': ['email'],
                'classes': ['collapse']}),
        ]


class StudenInline(admin.StackedInline):
    model = Student
    fk_name = 'group'
    fields = ['name']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudenInline]
    
