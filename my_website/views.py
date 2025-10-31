# see the imports in the ai's thing below
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article  #do I need this?
from django.views import generic
from .forms import ArticleForm

# Create your views here.
# def home_page_view(request):
#     return HttpResponse("Hello, World!")

class ArticleList(generic.ListView):
    queryset = Article.objects.filter(approved=1).order_by('-date_written')
    template_name = "my_website/article_list.html"
    # paginate_by = 6

#trying to get AI to re-write this as a function so I can use the last line, "article-form"
class MySubmissions(generic.ListView):
    template_name = "my_website/my_submissions.html"
    # article_form = ArticleForm() # I didn't do this exactly as the LMS did because their thing was a function, not a class
    
    def get_queryset(self):
        # Show all articles by the current user (both draft and published)
        return Article.objects.filter(writer=self.request.user).order_by('-date_written')






#from AI:

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

@login_required
def create_or_edit_article(request, pk=None):
    """
    If pk is None -> create new Article.
    If pk is provided -> edit Article with that pk.
    Template: create_or_edit_article.html
    Context: {'form': form, 'article': article_or_None}
    """
    article = None
    if pk:
        article = get_object_or_404(Article, pk=pk)

        # If your model has a writer field and you want only owners to edit:
        if hasattr(article, 'writer') and article.writer is not None:
            if article.writer != request.user:
                return HttpResponseForbidden("You may only edit your own articles.")

    if request.method == "POST":
        # bind the form to POST; pass instance for edit
        form = ArticleForm(request.POST, instance=article) if article else ArticleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            # Always set writer for new articles; preserve existing writer when editing
            if not obj.pk:  # new article (no primary key yet)
                obj.writer = request.user
            
            # Handle the ready_for_approval checkbox
            if request.POST.get('ready_for_approval') == '1':
                obj.ready_for_approval = 1
            else:
                obj.ready_for_approval = 0
            
            obj.save()
            # adjust redirect target to where you want to go after save
            
            # Add success message
            if pk:
                messages.success(request, 'Article updated successfully!')
            else:
                messages.success(request, 'Article created successfully!')
            
            return redirect('/my_submissions/')  # or 'article_detail', '/' etc.
        
        # if invalid: fall through and render template with form.errors
    else:
        form = ArticleForm(instance=article) if article else ArticleForm()

    return render(request, "my_website/create_or_edit_article.html", {
        "form": form,
        "article": article,
    })
    
@login_required
def delete_article(request, pk):
    """
    Delete an article. Only the owner can delete.
    """
    article = get_object_or_404(Article, pk=pk)
    
    # Check if user is the owner
    if hasattr(article, 'writer') and article.writer != request.user:
        return HttpResponseForbidden("You can only delete your own articles.")
    
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully!')
        return redirect('my_submissions')
    
    # If not POST, redirect to my subs
    return redirect('my_submissions')