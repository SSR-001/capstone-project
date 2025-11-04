from django.db import models
from django.contrib.auth.models import User

# Create your models here.


STATUS = ((0, "Draft"), (1, "Published"))
REQUESTAPPROVAL = ((0, "Not Ready For Approval"), (1, "Ready For Approval"))


class Article (models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    article_body = models.TextField()
    date_written = models.DateTimeField(auto_now_add=True)
    ready_for_approval = models.IntegerField(choices=REQUESTAPPROVAL,
        default=0)
    approved = models.IntegerField(choices=STATUS, default=0)
    blurb = models.TextField(blank=True)
    when_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"