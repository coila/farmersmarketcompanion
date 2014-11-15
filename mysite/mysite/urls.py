from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

urlpatterns = patterns('',
        url(r'^polls/', include('polls.urls', namespace = 'polls')),
        url(r'^admin/', include(admin.site.urls)),
)

