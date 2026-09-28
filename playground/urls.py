from django.urls import path, include
from playground.views import DealershipView, CarView
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register("dealerships", DealershipView)

dealerships_nested_router = routers.NestedDefaultRouter(router, "dealerships")
dealerships_nested_router.register("cars", CarView)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(dealerships_nested_router.urls)),
]
