from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^deanOffice$', views.dean_office, name='dean_office'),
    url(r'^deanOffice/nextNumber$', views.dean_next_number, name='dean_next_number'),
    url(r'^welfareOffice$', views.welfare_office, name='welfare_office'),
    url(r'^welfareOffice/nextNumber$', views.welfare_next_number, name='welfare_next_number'),
]
