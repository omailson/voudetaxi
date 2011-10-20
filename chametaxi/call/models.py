from django.db import models
from datetime import datetime

class TaxiRide(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    user_id = models.FloatField()
    timestamp = models.DateTimeField()
    accepted = models.BooleanField()
    taxi_lat = models.FloatField()
    taxi_lng = models.FloatField()

    def initNull(self):
        self.taxi_lat = 0
        self.taxi_lng = 0
        self.accepted = False
        self.timestamp = datetime.now()
