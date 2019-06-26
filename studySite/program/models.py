from django.db import models
from account.models import User
from django.utils import timezone

class Code(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return str(self.name)

class Program(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='program/cover', blank=True)
    title = models.CharField(max_length=20)
    introduction = models.TextField(max_length=200)
    url_key = models.CharField(max_length=10, unique=True)
    codes = models.ManyToManyField(Code)
    created_date = models.DateField(default = timezone.now)
    update_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.pk

class Chapter(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    number = models.IntegerField(blank=False)
    created_date = models.DateField(default = timezone.now)

    def __str__(self):
        return self.pk

class subject(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    created_date = models.DateField(default = timezone.now)
    edit_date = models.DateField(blank=True)

    def __str__(self):
        return self.pk

class subject_comment(models.Model):
    subject = models.ForeignKey(Program, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.pk