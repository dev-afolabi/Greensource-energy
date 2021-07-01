from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^services$', views.services, name='services'),
    url(r'^services/details$', views.service_detail, name='service_detail'),
    url(r'^services/details/solar-lighting$', views.electrical_design, name='electrical_design'),
    url(r'^services/details/design-installation$', views.solar_design, name='solar_design'),
    url(r'^services/details/commercial-solar$', views.commercial_solar, name='commercial_solar'),
    url(r'^services/details/solar-water-pump$', views.solar_water_pump, name='solar_water_pump'),
    url(r'^services/details/inverter-installation$', views.off_grid_solar, name='off_grid_solar'),
    url(r'^services/details/storage-solutions$', views.energy_management, name='energy_management'),
    url(r'^services/details/energy-management$', views.project_management, name='project_management'),
    url(r'^services/details/retrofit-maintenance$', views.maintenance_service, name='maintenance_service'),
    url(r'^services/details/electrical-installation$', views.hvac, name='hvac'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^shop$', views.design_plans, name= 'design_plans'),
    url(r'^shop/shop-details$', views.product_details, name= 'product_details'),
    url(r'^shop/cart$', views.cart, name= 'cart'),
    url(r'^gallery$', views.image, name= 'gallery'),
    url(r'^testimonial$', views.testimonial, name= 'testimonial'),
    url(r'^terms-of-use$', views.terms_of_use, name= 'terms-of-use'),
    url(r'^privacy-Policy$', views.privacy, name= 'privacy'),
    url(r'^mission/Vision$', views.mission, name= 'mission'),
    url(r'^faq$', views.faq, name= 'faq'),
    url(r'^company-profile$', views.Company, name= 'company-profile'),
    url(r'^Our-Team$', views.our_team, name= 'our-team'),
    url(r'^training$', views.training, name= 'training'),
    url(r'^pricing$', views.pricing, name= 'pricing'),    
]