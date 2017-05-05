from django.db import models

# from django.db.models.signals import post_delete
# from django.dispatch.dispatcher import receiver


class Location(models.Model):
    # TODO: improve by adding min and max value
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return 'lat: %f long: %f' % (self.latitude, self.longitude)

    class Meta:
        unique_together = ("latitude", "longitude")


class Place(models.Model):
    name = models.CharField(max_length=500, unique=True, default='')
    description = models.TextField(null=False, default='')
    locations = models.ManyToManyField(Location)
    main_full = models.ImageField(upload_to='places/main_full/', blank=True, null=True)
    main_thumb = models.ImageField(upload_to='places/main_thumb/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Image(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    full = models.ImageField(upload_to='places/additional/')
    thumbnail = models.ImageField(upload_to='places/additional_thumb/', null=True, blank=True)

    def __str__(self):
        return '%s for %s' % (self.full.url, self.place.name)

class LastUpdated(models.Model):
    date = models.DateTimeField()

# Receive the pre_delete signal and delete the file associated with the model instance.
'''@receiver(post_delete, sender=Place)
def place_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
'''
