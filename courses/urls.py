from django.conf.urls import patterns, url

from courses import views


urlpatterns = patterns(
    '',
    url(r'^$', views.courses_list, name="index"),
    url(r'^(?P<course_id>\d+)/$', views.courses_item, name="detail"),
    url(r'^add/$', views.courses_add, name="add"),
    url(r'^edit/(?P<course_id>\d+)/$', views.courses_edit, name="edit"),
    url(r'^delete/(?P<course_id>\d+)/$', views.courses_delete, name="delete"),
)
