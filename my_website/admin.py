from django.contrib import admin
from .models import ArticleModel
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# admin.site.register(ArticleModel) #told to delete this

#does this even work?:
# @admin.register(ArticleModel) #is this the best name?
# class ArticleModelAdmin(SummernoteModelAdmin):  #is this the best name?
#     #field names in model:
#     # title/, article_body/, writer/, date written/, approved/, slug/, updated on/, blurb/, order/
#     list_display = ('writer', 'slug', 'date_written')
#     search_fields = ['writer', 'article_body']
#     list_filter = ('approved', 'date_written')
#     prepoulated_fields = {'slug': ('title',)}
#     summernote_fields = ('content',)
    
    
    
