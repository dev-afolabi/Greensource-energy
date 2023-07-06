from django.shortcuts import render, get_object_or_404, redirect
from .models import Images, Solar, Testimonial, Landingpage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.
def index(request):
    template = {
        "solar" : Solar.objects.all()[:4],
        "testimonial" : Testimonial.objects.all()[:3],
    }
    return render(request,"greensource_pages/index.html", {'template':template})

def about(request):
    return render(request,"greensource_pages/about.html")

def services(request):
    return render(request,"greensource_pages/services.html")

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
    solar = Solar.objects.all()
    return render(request,"greensource_pages/projects.html", {'obj': solar})

def project_details(request,slug):
    solar = get_object_or_404(Solar,slug=slug)
    return render(request,'greensource_pages/project-details.html', {'obj': solar})

def image(request):
    images = Images.objects.all()
    return render(request,"greensource_pages/gallery.html", {'images': images})

def testimonial(request):
    testimonial = Testimonial.objects.all()
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
    template = {
        "featured" : Featured.objects.all(),
        "landingpage" : Landingpage.objects.all(),
    }
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['from_email']
            service_option = form.cleaned_data['service_option']
            address = form.cleaned_data['address']
            message = form.cleaned_data['message']
            agree = form.cleaned_data['agree']
            full_name = first_name+" "+last_name

            subject = "message from "+full_name
            content = "You have a message from "+full_name+ "\n Phone: "+phone+ "\n Email: "+from_email+ "\n service_option: "+service_option+ "\n address: "+address+ "\n" +message   
           

            try:
                send_mail(subject,content,'support@greensourcenergy.com',['support@greensourcenergy.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'greensource_pages/pricing.html', {'form':form, 'template':template})

def success(request):
    return render(request, "contact_us/success.html")

    