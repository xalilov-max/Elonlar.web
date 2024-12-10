from django.shortcuts import render, redirect
from .models import Category, News

def homepage(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'homepage.html', context)

def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        news = News(title=title, content=content, image=image, category=category)
        news.save()
        return redirect('homepage')
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'add_news.html', context)


def select_by_category(request, category_id):
    categories = Category.objects.all()
    news = News.objects.filter(category=category_id)
    context = {
        'categories': categories,
        'news': news,

    }
    return render(request, 'homepage.html', context)

def news_detail(request, news_id):
    categories = Category.objects.all()
    news = News.objects.get(id=news_id)
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news_detail.html', context)

