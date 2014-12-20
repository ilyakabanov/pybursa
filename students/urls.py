from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns(
    '',
    url(r'^$', views.students_list, name="index"),
    url(r'^(?P<student_id>\d+)/$', views.students_item, name="detail"),
    url(r'^add/$', views.students_add, name="add"),
    url(r'^edit/(?P<student_id>\d+)/$', views.students_edit, name="edit"),
    url(r'^delete/(?P<student_id>\d+)/$', views.students_delete, name="delete"),
)
