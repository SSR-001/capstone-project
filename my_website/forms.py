# from .models import Comment  #this was in the LMS/codestar. do i import article?
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'article_body')