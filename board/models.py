from django.db import models
from django.conf import settings
from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #1 POST :N WRITERS

    # like N:M USER
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)


class PostImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

