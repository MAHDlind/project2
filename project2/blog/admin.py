from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(models.Post)
class Post(admin.ModelAdmin):
    list_display = ['title', 'subject', 'author__first_name']
    list_filter = ['category']

admin.site.register(models.Category)
admin.site.register(models.Profile)

class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = True

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)