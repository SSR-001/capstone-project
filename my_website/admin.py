from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'writer', 'ready_for_approval', 'approved',)
    search_fields = ['article_body']
    list_filter = ('approved', 'date_written')
    summernote_fields = ('content',)
