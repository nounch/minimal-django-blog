from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bestblog.views',
    # Examples:
    # url(r'^$', 'bestblog.views.home', name='home'),
    # url(r'^bestblog/', include('bestblog.foo.urls')),
    url(r'^404/$', 'show_404'),
    url(r'^index/$', 'index'),
    url(r'^posts$', 'show_n_posts'),
    url(r'^post/(?P<post_id>\d+)/$', 'show_post'),
    url(r'^post/new/$', 'submit_post'),
    url(r'^post/new/submit/$', 'create_new_post'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

