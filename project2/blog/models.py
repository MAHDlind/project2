from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='blog')
    subject = models.CharField(max_length=255, null=False)
    context = models.TextField(null=False)
    category = models.ManyToManyField(Category)
    published_date = models.DateTimeField(null=True)
    published_status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='profile_pics',
        default='profile_pics/default.jpg',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'