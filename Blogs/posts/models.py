from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField
from django.db.models.signals import pre_save
from django.utils.text import slugify

User = get_user_model()

# Create your models here.
class contact_us(models.Model):
    name = models.CharField(max_length=100,null=True)
    Email_address = models.EmailField(max_length=100,null=True)
    message = models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.name
    

class subscription(models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        return self.email

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Poster(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    profile_picture = models.ImageField(null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title','slug')

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Poster', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

  
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Poster', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    