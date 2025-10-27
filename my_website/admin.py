from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# admin.site.register(Article) #told to delete this

# does this even work?:
@admin.register(Article) #is this the best name?
class ArticleAdmin(SummernoteModelAdmin):  #is this the best name?
    #field names in model:
    # title/, article_body/, writer/, date written/, approved/, slug/, updated on/, blurb/, order/
    list_display = ('slug', 'date_written') #"writer" taken out of this
    search_fields = ['article_body'] #"writer" taken out of this
    list_filter = ('approved', 'date_written')
    prepoulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
    
    
