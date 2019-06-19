from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.

class Community(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default='noname')
    introduction = models.TextField(max_length=200)
    url_key = models.CharField(max_length=10, unique=True)
    created_date = models.DateField(default = timezone.now)

    def __str__(self):
        return str(self.title)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(help_text = 'Post content')
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.pk
