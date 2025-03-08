from django.db import models

class Animal(models.Model):
    name = models.CharField("動物名稱", max_length=100)
    age = models.IntegerField("年齡")
    species = models.CharField("物種", max_length=100)
    weight = models.FloatField("體重")

    def __str__(self):
        return self.name
