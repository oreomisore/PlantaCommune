from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)


class Post(models.Model):
    img = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=225)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    author = models.CharField(default='')
    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



