from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            from_email = form.cleaned_data['from_email']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            price_code = form.cleaned_data['price_code']
            service = form.cleaned_data['service']
            message = form.cleaned_data['message']
            full_name = first_name

            subject = "message from "+first_name
            content = "You have a message from "+full_name+ " \n\n Phone number: "+phone+ "\n Email: "+from_email+"\n city: "+city+ "\n Code: "+price_code+ "\n service: "+service+" \n\n" +message
                        


            try:
                send_mail(subject,content,from_email,['support@greensourcenergy.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact_us/contact.html', {'form':form})

def success(request):
    return render(request, "contact_us/success.html")