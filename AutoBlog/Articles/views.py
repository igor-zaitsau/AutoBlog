from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

def MainPage(request):
    posts = ArticleModel.objects.all()
    categories = CategoryModel.objects.all()
    return render(request, 'Articles/allArticles.html', {'posts': posts, 'categories': categories})

def ArticlePage(request, post_id):
    post = ArticleModel.objects.get(pk=post_id)
    categories = CategoryModel.objects.all()
    return render(request, 'Articles/articlePage.html', {'post': post, 'categories': categories})


def CategoryPage(request, cat_id):
    posts = ArticleModel.objects.filter(category_id=cat_id)
    categories = CategoryModel.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'cat_selected': cat_id
    }

    return render(request, 'Articles/allArticles.html', context)




def AddPage(request):
    return render(request, 'Articles/addArticle.html')

def FeedbackPage(request):
    return render(request, 'Articles/feedbackPage.html')

def AboutPage(request):
    return render(request, 'Articles/aboutPage.html')