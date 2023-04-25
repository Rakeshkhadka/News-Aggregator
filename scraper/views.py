from django.shortcuts import render, redirect
from .models import News
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

@login_required(login_url="/login/")
def index(request):
    
    news = News.objects.all()
    paginator = Paginator(news, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)
@login_required(login_url="/login/")
def index_by_category(request, category):
    # categories = News.CATEGORY_CHOICES
    news = News.objects.filter(category=category)
    paginator = Paginator(news, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,    
               }
    return render(request, 'index.html', context)


def search(request):
    query = request.GET.get('query') 
    if query:
        news = News.objects.filter(Q(title__icontains=query) | Q(category=query))  
    else:
        news = News.objects.all()  
    paginator = Paginator(news, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'query': query}  
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
            return redirect("login")
    
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
        if not user:
            return redirect('login')
        login(request, user)  
        return redirect('home')
            
    context = {
        
    }
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
