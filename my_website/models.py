from django.db import models
# from other-app.models import OtherModel
from django.contrib.auth.models import User

# Create your models here.


# SOME HERE TO DO LATER:
STATUS = ((0, "Draft"), (1, "Published"))
class Article (models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    article_body = models.TextField()
    date_written = models.DateTimeField(auto_now_add=True)
    # image = CloudinaryField('image', default='placeholder') #is this right?
    approved = models.IntegerField(choices=STATUS, default = 0)
    blurb = models.TextField(blank=True)
    when_updated = models.DateTimeField(auto_now=True)
    # articles_order = models.IntegerField()
    # class Meta:
    #     ordering = ???
    
    #this must come after the Meta class if I have one:
    def __str__(self):
        return f"{self.title}"