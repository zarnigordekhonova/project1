from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()



    def __str__(self):
        return f'{self.title} {self.author}'



class Books_description(models.Model):
    color_cover = models.CharField(max_length=255)
    cover_type = models.CharField(max_length=255)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.color_cover} {self.cover_type}'