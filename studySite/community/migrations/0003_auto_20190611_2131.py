# Generated by Django 2.2.1 on 2019-06-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_community_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='url_key',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
