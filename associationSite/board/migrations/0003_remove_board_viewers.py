# Generated by Django 2.2.1 on 2019-06-04 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20190603_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='viewers',
        ),
    ]