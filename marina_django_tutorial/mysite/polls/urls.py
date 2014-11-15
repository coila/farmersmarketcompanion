from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="details"),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name="results"),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    # url(r'^search-form/$', views.search_form, name='search_form'),
    # url(r'^search/$', views.search, name='search'),

    # url(r'^search_form', views.search_form, name='search_form'),
    url(r'^search', views.search, name='search'),
    url(r'^getResults', views.search, name='getResults'),

    )
urlpatterns += staticfiles_urlpatterns()
