from django.shortcuts import render
from .utils import weather_api_request


def index(request):
    context = {}
    city = request.GET.get("city")
    if city:
        data: dict = weather_api_request.get_weather_request(city)
        context["name"] = data["location"]["name"]
        context["region"] = data["location"]["region"]
        context["country"] = data["location"]["country"]
        context["temp_c"] = data["current"]["temp_c"]
    return render(request, "weather/index.html", context=context)
