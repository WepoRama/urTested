from django.conf.urls import patterns, include, url
from django.contrib import admin
import django.contrib.auth


# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/profile/$', 'DjangoApplication.MyFirstApp.views.choose', name='choose'),
    
    #url(r'^$', 'DjangoApplication.MyFirstApp.views.login', name='login'),
    url(r'^createTest$', 'DjangoApplication.MyFirstApp.views.createTest', name='createTest'),
    url(r'^listTests$', 'DjangoApplication.MyFirstApp.views.listTests', name='listTests'),
    url(r'^(?P<test_id>\d+)/takeTest$', 'DjangoApplication.MyFirstApp.views.takeTest', name='takeTest'),
    url(r'^(?P<test_id>\d+)/rateTest$', 'DjangoApplication.MyFirstApp.views.rateTest', name='rateTest'),
    url(r'^createIt/$', 'DjangoApplication.MyFirstApp.views.createIt', name='createIt'),
    #url(r'^addQuestion//$', 'DjangoApplication.MyFirstApp.views.addQuestion', name='addQuestion'),
    url(r'^(?P<test_id>\d+)/addQuestion/$', 'DjangoApplication.MyFirstApp.views.addQuestion'),
    url(r'^(?P<question_id>\d+)/addAnswer/$', 'DjangoApplication.MyFirstApp.views.addAnswer'),
    # Examples:
    # url(r'^$', 'DjangoApplication.views.home', name='home'),
    # url(r'^DjangoApplication/', include('DjangoApplication.DjangoApplication.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
