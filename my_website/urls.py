from django.urls import path
# from .views import home_page_view
from .views import ArticleList

urlpatterns = [
    # path("", home_page_view),
    path("", ArticleList.as_view(), name='home'),
]