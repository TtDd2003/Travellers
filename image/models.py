from django.db import models

class Image(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/%y')
    experience = models.CharField(max_length=200)

    def __str__(self):
     return f"{self.caption} - {self.experience} - {self.image.name}"


# Create your models here.
