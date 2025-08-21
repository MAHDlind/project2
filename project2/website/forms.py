
from django import forms
from . import models
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'message']
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = models.NewsLetterForm
        fields = ['email']