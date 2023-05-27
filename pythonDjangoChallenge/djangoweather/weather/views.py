import requests
from django.shortcuts import render

def weather_map(request):
    # Fetch weather data from the National Weather Service API
    api_url = 'https://www.weather.gov/documentation/services-web-api'
    # latitude = '37.7749'  # Example latitude
    # longitude = '-122.4194'  # Example longitude
    # url = api_url.format(latitude=latitude, longitude=longitude)
    response = requests.get(api_url)
    data = response.json()

    # Process weather data to get geolocations
    locations = []
    for forecast in data['properties']['periods']:
        location = {
            'name': forecast['name'],
            'city': forecast['city'],
        }
        locations.append(location)

    # Pass locations to the template
    context = {'locations': locations}
    return render(request, 'weather/weather_tem.html', context)

