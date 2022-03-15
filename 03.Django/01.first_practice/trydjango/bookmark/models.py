from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('제목', max_length=80)
    url = models.URLField('주소', unique=True)
    writer = models.CharField('작성자', max_length=20)