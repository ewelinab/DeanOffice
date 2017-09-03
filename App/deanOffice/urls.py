from django.conf.urls import url, include
from . import views
from . import test_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^deanOffice/$', views.dean_office, name='dean_office'),
    url(r'^deanOffice/nextNumber/$', views.dean_next_number, name='dean_next_number'),
    url(r'^deanOffice/getActualNumber/$', views.dean_get_actual_number, name='dean_get_actual_number'),
    url(r'^deanOffice/getAvailableNumber/$', views.dean_get_available_number, name='dean_get_available_number'),
    url(r'^deanOffice/reserveNumber/(?P<login>[0-9]+)/(?P<password>\w+)/$', views.dean_reserve_number, name='dean_reserve_number'),
    url(r'^welfareOffice/$', views.welfare_office, name='welfare_office'),
    url(r'^welfareOffice/nextNumber/$', views.welfare_next_number, name='welfare_next_number'),
    url(r'^welfareOffice/getActualNumber/$', views.welfare_get_actual_number, name='welfare_get_actual_number'),
    url(r'^welfareOffice/getAvailableNumber/$', views.welfare_get_available_number, name='welfare_get_available_number'),
    url(r'^welfareOffice/reserveNumber/(?P<login>[0-9]+)/(?P<password>\w+)/$', views.welfare_reserve_number, name='welfare_reserve_number'),
    # employee authorization urls
    url(r'^checkLogin/(?P<login>[0-9]+)/(?P<password>\w+)/$', views.check_login, name='check_login'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    # for test, will be removed in future
    # fill database with random data
    url(r'^fillDatabase/$', test_views.fill_database, name='fill_database'),
    # reserveNumber that do not need password
    url(r'^deanOffice/reserveNumber/(?P<login>[0-9]+)/$', test_views.dean_reserve_number, name='dean_reserve_number'),
    url(r'^welfareOffice/reserveNumber/(?P<login>[0-9]+)/$', test_views.welfare_reserve_number, name='welfare_reserve_number'),
]
