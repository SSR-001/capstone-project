from django.urls import path
# from .views import home_page_view
from .views import ArticleList, MySubmissions
from . import views #this is from AI

urlpatterns = [
    path("my_submissions/", MySubmissions.as_view(), name="my submissions"),
    path('articles/create/', views.create_or_edit_article, name='article_create'), #this is from AI
    path('articles/<int:pk>/edit/', views.create_or_edit_article, name='article_edit'), #this is from AI
    # path("", home_page_view),
    path("", ArticleList.as_view(), name='home'),
]