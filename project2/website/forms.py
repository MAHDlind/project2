from django import forms
from . import models
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from snowpenguin.django.recaptcha3.widgets import ReCaptchaHiddenInput

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaHiddenInput())
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'message']

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = models.NewsLetterForm
        fields = ['email']