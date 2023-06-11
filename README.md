# Django Weather App
Django weather forecast search web app.

## About

This app allows users to obtain information about the current weather forecast for a required city using API.

## Task
[Here](https://github.com/j8r41/django_weather_api/blob/dev/task.txt)


## Getting Started

### Prerequisites:

- python 3.9+
- pip

### Before installation:
1. Get API-key on [Rapid API by WeatherAPI.com](https://rapidapi.com/weatherapi/api/weatherapi-com/)

### Installation:
1. Clone the repo.
```
$ git clone git@github.com:j8r41/django_weather_api.git
```

2. Aсtivate virtual environment.
```
$ cd django_weather_api
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install requirements.
```
(venv) $ pip install -r requirements.txt
```

4. Define environment variables
```
$ nano .env
```
```
X-RAPIDDAPI-KEY= ...
SECRET_KEY=django-insecure-...
```
5. Run python code
```
$ cd app/
$ python3 manage.py runserver
```
