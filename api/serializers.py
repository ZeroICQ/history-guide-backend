from rest_framework import serializers
from .models import Image, Location, Place, LastUpdated

class LastUpdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastUpdated
        fields = ('date',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('full', 'thumbnail')


class LocationSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_value=360, min_value=-360, max_digits=9, decimal_places=6, coerce_to_string=False)
    longitude = serializers.DecimalField(max_value=360, min_value=-360, max_digits=9, decimal_places=6, coerce_to_string=False)

    class Meta:
        model = Location
        fields = ('latitude', 'longitude',)


class PlaceListSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'locations', 'description', 'main_full', 'main_thumb', 'images')


class PlaceDetailSerializer(PlaceListSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'locations', 'main_full', 'main_thumb', 'images')
