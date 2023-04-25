import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse 
from .models import News


from celery import shared_task


categories = dict(News.CATEGORY_CHOICES)


def scrape_requirements(base_url: str, path: str, tag_name:str, class_name:str) -> list:
    response = requests.get(base_url+'/'+path, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = soup.find_all(tag_name, {'class':class_name})
    return news

@shared_task
def scrape_ekantipur():
    base_url = "https://ekantipur.com"
    paths = ["sports", "national", "world", "entertainment", "abc"]
    category = ['sports', 'national']
    for path_ in paths:
        # response = requests.get(base_url+'/'+path_, verify=False)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # news = soup.find_all('article', {'class':'normal'})
        news = scrape_requirements(base_url, path_, tag_name='article', class_name='normal')
    
        for article in news:
            my_dict = {}
            title=article.find('h2').get_text()
            my_dict['title'] = title
            my_dict['url'] = base_url+article.find('a')['href']
            my_dict['img_src'] = article.find('figure').find('img')['data-src']
            if path_ in categories:
                category = path_
            else:
                category = "others"
            my_dict['category']=category
            if not News.objects.filter(title=title).exists():
                News.objects.create(**my_dict)
    return "ekantipur scraped"



@shared_task
def scrape_nagarik():
    base_url = "https://nagariknews.nagariknetwork.com"
    paths = [ "politics", "economy", "arts", "sports"]
    for path_ in paths:
        news = scrape_requirements(base_url, path_, tag_name='article', class_name='list-group-item')
        for article in news:
            my_dict = {}
            info = article.find('a')
            # url = base_url+info['href']
            my_dict['url'] = base_url+info['href']
            # image_url = info.find('img')['data-src']
            my_dict['img_src'] = info.find('img')['data-src']
            title = info['title']
            my_dict['title']=title
            my_dict['category'] = path_ if path_ in categories else "others"
            # if paths_ in categories:
            #     category = paths_   
            # else:
            #     category = "others"
            # my_dict = {'title':title, 'img_src':image_url, 'url':url, 'category':category}
            if not News.objects.filter(title=title).exists():
                    News.objects.create(**my_dict)
    return "Nagirk news scraped"
