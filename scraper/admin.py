from django.contrib import admin
from .models import News, Category, Site
# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Site)