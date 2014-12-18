from django.contrib import admin

# Register your models here.
from coaches.models import Coach
from courses.models import Course


class CoachInline(admin.TabularInline):
    model = Course
    fk_name = 'coach'
    extra = 0
    verbose_name_plural = 'Coach'


class AssistantInline(admin.TabularInline):
    model = Course
    fk_name = 'assistant'
    extra = 0
    verbose_name_plural = "Assistant"


class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'type')
    list_filter = ['type', ]
    list_editable = ['type', ]
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    radio_fields = {'type': admin.VERTICAL}
    inlines = [CoachInline, AssistantInline]


admin.site.register(Coach, CoachAdmin)