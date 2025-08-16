from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactUsMessages(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=255, null=False)
    message = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.name}({self.email})'