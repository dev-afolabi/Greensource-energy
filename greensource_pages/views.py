from django.shortcuts import render
from .models import Galllery, Images

# Create your views here.
def index(request):
    return render(request,"greensource_pages/index.html")

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

def energy_management(request):
    return render(request,"greensource_pages/energy-management.html")

def maintenance_service(request):
    return render(request,"greensource_pages/maintenance-service.html")

def hvac(request):
    return render(request,"greensource_pages/hvac.html")

def project_management(request):
    return render(request,"greensource_pages/project-management.html")

def projects(request):
    projects = Galllery.objects.all().order_by('-date')
    return render(request,"greensource_pages/projects.html", {'projects': projects})

def image(request):
    images = Images.objects.all().order_by('-date')
    return render(request,"greensource_pages/gallery.html", {'images': images})

def design_plans(request):
    return render(request,"greensource_pages/design-plans.html") 

def testimonial(request):
    return render(request,"greensource_pages/testimonial.html")

def terms_of_use(request):
    return render(request,"greensource_pages/terms-of-use.html")

def privacy(request):
    return render(request,"greensource_pages/privacy.html")

def Company(request):
    return render(request,"greensource_pages/company-profile.html")

def mission(request):
    return render(request,"greensource_pages/mission.html")

def faq(request):
    return render(request,"greensource_pages/faq.html")

def our_team(request):
    return render(request,"greensource_pages/our-team.html")

def training(request):
    return render(request,"greensource_pages/training.html")





