from django.shortcuts import render, redirect
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


from .forms import UserForm
def registerUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
    
    
    context = {
        'form':form
    }
    return render(request, 'register.html', context)


from django.contrib.auth import authenticate, login, logout
def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)  
            return redirect('home')
        else:
            return redirect('login')
    context = {
        
    }
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
        