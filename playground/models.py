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
    postal_code = models.CharField(
        max_length=5,
    )


class TransmissionChoices(models.TextChoices):
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class Car(models.Model):
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, related_name="cars")

    make = models.CharField(
        max_length=32
    )
    model = models.CharField(
        max_length=64
    )
    trim_level = models.CharField(
        max_length=8
    )
    vin_number = models.CharField(
        max_length=17
    )
    transmission = models.CharField(
        max_length=9,
        choices=TransmissionChoices.choices,
    )
    street_datetime = models.DateTimeField()
