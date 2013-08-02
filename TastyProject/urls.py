from django.conf.urls import patterns, include, url
from TastyApp1.api.resources import UserResource,UserExtaResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api=Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(UserExtaResource())
v1_api.prepend_urls()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TastyProject.views.home', name='home'),
    # url(r'^TastyProject/', include('TastyProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
