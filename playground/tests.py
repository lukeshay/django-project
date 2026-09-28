import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_api_client(api_client):
    User = get_user_model()
    user = User.objects.create(
    )

    api_client.force_login(user)

    return api_client


# Create your tests here.
@pytest.mark.django_db
class TestDealershipView:
    pass
