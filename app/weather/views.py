from django.shortcuts import render
from .utils import weather_api_request


def index(request):
    return render(request, "weather/index.html")


def get_weatherforecast_data(request):
    data = weather_api_request.get_weather_request("Kirov")
    return render(
        request, "weather/get_weatherforecast_data.html", context=data
    )
