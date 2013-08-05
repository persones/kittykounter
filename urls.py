from django.conf.urls import patterns, url

from kittykounter import views

urlpatterns = patterns('',
    url(r'^$', 'kittykounter.views.mainView', name='index'),
    url(r'^update/$', 'kittykounter.views.updateView', name='update'),
)
