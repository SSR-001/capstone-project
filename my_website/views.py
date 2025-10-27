from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticleModel  #do I need this?
from django.views import generic

# Create your views here.
# def home_page_view(request):
#     return HttpResponse("Hello, World!")

class ArticleList(generic.ListView):
    queryset = ArticleModel.objects.filter(approved=1)
    