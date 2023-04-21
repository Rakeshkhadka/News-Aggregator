from django.urls import path
from . import views

urlpatterns = [
    path('scrape', views.scrape_ekantipur, name='scrape'),
    path('', views.index, name='home')
]