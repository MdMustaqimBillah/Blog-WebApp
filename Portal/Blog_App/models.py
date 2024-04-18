from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog_images/', null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title



class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.author.username + ' comments on ' + self.blog.title


class Likes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like')

    def __str__(self):
        return self.author.username + ' likes on ' + self.blog.title