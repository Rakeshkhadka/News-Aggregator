from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse 
from .models import News

# Create your views here.

# def scrape_nagarik(request):
#     base_url = "https://nagariknews.nagariknetwork.com"
#     paths = [ "/politics", "/economy", "/arts", "/sports"]
#     for paths_ in paths:
#         response = requests.get(base_url+paths_, verify=False)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         news = soup.find_all('article', {'class':'list-group-item'})
#         for article in news:
#             h1_tages = article.find_all('h1') #h1
#             images = article.find('figure').find_all('img') #gives image and url
#             urls = article.find('figure').find_all('a')
#             for h1, imag, url in zip(h1_tages, images, urls):
#                 img_url = ''
#                 category = next((choice[0] for choice in News.CATEGORY_CHOICES if choice[1] == paths_.replace('/', '').title()), 'others')
#                 print(imag['data-src'])
#                 try:
#                     img_url = imag['data-lazy']
#                 except:
#                     img_url = imag['data-src']
#                 print(h1.get_text())
#                 news_title = h1.get_text()
#                 print(url['href'])
#                 nurl = base_url + url['href']
#                 if not News.objects.filter(title__icontains=news_title).exists():
#                     News.objects.create(title=news_title, img_src=img_url, url=nurl, category=category)
#     return HttpResponse("hello")        
    
    
    
def index(request):
    news = News.objects.all()
    categories = News.CATEGORY_CHOICES
    context = {
        'news': news,
        'categories':categories
    }
    return render(request, 'index.html', context)

def index_by_category(request, category):
    categories = News.CATEGORY_CHOICES
    news = News.objects.filter(category=category)
    context = {
        'news': news,
        'categories':categories,     
               }
    return render(request, 'index.html', context)