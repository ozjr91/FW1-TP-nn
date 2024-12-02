from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn=models.CharField(max_length=30, unique=True)
    backCover=models.TextField()
    cover=models.BooleanField(default=False)

    def __str__(self):
        return self.title