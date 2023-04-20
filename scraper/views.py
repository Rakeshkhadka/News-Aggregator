from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse 
from .models import News

# Create your views here.

def scrape(request):
    website = "https://ekantipur.com/"
    response = requests.get(website, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = soup.find_all('article', {'class':'normal'})
    

    for article in news:
        titles = article.find_all('h2')
        image_source = article.find_all('img')
        url = article.find_all('a')
        for title, img, u in zip(titles, image_source, url):
            news_title = title.get_text()
            url = website+u['href']
            try:
                img_url =  'https:'+img['src']
            except:
                pass 
            if not News.objects.filter(title__icontains=news_title).exists():
                News.objects.create(title=news_title, img_src=img_url, url=url)
    return HttpResponse("hello")


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'index.html', context)