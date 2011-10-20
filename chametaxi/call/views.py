from django.http import HttpResponse
from datetime import datetime

from models import TaxiRide

base_url = "http://localhost:8000/call/"

def callTaxi(request):
    """
    """
    user_id = request.GET['user_id']
    address = request.GET['address']
    lng = request.GET['lng']
    lat = request.GET['lat']

    ride = TaxiRide.objects.create(
        user_id=user_id,
        user_lng=lng,
        user_lat=lat,
        address=address,
        timestamp=datetime.now(),
        accepted=False,
        taxi_lng=0,
        taxi_lat=0
    )

    check_url = base_url + 'checkTaxi/?ride_id=' + str(ride.id)

    return HttpResponse('{status:"success", ride_id:%s, checkTaxiUrl:"%s"}'
                        % (ride.id, check_url))


def checkTaxi(request):
    """
    """
    ride = TaxiRide.objects.get(id=request.GET['ride_id'])

    if not ride:
        return HttpResponse('{status:"notRequested"}')

    if not ride.accepted:
        return HttpResponse('{status:"notYet"}')

    lat = ride.taxi_lat
    lng = ride.taxi_lng

    return HttpResponse('{status:"success", lat:"%s", lng:"%s"}'
                        % (lat, lng))

def listRides(request):
    """
    """
    rides = TaxiRide.objects.filter(accepted=False)
    rides = [ride.jsonUserInfo() for ride in rides]

    return HttpResponse('{status:"success", rides:%s}' % unicode(rides))


def acceptRide(request):
    """
    """
    ride_id = request.GET['ride_id']
    lng = request.GET['lng']
    lat = request.GET['lat']

    ride = TaxiRide.objects.get(id=ride_id)
    if ride.accepted:
        return HttpResponse('{status:"rideAlreadyAccepted"}')

    ride.acceptRide(lng, lat)

    return HttpResponse('{status:"success"}')

