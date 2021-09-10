from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User,related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=256, verbose_name= 'Put a Title')
    slug = models.SlugField(max_length=256,unique=True)
    blog_content  = models.TextField(max_length=2000,verbose_name='Whats in your mind?')
    blog_image = models.ImageField(upload_to='blog_image',verbose_name='Blog_Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']
    
    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_like')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='liker_user')


