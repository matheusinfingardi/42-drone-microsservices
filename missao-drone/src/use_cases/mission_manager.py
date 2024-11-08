# src/use_cases/mission_manager.py
from src.interfaces.mavsdk_controller import MAVSDKController
from src.interfaces.weather_api import WeatherAPI
from src.core.models import Mission

class MissionManager:
    def __init__(self, mavsdk_controller: MAVSDKController, weather_api: WeatherAPI):
        self.mavsdk_controller = mavsdk_controller
        self.weather_api = weather_api

    def start_mission(self, mission: Mission):
        # Obtém a temperatura para o ponto inicial e final
        weather_start = self.weather_api.get_weather(mission.start_lat, mission.start_lon)
        weather_end = self.weather_api.get_weather(mission.end_lat, mission.end_lon)

        # Converter a temperatura de Kelvin para Celsius
        weather_start_celsius = weather_start - 273.15
        weather_end_celsius = weather_end - 273.15

        # Se a temperatura do ponto de início for muito baixa, adiar a missão
        if weather_start_celsius < 0:
            print(f"Clima ruim no ponto inicial: {weather_start_celsius:.2f}°C. Missão adiada.")
            return

        # Lógica de controle de voo
        self.mavsdk_controller.arm_and_takeoff(mission.altitude)
        self.mavsdk_controller.go_to(mission.end_lat, mission.end_lon, mission.altitude)
        print(f"Missão concluída de {mission.start_lat}, {mission.start_lon} para {mission.end_lat}, {mission.end_lon}.")
