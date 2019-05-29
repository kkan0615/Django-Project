from django.db import models
from django.utils import timezone
from accounts.models import SiteUser

class Board(models.Model):
    author = models.ForeignKey(SiteUser, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(help_text = 'Post content')
    created_date = models.DateTimeField(default = timezone.now)
    viewers = models.PositiveIntegerField(default = 0)
    likes = models.ManyToManyField(SiteUser, related_name = 'likes', blank = True)

    def __str__(self):
        return self.title

    # https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-4/
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    author = models.ForeignKey(SiteUser, on_delete = models.CASCADE)
    post = models.ForeignKey(Board, on_delete = models.CASCADE)
    content = models.TextField(help_text = 'Conmment content')
    created_date = models.DateField(default = timezone.now)