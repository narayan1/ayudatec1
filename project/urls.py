from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^experts/$', 'project.ayudatec1.views.expert_list'),
    url(r'^experts/(?P<username>\w+)/$', 'project.ayudatec1.views.profile'),

    # url(r'^articles/$', 'project.ayudatec1.views.articles_list'),
    # url(r'^articles/(?P<category>\w+)/$', 'project.ayudatec1.views.category'),
    # url(r'^articles/(?P<category>\w+)/(?P<article_slug>\w+)/$', 'project.ayudatec1.views.article'),
)
