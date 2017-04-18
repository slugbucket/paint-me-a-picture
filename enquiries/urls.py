from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enquiries/create$', views.create_enquiry, name='create'),
    url(r'^(?P<enquiry_id>[0-9]+)/', views.detail, name='detail'),
    url(r'^enquiries$', views.index, name='index')
]
