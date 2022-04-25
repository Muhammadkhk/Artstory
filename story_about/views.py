from django.shortcuts import render

# Create your views here.
from .models import Siteabout 

def about_page(request):
    site_about = Siteabout.objects.first()
    context = {
        'setting': site_about
    }
    return render(request, 'home/about.html', context)