from django.db import models

class Enquery(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # Assuming phone numbers will be stored as strings
    whatsapp_no = models.CharField(max_length=20, blank=False, null=True)  # Make it optional
    description = models.TextField(max_length=200)
    image = models.FileField(upload_to='images/',max_length=250,null=True)

# Create your models here.
