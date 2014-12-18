from django.contrib import admin

from students.models import Student, Dossier, Address


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'package']
    list_filter = ['package', ]
    list_editable = ['package', ]
    search_fields = (
        'first_name', 'last_name', 'email', 'phone_number', 'package')
    radio_fields = {'package': admin.HORIZONTAL}
    filter_horizontal = ['courses', ]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['zip', 'country', 'city', 'street', 'house']
    list_display_links = list_display
    list_filter = ['country', 'city']
    search_fields = ['zip', 'country', 'city', 'street']


class DossierAdmin(admin.ModelAdmin):
    list_display = ['address', 'favourite_color']
    list_display_links = list_display
    filter_horizontal = ['unliked_courses', ]
    radio_fields = {'favourite_color': admin.VERTICAL}


admin.site.register(Student, StudentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Dossier, DossierAdmin)