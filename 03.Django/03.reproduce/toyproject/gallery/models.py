from django.db import models

TYPE = [('photo', 'photo'), ('painting', 'painting'), ('sculpture', 'sculpture'), ('video', 'video'), ('print', 'print')]

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    explanation = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    type = models.CharField(max_length=20, choices=TYPE, default='photo')

    def __str__(self):
        return self.workname

    class Meta:
        ordering = ['-created_at']