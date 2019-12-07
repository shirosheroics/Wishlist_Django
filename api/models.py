from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=120)
    url = models.URLField(max_length=255, null=True, blank=True)
    checker = models.CharField(max_length=255, null=True, blank=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
