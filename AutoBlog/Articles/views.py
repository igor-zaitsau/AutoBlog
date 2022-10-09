from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

def MainPage(request):
    posts = ArticleModel.objects.all()
    return render(request, 'Articles/allArticles.html', {'posts': posts})

def ArticlePage(request, post_id):
    return render(request, 'Articles/articlePage.html', {'post_id': post_id})

def AddPage(request):
    return render(request, 'Articles/addArticle.html')

def FeedbackPage(request):
    return render(request, 'Articles/feedbackPage.html')

def AboutPage(request):
    return render(request, 'Articles/aboutPage.html')