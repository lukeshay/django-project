from django.urls import path, include
from rest_framework import routers
# from rest_framework_nested import routers

from playground.views import DealershipViewSet

# add urls here
router = routers.DefaultRouter()

router.register("dealerships", DealershipViewSet)

# TODO: Add the car view set to the urls

urlpatterns = [
    path(r'', include(router.urls)),
]
