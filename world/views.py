import json
import requests  # Import the requests library
from django.http import JsonResponse
from django.shortcuts import render

def map_view(request):
    return render(request, 'map.html')

def nearby_restaurants(request):
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))

    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node["amenity"="restaurant"](around:5000, {lat}, {lng});
    out;
    """

    # Send the request to Overpass API
    response = requests.get(overpass_url, params={'data': query})  # Use requests.get
    data = response.json()

    # Extract relevant information
    restaurants = [
        {
            "name": element.get("tags", {}).get("name", "Unnamed Restaurant"),  # Fix typo
            "lat": element["lat"],
            "lng": element["lon"],
            "address": element.get("tags", {}).get("addr:street", "Address not available"),  # Fix key to addr:street
        }
        for element in data["elements"]
    ]

    return JsonResponse(restaurants, safe=False)
