from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage, name='MainPage'),
    path('post/<slug:post_slug>', ArticlePage, name='ArticlePage'),
    path('category/<slug:post_slug>', CategoryPage, name='CategoryPage'),
    path('add/', AddPage, name='AddPage'),
    path('feedback/', FeedbackPage, name='FeedbackPage'),
    path('about/', AboutPage, name='AboutPage')
]