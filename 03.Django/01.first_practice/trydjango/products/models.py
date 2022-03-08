from django.db import models

# Create your models here.
class Garbage(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    admin = models.CharField(max_length=8, default='이창민')