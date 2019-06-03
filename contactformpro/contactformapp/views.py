from django.shortcuts import render
from .forms import ContactForm
from .models import ContactData
from django.http.response import HttpResponse

def contact_view(request):
    if request.method=="POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            first_name1 = request.POST.get('first_name')
            last_name1 = request.POST.get('last_name')
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')
            email1 = request.POST.get('email')
            mobile1 = request.POST.get('mobile')

            data = ContactData(
                first_name=first_name1,
                last_name=last_name1,
                username=username1,
                password=password1,
                email=email1,
                mobile=mobile1
            )

            data.save()
            cform=ContactForm()
            return render(request, 'contact.html', {'cform': cform})

        else:
            return HttpResponse("User Invalid Data")
    else:
        cform=ContactForm()
        return render(request,'contact.html',{'cform':cform})
