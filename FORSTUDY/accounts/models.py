# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class BlogUserManager(BaseUserManager):
    def create_user(self, email, nickname, password = None):
        if not email:
            raise ValueError('User must have email')

        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
        )

        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
        )

        user.is_admin = True
        user.save(using = self._db)
        return user


class BlogUser(AbstractBaseUser):
    #고유 식별 unique 64 bytes of id. Instead of id
    uuid = models.UUIDField(
        primary_key = True,
        unique = True,
        editable = False,
        default = uuid.uuid4,
        verbose_name = 'PK'
    )

    email = models.EmailField(unique = True)
    nickname = models.CharField(max_length  = 20)
    date_join = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True) # Active
    is_admin = models.BooleanField(default = False) # Admin

    objects = BlogUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return True

    def has_moudle_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin