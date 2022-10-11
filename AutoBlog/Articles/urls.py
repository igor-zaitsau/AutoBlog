from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage, name='MainPage'),
    path('post/<int:post_id>', ArticlePage, name='ArticlePage'),
    path('category/<int:cat_id>', CategoryPage, name='CategoryPage'),
    path('add/', AddPage, name='AddPage'),
    path('feedback/', FeedbackPage, name='FeedbackPage'),
    path('about/', AboutPage, name='AboutPage')
]