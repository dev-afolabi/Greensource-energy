from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['location']
            state = form.cleaned_data['services']
            message = form.cleaned_data['message']
            full_name = first_name+" "+last_name

            subject = "message from "+first_name+" "+last_name
            content = "You have a message from "+full_name+ " \n\n Phone number: "+phone+ "\n Email: "+from_email+"\n city: "+city+" \n state: "+state+" \n\n" + message
                        


            try:
                send_mail(subject,content,from_email,['support@greensourcenergy.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact_us/contact.html', {'form':form})

def success(request):
    return render(request, "contact_us/success.html")