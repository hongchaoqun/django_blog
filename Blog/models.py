from django.db import models
from django.utils import timezone
from django.contrib.auth import User

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300, help_text="标题")
    author = models.ForeignKey(User, related_name="blog_posts", help_text="作者")
    body = models.TextField(help_text="文章")
    publish = models.DateTimeField(default=timezone.now)

    class Mate:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
