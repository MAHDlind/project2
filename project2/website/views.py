from django.shortcuts import render
from . import forms


# Create your views here.
def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def contact_us(request):
    return render(request, 'website/contact.html')

def get_start(request):
    return render(request, 'website/starter-page.html')
