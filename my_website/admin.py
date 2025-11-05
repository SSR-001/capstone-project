from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    # field names in the model:
    # title, article_body, writer, date_written, ready_for_approval, approved, when_updated
    list_display = ('title', 'writer', 'ready_for_approval', 'approved',)
    search_fields = ['article_body']
    list_filter = ('approved', 'date_written')
    summernote_fields = ('content',)
