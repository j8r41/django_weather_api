import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather_request(q_object):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": q_object}

    headers = {
        "X-RapidAPI-Key": os.environ.get("X-RAPIDDAPI-KEY"),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


if __name__ == "__main__":
    data = get_weather_request('Kirov')
    print(data)