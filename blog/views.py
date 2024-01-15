from django.shortcuts import render
from django.http import HttpResponse 
from .models import Article, Author

def article(request):
    articles = Article.objects.all()
    return articles
    