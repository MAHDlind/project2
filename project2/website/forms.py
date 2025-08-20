from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'message']

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = models.NewsLetterForm
        fields = ['email']