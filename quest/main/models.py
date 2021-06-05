from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_NULL, null=True)
    col = models.CharField(max_length=255)
    ultimate = models.IntegerField()
    descriptions = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=512)

    def __str__(self):
        return self.col
