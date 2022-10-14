from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

def MainPage(request):
    posts = ArticleModel.objects.all().order_by('-time_update')
    categories = CategoryModel.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'title': 'Главная'
    }

    return render(request, 'Articles/allArticles.html', context)

def ArticlePage(request, post_slug):
    post = ArticleModel.objects.get(slug=post_slug)
    categories = CategoryModel.objects.all()
    return render(request, 'Articles/articlePage.html', {'post': post, 'categories': categories})


def CategoryPage(request, post_slug):
    posts = ArticleModel.objects.filter(category__slug=post_slug)
    categories = CategoryModel.objects.all()


    context = {
        'posts': posts,
        'categories': categories,
        'slug_selected': post_slug
    }

    return render(request, 'Articles/allArticles.html', context)




def AddPage(request):
    return render(request, 'Articles/addArticle.html', {'title': 'Добавить'})

def FeedbackPage(request):
    return render(request, 'Articles/feedbackPage.html', {'title': 'Обратная связь'})

def AboutPage(request):
    return render(request, 'Articles/aboutPage.html', {'title': 'О нас'})