from .models import News




def categories(request):
    return {
       'all_categories': News.CATEGORY_CHOICES,
    }