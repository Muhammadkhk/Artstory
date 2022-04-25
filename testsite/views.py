import itertools
from django.shortcuts import render


# code behind
def home_page(request):

    return render(request, 'home/index.html', {})

def handle_404_error(request, exception):
    return render(request, 'home/404.html', {})

