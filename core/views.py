from django.shortcuts import render
from django.http.response import JsonResponse
from .models import EVChargingLocation
from geopy.distance import geodesic

# Create your views here.


def index(request):
    stations = list(EVChargingLocation.objects.values(
        'longitude', 'latitude')[:100])
    context = {
        "stations": stations
    }
    return render(request, 'index.html', context)


def nearest_location(request):
    latitude = request.GET.get("latitude")
    longitude = request.GET.get("longitude")
    user_location = latitude, longitude
    # print(f'{longitude} and {latitude}')
    station_distances = {}
    for station in EVChargingLocation.objects.all()[:100]:
        station_location = station.latitude, station.longitude
        distance = geodesic(user_location, station_location).km
        station_distances[distance] = station_location
        min_distance = min(station_distances)
        station_coords = station_distances[min_distance]

    return JsonResponse({
        "coordinates": station_coords,
        "distance": min_distance
    })
