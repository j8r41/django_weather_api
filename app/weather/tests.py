import os

import requests
from django.test import Client, TestCase


class WeatherTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_weather_request(self):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q": "Moscow"}

        headers = {
            "X-RapidAPI-Key": os.environ.get("X-RAPIDDAPI-KEY"),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        }

        response = requests.get(url, headers=headers, params=querystring)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/?city=Moscow")
        self.assertEqual(response.status_code, 200)
