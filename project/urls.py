from django.conf.urls.defaults import *
from ayudatec1.views import *

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

    url(r'^experts/$', ExpertsListView.as_view()),
    url(r'^experts/(?P<username>[\w-]+)/$', ProfileView.as_view(template_name='profile.html')),

    url(r'^articles/$', ArticlesListView.as_view()),
    url(r'^articles/(?P<category>[\w-]+)/$', CategoryView.as_view(), name='CV'),
    url(r'^articles/(?P<category>[\w-]+)/(?P<article_slug>[\w-]+)/$', ArticleView.as_view()),

    url(r'^contact/$', ContactView.as_view()),

    url(r'^userinterface/$', UserInterface.as_view()),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^userinterface/myprofile/$', EditProfileView.as_view(), name='edit_profile'),
)
