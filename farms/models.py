from django.db import models
from datetime import datetime


class Farm(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=22, decimal_places=16)


class Farmer(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.EmailField()

    @property
    def age(self):
        # approximately :)
        return (datetime.today().date() - self.birthday).days // 365


class Animal(models.Model):
    class Species(models.TextChoices):
        COW = 'COW', 'cow'
        DUCK = 'DUC', 'duck'
        HORSE = 'HOR', 'horse'
        CHICKEN = 'CHI', 'chicken'
        NAN = 'NAN', 'not_identified_yet'

    specie = models.CharField(
        max_length=3,
        choices=Species.choices,
    )
    farm = models.ForeignKey(Farm, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField()
