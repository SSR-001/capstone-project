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
    queryset = Article.objects.filter(approved=1)
    template_name = "my_website/article_list.html"
    # paginate_by = 6

#trying to get AI to re-write this as a function so I can use the last line, "article-form"
class MySubmissions(generic.ListView):
    queryset = Article.objects.filter(approved=0)
    template_name = "my_website/my_submissions.html"
    # article_form = ArticleForm() # I didn't do this exactly as the LMS did because their thing was a function, not a class






#from AI:

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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
            obj.save()
            # adjust redirect target to where you want to go after save
            
            return redirect('/my_submissions/')  # or 'article_detail', '/' etc.
        
        # if invalid: fall through and render template with form.errors
    else:
        form = ArticleForm(instance=article) if article else ArticleForm()

    return render(request, "my_website/create_or_edit_article.html", {
        "form": form,
        "article": article,
    })