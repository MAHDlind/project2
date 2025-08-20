from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}({self.email})'


class NewsLetterForm(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email