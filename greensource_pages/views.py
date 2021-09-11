from django.shortcuts import render, get_object_or_404, redirect
from .models import Galllery, Images, Testimonial

# Create your views here.
def index(request):
    index = Testimonial.objects.all().order_by('-date')
    return render(request,"greensource_pages/index.html", {'index': index})

def about(request):
    return render(request,"greensource_pages/about.html")

def services(request):
    return render(request,"greensource_pages/services.html")

def service_detail(request):
    return render(request,"greensource_pages/service-detail.html")

def electrical_design(request):
    return render(request,"greensource_pages/electrical-design.html")

def solar_design(request):
    return render(request,"greensource_pages/solar-design.html")

def off_grid_solar(request):
    return render(request,"greensource_pages/off-grid-solar.html")  

def commercial_solar(request):
    return render(request,"greensource_pages/commercial-solar.html")  

def solar_water_pump(request):
    return render(request,"greensource_pages/solar-water-pump.html")

def energy_management(request):
    return render(request,"greensource_pages/energy-management.html")

def maintenance_service(request):
    return render(request,"greensource_pages/maintenance-service.html") 

def hvac(request):
    return render(request,"greensource_pages/hvac.html")

def project_management(request):
    return render(request,"greensource_pages/project-management.html")

def image(request):
    images = Images.objects.all().order_by('-date')
    return render(request,"greensource_pages/gallery.html", {'images': images})

def testimonial(request):
    testimonial = Testimonial.objects.all().order_by('-date')
    return render(request,"greensource_pages/testimonial.html", {'testimonial': testimonial})

def terms_of_use(request):
    return render(request,"greensource_pages/terms-of-use.html")

def privacy(request):
    return render(request,"greensource_pages/privacy.html")

def faq(request):
    return render(request,"greensource_pages/faq.html")

def our_team(request):
    return render(request,"greensource_pages/our-team.html")

def pricing(request):
    return render(request,"greensource_pages/pricing.html")

def projects(request):
    projects = Galllery.objects.all().order_by('-date')
    return render(request,"greensource_pages/projects.html", {'projects': projects})






