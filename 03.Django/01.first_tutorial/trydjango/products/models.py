from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField
    description = models.TextField()
    price = models.IntegerField()
    admin = models.TextField(default='이창민')
