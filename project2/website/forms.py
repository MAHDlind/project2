from django import forms
from . import models
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'message']


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = models.NewsLetterForm
        fields = ['email']
