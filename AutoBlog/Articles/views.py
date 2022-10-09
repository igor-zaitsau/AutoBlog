from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def MainPage(request):
    return HttpResponse('Hello dear')