from django.db import models

# Create your models here.
class Course(models.Model):

    price = models.IntegerField()
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="pics")
    duration = models.TextField()
    description = models.TextField()
    