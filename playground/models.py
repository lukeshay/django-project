from django.db import models


# Create your models here.
class Dealership(models.Model):
    name = models.CharField(
        max_length=64
    )
    timezone = models.CharField(
        max_length=64
    )
    address1 = models.CharField(
        max_length=512
    )
    address2 = models.CharField(
        max_length=512,
        null=True,
    )
    city = models.CharField(
        max_length=64,
    )
    state = models.CharField(
        max_length=2,
    )
    zipcode = models.CharField(
        max_length=5,
    )
