from django.contrib.auth.models import AbstractUser
from django.db import models

class SiteUser(AbstractUser):
    nickname = models.CharField(max_length = 15)

    def __str__(self):
        return self.email