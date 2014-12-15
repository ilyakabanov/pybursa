from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', _list),
    url(r'^(?P<_id>\d+)/$', _item),

)
