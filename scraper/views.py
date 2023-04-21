from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse 
from .models import News

# Create your views here.

def scrape_ekantipur(request):
    base_url = "https://ekantipur.com"
    paths = ["/sports","/video", "/national", "/world", "/entertainment"]
    for path_ in paths:
        response = requests.get(base_url+path_, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        news = soup.find_all('article', {'class':'normal'})
    

        for article in news:
            titles = article.find_all('h2')
            image_source = article.find_all('img')
            url = article.find_all('a')

            
            
        # Create a new News object with the correct category/sport
            for title, img, u in zip(titles, image_source, url):
                news_title = title.get_text()
                url = base_url+u['href']
                
                category = next((choice[0] for choice in News.CATEGORY_CHOICES if choice[1] == path_.replace('/', '').title()), 'others')
                img_url = ""
                try:
                    img_url =  img['data-src']
                except:
                    pass 
                if not News.objects.filter(title__icontains=news_title).exists():
                    News.objects.create(title=news_title, img_src=img_url, url=url, category=category)
    
    return HttpResponse("hello")


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'index.html', context)