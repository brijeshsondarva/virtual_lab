from django.db import models

# Create your models here.
class Slideshow(models.Model):
    img = models.ImageField(upload_to="pics")

class Teams(models.Model):
    img = models.ImageField(upload_to = "teams")
    name =  models.TextField(max_length=100)
    designation = models.TextField(max_length=50)
    