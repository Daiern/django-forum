from django.conf import settings
from django.db import models


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=250)
    text = models.CharField(max_length=1000)
    createdDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

    def get_body(self):
        return self.text

    def get_date(self):
        return self.createdDate

    def get_author(self):
        return self.author


class Comment(models.Model):
    parentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    createdDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
