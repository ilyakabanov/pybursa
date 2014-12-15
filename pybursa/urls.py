from django.conf.urls import patterns, include, url
from django.contrib import admin

# from django.contrib.admin import AdminSite

# class PBAdminSite(AdminSite):
#     site_header = 'PyBursa admin'

# pb_admin_site = PBAdminSite(name='pybursaadmin')


urlpatterns = patterns('',

    url(r'^students/', include('students.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^pbadmin/', include(pb_admin_site.urls)),

)
