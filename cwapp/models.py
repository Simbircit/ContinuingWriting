from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images', default='avatar.jpg')


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, default='')
    start_title = models.CharField(max_length=300, null=True, blank=True)
    end_title = models.CharField(max_length=300, null=True, blank=True)
    post_start = models.TextField(max_length=3000)
    post_end = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(upload_to='images')

    continues_max = models.PositiveIntegerField(default=0)
    continues_count = models.PositiveIntegerField(default=0)
    published = models.DateTimeField(auto_now=True)
    changed = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class PostStatus(models.TextChoices):

        draft = 'Draft'
        public = 'Public'

    status = models.CharField(max_length=6, choices=PostStatus.choices, default=PostStatus.draft)


class PostContinue(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    chapter = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True, blank=True)
    text = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    changed = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    post_continue = models.ForeignKey(PostContinue, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    changed = models.DateTimeField(auto_now_add=True)
