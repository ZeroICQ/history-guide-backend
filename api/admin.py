from django.contrib import admin
from .models import Location, Image, Place, LastUpdated


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    filter_horizontal = ('locations',)

@admin.register(LastUpdated)
class LastUpdatedAdmin(admin.ModelAdmin):
    pass
