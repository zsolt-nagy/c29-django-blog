from django.db import models
import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField(default=datetime.date.today)
