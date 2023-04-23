import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse 
from .models import News


from celery import shared_task


@shared_task
def scrape_ekantipur():
    base_url = "https://ekantipur.com"
    paths = ["/sports", "/national", "/world", "/entertainment"]
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
    
    return "ekantipur scraped"

def scrape_nagarik():
    base_url = "https://nagariknews.nagariknetwork.com"
    paths = [ "/politics", "/economy", "/arts", "/sports"]
    for paths_ in paths:
        response = requests.get(base_url+paths_, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        news = soup.find_all('article', {'class':'list-group-item'})
        for article in news:
            h1_tages = article.find_all('h1') #h1
            images = article.find('figure').find_all('img') #gives image and url
            urls = article.find('figure').find_all('a')
            for h1, imag, url in zip(h1_tages, images, urls):
                img_url = ''
                category = next((choice[0] for choice in News.CATEGORY_CHOICES if choice[1] == paths_.replace('/', '').title()), 'others')
                print(imag['data-src'])
                try:
                    img_url = imag['data-lazy']
                except:
                    img_url = imag['data-src']
                print(h1.get_text())
                news_title = h1.get_text()
                print(url['href'])
                nurl = base_url + url['href']
                if not News.objects.filter(title__icontains=news_title).exists():
                    News.objects.create(title=news_title, img_src=img_url, url=nurl, category=category)
    return "Nagirk news scraped"     