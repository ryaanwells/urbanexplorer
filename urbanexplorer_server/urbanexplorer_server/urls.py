from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from tastypie.api import Api
from api.views import getSelf
from api.api import UserProfileResource, UserResource
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserProfileResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urbanexplorer_server.views.home', name='home'),
    # url(r'^urbanexplorer_server/', include('urbanexplorer_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^getSelf/', getSelf, name='getSelf'),
                       url(r'^api/', include(v1_api.urls)),
                       
)
