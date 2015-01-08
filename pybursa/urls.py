from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import contact

urlpatterns = patterns('',

    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', contact, name='contact-us'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

)