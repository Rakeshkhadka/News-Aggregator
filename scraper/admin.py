from django.contrib import admin
from .models import News
# Register your models here.
@admin.register(News)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    ordering = list_display