from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ContactUsMessages)
class Admin(admin.ModelAdmin):
    list_display = ['__str__', 'sent_at']
    date_hierarchy = 'sent_at'
    empty_value_display = '-empty-'
    list_filter = ['sent_at']
    search_fields = ['email', 'name']
    ordering = ['sent_at']
