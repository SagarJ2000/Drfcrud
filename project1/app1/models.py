from django.db import models

# Create your models here.

class Post(models.Model):
    roll = models.IntegerField()
    fname = models.CharField(max_length=88)
    lname = models.CharField(max_length=99)

