from django.db import models


# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#-------
class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Word(models.Model):
    word = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.word