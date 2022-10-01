from django.db import models

# Create your models here.


class products(models.Model):
    Name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop')