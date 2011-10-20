from django.http import HttpResponse

from models import TaxiRide

base_url = "http://localhost:8000/call/"

def callTaxi(request):
    """
    """
    ride = TaxiRide()
    ride.initNull()

    ride.user_id = request.GET['user_id']
    ride.lng = request.GET['lng']
    ride.lat = request.GET['lat']

    ride.save()

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

def listRide(request):
    """
    """
    rides = TaxiRide.objects.filter(accepted=False)
    rides = [{'lng':ride.lng, 'lat': ride.lat, 'ride_id': ride.id}
             for ride in rides]

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

    ride.taxi_lng = lng
    ride.taxi_lat = lat
    ride.accepted = True
    ride.save()

    return HttpResponse('{status:"success"}')

