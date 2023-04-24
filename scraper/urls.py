from django.urls import path
from . import views

urlpatterns = [
    # path('scrape', views.scrape_nagarik, name='scrape'),
    # path('scrape1', views.scrape_ekantipur, name='scrape1'),
    path('', views.index, name='home'),
    path('<str:category>', views.index_by_category, name="get_by_category")
]