# Generated by Django 5.1.6 on 2025-02-19 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=1000)),
                ('start_title', models.CharField(blank=True, max_length=300, null=True)),
                ('end_title', models.CharField(blank=True, max_length=300, null=True)),
                ('post_start', models.TextField(max_length=3000)),
                ('post_end', models.TextField(blank=True, max_length=3000, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('continues_max', models.PositiveIntegerField(default=0)),
                ('published', models.DateTimeField(auto_now=True)),
                ('changed', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Public', 'Public')], default='Draft', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostContinue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.PositiveIntegerField()),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('text', models.TextField(max_length=3000)),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField()),
                ('changed', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cwapp.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('created', models.DateTimeField()),
                ('changed', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cwapp.post')),
                ('post_continue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cwapp.postcontinue')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
