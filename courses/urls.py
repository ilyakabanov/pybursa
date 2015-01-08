from django.conf.urls import patterns, url

from courses import views


urlpatterns = patterns(
    '',
    url(r'^$', views.courses_list, name="courses-list"),
    url(r'^(?P<course_id>\d+)/$', views.courses_item, name="course-item"),
    url(r'^add/$', views.courses_add, name="course-add"),
    url(r'^edit/(?P<course_id>\d+)/$', views.courses_edit, name="course-edit"),
    url(r'^delete/(?P<course_id>\d+)/$', views.courses_delete, name="course-delete"),
)