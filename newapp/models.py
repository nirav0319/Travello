from django.db import models


# Create your models here.
class destination(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=30)
    price=models.IntegerField()
    img=models.ImageField(max_length=40)
