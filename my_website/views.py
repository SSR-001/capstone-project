from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  #do I need this?
from django.views import generic

# Create your views here.
# def home_page_view(request):
#     return HttpResponse("Hello, World!")

class ArticleList(generic.ListView):
    queryset = Article.objects.filter(approved=1)
    template_name = "my_website/article_list.html"
    # paginate_by = 6

class MySubmissions(generic.ListView):
    queryset = Article.objects.filter(approved=0)
    template_name = "my_website/my_submissions.html"