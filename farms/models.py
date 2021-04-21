from datetime import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Picture(models.Model):
    image = models.ImageField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey("content_type", "object_id")


class Address(models.Model):
    street_and_number = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=30)
    additional_info = models.CharField(max_length=30, blank=True, null=True)
    registration_document = models.FileField(null=True)


class Farm(models.Model):
    name = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.OneToOneField(
        Address,
        on_delete=models.SET_NULL,
        null=True
    )


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
    pictures = GenericRelation(Picture)


class Fair(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address,
        on_delete=models.SET_NULL,
        null=True
    )
    farms = models.ManyToManyField(Farm)
    when = models.CharField(max_length=100)
    periodical = models.BooleanField(default=True)
    organizer = models.CharField(max_length=100)
    email = models.EmailField()
    pictures = GenericRelation(Picture)

    def __str__(self):
        return f"Fair {self.name}"
