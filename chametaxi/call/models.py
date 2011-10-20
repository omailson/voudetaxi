from django.db import models
from datetime import datetime

class TaxiRide(models.Model):
    user_lat = models.FloatField()
    user_lng = models.FloatField()
    user_id = models.FloatField()
    address = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    accepted = models.BooleanField()
    taxi_lat = models.FloatField()
    taxi_lng = models.FloatField()

    def jsonUserInfo(self):
        return {
            'ride_id': self.id,
            'ride_address': self.address,
            'lng': self.user_lng,
            'lat': self.user_lat
        }

    def acceptRide(self, lng, lat):
        self.taxi_lng = lng
        self.taxi_lat = lat
        self.accepted = True
        self.save()
