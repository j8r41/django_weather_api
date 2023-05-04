from django.shortcuts import render
from .utils import weather_api_request


def index(request):
    context = {}
    city = request.GET.get("city")
    if city:
        data: dict = weather_api_request.get_weather_request(city)
        if data.get('error'):
            context["error"] = data["error"]["message"]
        else:
            context["city"] = data["location"]["name"]
            context["region"] = data["location"]["region"]
            context["country"] = data["location"]["country"]
            context["temp_c"] = data["current"]["temp_c"]
            context["feelslike_c"] = data["current"]["feelslike_c"]
            context["condition_text"] = data["current"]["condition"]["text"]
            context["condition_icon"] = data["current"]["condition"]["icon"]
            context["wind_kph"] = data["current"]["wind_kph"]
            context["wind_dir"] = data["current"]["wind_dir"]

        return render(request, "weather/index.html", context=context)
