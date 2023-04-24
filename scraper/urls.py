from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:category>', views.index_by_category, name="get_by_category"),
    path('search/', views.search, name='search'),
]