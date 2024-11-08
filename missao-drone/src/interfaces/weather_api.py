# src/interfaces/weather_api.py
import requests

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, latitude, longitude):
        # Faz a chamada para a API de clima
        response = requests.get(self.base_url, params={
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key
        })
        
        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            # Retorna o valor da temperatura
            return data["main"]["temp"]  # temperatura em Kelvin
        else:
            raise Exception("Erro ao buscar clima.")
