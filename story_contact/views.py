from multiprocessing import context
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import ContactUs

# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url = '/singin')
def contact_page(request):
    if request.method == 'GET':
        return render(request, 'home/contact.html', {})
    else:
        contact =ContactUs.objects.create(full_name=request.POST['fullname'],subject=request.POST['subject'], email=request.POST['email'], text =request.POST['message'])
        contact.save()
        context={
        'username':request.POST['fullname'],
        'subject':request.POST['subject'],
        'email':request.POST['email'],
        'text':request.POST['message']
            }
        return render(request, 'home/index.html',context)

             

