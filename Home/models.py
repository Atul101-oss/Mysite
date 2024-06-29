from django.db import models

# Create your models here.
class Books(models.Model):
    bID = models.CharField(max_length=20,primary_key=True)
    bName = models.CharField(max_length=50)
    bDescription = models.CharField(max_length=300)
