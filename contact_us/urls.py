from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact-us$', views.contact_us, name='contact_us'),
    url(r'^success$', views.success, name='success'),
] 