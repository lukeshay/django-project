import pytest
from rest_framework.test import APIClient
from faker import Faker
from playground.models import Dealership

fake = Faker()


def create_dealership():
    Dealership.objects.create(
        name=fake.company(),
        timezone=fake.timezone(),
        address1=fake.street_address(),
        city=fake.city(),
        state=fake.state_abbr(),
        zipcode=fake.zipcode(),
    )

# Create your tests here.