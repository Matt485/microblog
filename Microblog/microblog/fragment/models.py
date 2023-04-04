from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
    blog_name = models.CharField(max_length=1000)
    url_stem = models.SlugField(max_length=30)
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Post(models.Model):
    post_date = models.DateTimeField('date created', default=timezone.now)
    post_text = models.CharField(max_length=200) 
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

    def __str__(self):
        return self.post_text[0:20]

class TextPost(Post):
    post_text_extra = models.CharField(max_length=1000)

class AudioPost(Post):
    post_audio = models.BinaryField(max_length=10000000)
