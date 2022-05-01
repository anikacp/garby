from django.db import models

# Create your models here.


class CUser(models.Model):
    username = models.CharField(max_length=100, verbose_name="username")
    full_name = models.CharField(max_length=100, verbose_name="full name")
    points = models.IntegerField(default=0)
    redeemed = models.IntegerField(default=0)
