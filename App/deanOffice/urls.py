from django.conf.urls import url, include
from . import views
from . import test_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^deanOffice/$', views.dean_office, name='dean_office'),
    url(r'^deanOffice/nextNumber/$', views.dean_next_number, name='dean_next_number'),
    url(r'^deanOffice/getActualNumber/$', views.dean_get_actual_number, name='dean_get_actual_number'),
    url(r'^deanOffice/getAvailableNumber/$', views.dean_get_available_number, name='dean_get_available_number'),
    url(r'^deanOffice/reserveNumber/(?P<login>[0-9]+)/$', views.dean_reserve_number, name='dean_reserve_number'),
    url(r'^welfareOffice/$', views.welfare_office, name='welfare_office'),
    url(r'^welfareOffice/nextNumber/$', views.welfare_next_number, name='welfare_next_number'),
    url(r'^fillDatabase/$', test_views.fill_database, name='fill_database'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
]
