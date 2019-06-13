from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length = 15)
    introduction = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.pk