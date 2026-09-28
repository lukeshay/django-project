# from django.shortcuts import render
from playground.models import Dealership, Car
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class DealershipSerializer(ModelSerializer):
    class Meta:
        model = Dealership
        fields = '__all__'


# Create your views here.
class DealershipView(ModelViewSet):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer
    permission_classes = [IsAuthenticated]


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
