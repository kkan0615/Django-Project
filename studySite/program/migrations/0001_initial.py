# Generated by Django 2.2.1 on 2019-06-29 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, upload_to='program/cover')),
                ('title', models.CharField(max_length=20)),
                ('introduction', models.TextField(max_length=200)),
                ('url_key', models.CharField(max_length=10, unique=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('update_date', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('codes', models.ManyToManyField(to='program.Code')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=200)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('edit_date', models.DateField(blank=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Chapter')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program'),
        ),
    ]