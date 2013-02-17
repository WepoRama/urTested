from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'DjangoApplication.MyFirstApp.views.home', name='home'),
    url(r'^$', 'DjangoApplication.MyFirstApp.views.createTest', name='createTest'),
    url(r'^createIt/$', 'DjangoApplication.MyFirstApp.views.createIt', name='createIt'),
    #url(r'^addQuestion//$', 'DjangoApplication.MyFirstApp.views.addQuestion', name='addQuestion'),
    url(r'^(?P<test_id>\d+)/addQuestion/$', 'DjangoApplication.MyFirstApp.views.addQuestion'),
    # Examples:
    # url(r'^$', 'DjangoApplication.views.home', name='home'),
    # url(r'^DjangoApplication/', include('DjangoApplication.DjangoApplication.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)