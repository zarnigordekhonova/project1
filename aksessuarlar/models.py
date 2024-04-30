from django.db import models

# Create your models here.

class aksessuar(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.IntegerField()


    def __str__(self):
        return f'{self.name} {self.make}'


class Orders(models.Model):
    users_info = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    number_of_orders = models.IntegerField()


    def __str__(self):
        return f'{self.users_info} {self.email}'