from zoneinfo import ZoneInfo

from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.viewsets import ModelViewSet

from playground.models import Dealership


class DealershipSerializer(ModelSerializer):
    class Meta:
        model = Dealership
        fields = "__all__"

    def validate_timezone(self, value):
        try:
            ZoneInfo(value)
            return value
        except:
            raise ValidationError("Must be a valid timezone")


# Create your views here.
class DealershipViewSet(ModelViewSet):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer


# TODO: Create the car view set
