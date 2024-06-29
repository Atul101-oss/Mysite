from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')
    publication_date = models.DateField()

    def __str__(self):
        return self.title
