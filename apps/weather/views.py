import pytz
import requests
from datetime import datetime
from decouple import config as env_config

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weather
from .serializers import WeatherSerializer


class WeatherView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WeatherSerializer


    def post(self, request):
        city_name = request.data.get('city', None)

        if not city_name:
            return Response({'error': 'City name is required'}, status=status.HTTP_400_BAD_REQUEST)

        weather_data = self.get_cached_weather_data(city_name)

        if not weather_data:
            weather_data = self.fetch_weather_data(city_name)
            self.cache_weather_data(city_name, weather_data)

        return Response(weather_data)

    def get_cached_weather_data(self, city_name):
        city_name = city_name.title()
        cached_data = Weather.objects.filter(city=city_name).first()

        if cached_data:
            cached_timestamp = cached_data.created.replace(tzinfo=pytz.UTC)
            time_difference = datetime.now(pytz.UTC) - cached_timestamp

            if time_difference.total_seconds() < 1800:
                return {
                    'temperature': cached_data.temperature,
                    'pressure': cached_data.pressure,
                    'wind_speed': cached_data.wind_speed
                }
            else:
                cached_data.delete()

        return None

    def fetch_weather_data(self, city_name):
        api_key = env_config('OPENWEATHER_API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            weather_info = response.json()
            temperature = weather_info['main']['temp']
            pressure = weather_info['main']['pressure']
            wind_speed = weather_info['wind']['speed']

            return {
                'temperature': temperature,
                'pressure': pressure,
                'wind_speed': wind_speed
            }
        elif response.status_code == 404:
            return {'error': 'City not found'}
        else:
            return {'error': 'Failed to fetch weather data'}

    def cache_weather_data(self, city_name, weather_data):
        if all(key in weather_data for key in ['temperature', 'pressure', 'wind_speed']):
            Weather.objects.create(
                city=city_name.title(),
                temperature=weather_data['temperature'],
                pressure=weather_data['pressure'],
                wind_speed=weather_data['wind_speed']
            )
        else:
            return Response({'error': 'Invalid weather data format'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
