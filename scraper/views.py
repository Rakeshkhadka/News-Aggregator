from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
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


def search(request):
    query = request.GET.get('query')  # get the search query from the GET parameters
    if query:
        news = News.objects.filter(title__icontains=query)  # search the News model for the query in the title field
    else:
        news = News.objects.all()  # if no query, return all News objects
    context = {'news': news, 'query': query}  # pass the query and search results to the template
    return render(request, 'search.html', context)