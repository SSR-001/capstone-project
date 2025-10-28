from django.urls import path
# from .views import home_page_view
from .views import ArticleList, MySubmissions

urlpatterns = [
    path("my_submissions/", MySubmissions.as_view(), name="my submissions"),
    # path("", home_page_view),
    path("", ArticleList.as_view(), name='home'),
]