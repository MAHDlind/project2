from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['__str__', 'sent_at']
    ordering = ['sent_at']
    list_filter = ['sent_at']
    search_fields = ['email', 'name']

@admin.register(models.NewsLatterForm)
class NewsLatterFormAdmin(admin.ModelAdmin):
    pass
