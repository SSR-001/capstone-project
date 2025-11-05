from django.urls import path
from .views import ArticleList, MySubmissions
from . import views

urlpatterns = [
    path("my_submissions/", MySubmissions.as_view(), name="my_submissions"),
    path('articles/create/', views.create_or_edit_article,
         name='article_create'),
    path('articles/<int:pk>/edit/', views.create_or_edit_article,
         name='article_edit'),
    path('articles/<int:pk>/delete/', views.delete_article,
         name='article_delete'),
    path("", ArticleList.as_view(), name='home'),
]
