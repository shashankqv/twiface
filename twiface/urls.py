from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^twiface/', include('twiface.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'twiface.views.home'),
    url(r'^login$', 'twiface.views.login', name='login_url'),
    url(r'^logout$','django.contrib.auth.views.logout',name='logout'),
    url(r'customize$', 'twiface.userprofile.views.create_background', name='customize'),
    url(r'', include('social_auth.urls')),
)
