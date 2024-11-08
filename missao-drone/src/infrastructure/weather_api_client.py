
import requests

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, latitude, longitude):
        response = requests.get(self.base_url, params={
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key
        })
        return response.json()
