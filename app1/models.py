from django.db import models

# Create your models here.
class electronics(models.Model):
    electronic_id =  models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/')