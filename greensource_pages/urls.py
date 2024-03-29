from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^services$', views.services, name='services'),
    url(r'^services/details/solar-lighting$', views.electrical_design, name='electrical_design'),
    url(r'^services/details/residential-solar$', views.solar_design, name='solar_design'),
    url(r'^services/details/storage-solutions$', views.energy_management, name='energy_management'),
    url(r'^services/details/energy-management$', views.project_management, name='project_management'),
    url(r'^services/details/retrofit-maintenance$', views.maintenance_service, name='maintenance_service'),
    url(r'^services/details/electrical-installation$', views.hvac, name='hvac'),
    url(r'^about/gallery$', views.image, name= 'gallery'),
    url(r'^testimonial$', views.testimonial, name= 'testimonial'),
    url(r'^terms-of-use$', views.terms_of_use, name= 'terms_of_use'),
    url(r'^privacy-Policy$', views.privacy, name= 'privacy'),
    url(r'^faq$', views.faq, name= 'faq'),
    url(r'^about/our-team$', views.our_team, name= 'our_team'),
    url(r'^landing-page$', views.pricing, name= 'pricing'),   
    url(r'^projects', views.projects, name='projects'),
    url(r'^project/(?P<slug>[\w-]+)/$', views.project_details, name='project_details'),
]