from django.db import models

# Create your models here.
class Post(models.Model):
    post_heading=models.CharField(max_length=200)
    post_text=models.TextField()
    post_author=models.CharField(max_length=100, default='anonymous')
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)