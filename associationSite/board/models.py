from django.db import models
from django.utils import timezone
from accounts.models import SiteUser
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin

class Board(models.Model, HitCountMixin):
    author = models.ForeignKey(SiteUser, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(help_text = 'Post content')
    created_date = models.DateTimeField(default = timezone.now)
    viewers = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(SiteUser, on_delete = models.CASCADE)
    post = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='comments')
    content = models.TextField(help_text = 'Conmment content')
    created_date = models.DateField(default = timezone.now)

    class Meta:
        ordering = ['-id']