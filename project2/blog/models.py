from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
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
    tags = TaggableManager()
    published_date = models.DateTimeField(null=True)
    published_status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_details', kwargs={'pid': self.id})


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