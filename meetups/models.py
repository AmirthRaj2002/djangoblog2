from tkinter import CASCADE
from turtle import title
from django.db import models
from django.urls import reverse
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# User=get_user_model()

# Create your models here.
class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

        
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    def __str__(self) :
        return self.name
        
class Post(models.Model) :
    class newmanager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
        
    options=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=50,unique=True)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=options,default='draft')
    objects=models.Manager()
    Newmanager=newmanager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("meetups:post_single", args={self.title})
    

class Comments(models.Model):
    post=models.ForeignKey(Post,to_field='title',on_delete=models.CASCADE)
    content=models.TextField()
    def __str__(self):
        return self.content
    