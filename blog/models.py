from tkinter import CASCADE
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
# post model
#user tables
class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
def post_pre_save(sender, instance ,*args, **kwargs):
    #print('pre save')
    if instance.slug is None:
        instance.slug = slugify(instance.title)
        #super().save(*args, **kwargs)
        
pre_save.connect(post_pre_save, sender=Post)
    
    
    
# post for comments
class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.body
    
#post likes
class Likes(models.Model):
    post = models.ForeignKey(Post, related_name='likes' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_likes' ,on_delete=models.CASCADE)
    likes = models.CharField(max_length=1)
    
    def __str__(self):
        return self.likes
