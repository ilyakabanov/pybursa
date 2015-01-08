from django.conf.urls import patterns, include, url
from students.views import (StudentListView, StudentView, 
					StudentUpdateView, StudentCreateView)


urlpatterns = patterns('',

    url(r'^$', StudentListView.as_view(), name='students-list'),
    url(r'^add/$', StudentCreateView.as_view(), name='student-add'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='student-edit'),
    url(r'^(?P<pk>\d+)/$', StudentView.as_view(), name='student-item'),

)
