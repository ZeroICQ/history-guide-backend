from rest_framework import generics
from .models import Place, Location, LastUpdated
from .serializers import PlaceListSerializer, PlaceDetailSerializer, LocationSerializer, LastUpdatedSerializer
from django.db.models import Func, F

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceListSerializer


class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer

class LastUpdatedView(generics.ListAPIView):
    queryset = LastUpdated.objects.all()
    serializer_class = LastUpdatedSerializer
