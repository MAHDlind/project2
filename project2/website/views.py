from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def contact_us(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
        else:
            messages.error(request, 'Your message encountered and error! and could not be sent.')

        return redirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, 'website/contact.html')

def get_start(request):
    return render(request, 'website/starter-page.html')

def newslatter(request):
    if request.method == 'POST':
        form = forms.NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your subscription request has been sent. Thank you!')
        else:
            messages.error(request, 'Your subscription request did not send.')

        return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect(request.META.get('HTTP_REFERER', '/'))