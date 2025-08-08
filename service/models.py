from django.db import models

class Service(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)

class product(models.Model):
    image= models.ImageField(),
    price= models.IntegerField(null=True, blank=True)
