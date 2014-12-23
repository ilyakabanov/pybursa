from django.conf.urls import patterns, url

from coaches import views


urlpatterns = patterns(
    '',
    url(r'^$', views.coaches_list, name="index"),
    url(r'^(?P<coach_id>\d+)/$', views.coaches_item, name="detail"),
    url(r'^add/$', views.coaches_add, name="add"),
    url(r'^edit/(?P<coach_id>\d+)/$', views.coaches_edit, name="edit"),
    url(r'^delete/(?P<coach_id>\d+)/$', views.coaches_delete, name="delete"),
)
