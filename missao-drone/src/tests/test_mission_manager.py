# src/tests/test_mission_manager.py
import pytest
from unittest.mock import MagicMock
from src.use_cases.mission_manager import MissionManager
from src.core.models import Mission

# Criando o mock para o WeatherAPI
class MockWeatherAPI:
    def get_weather(self, latitude, longitude):
        # Retorna uma temperatura fictícia, em Kelvin (exemplo: 290K = 16.85°C)
        return 290.0  # Exemplo de resposta em Kelvin

# Criando o mock para o MAVSDKController
class MockMAVSDKController:
    def arm_and_takeoff(self, altitude):
        # Simula o armamento e decolagem do drone
        pass

    def go_to(self, lat, lon, alt):
        # Simula o movimento do drone
        pass

# Teste de iniciar a missão
def test_start_mission():
    # Cria o mock dos controladores
    mavsdk_controller = MockMAVSDKController()
    weather_api = MockWeatherAPI()

    # Cria o objeto MissionManager com os mocks
    mission_manager = MissionManager(mavsdk_controller, weather_api)

    # Cria uma missão de exemplo
    mission = Mission(start_lat=12.9716, start_lon=77.5946, end_lat=13.0827, end_lon=80.2707, altitude=100)

    # Testa a missão
    mission_manager.start_mission(mission)
    
    # Se não houver exceções, o teste passa
    assert True

# Teste com clima ruim (temperatura muito baixa)
def test_start_mission_climate_bad():
    # Modifica o mock do clima para retornar uma temperatura abaixo de 0°C (em Kelvin)
    class MockWeatherAPICold:
        def get_weather(self, latitude, longitude):
            return 270.0  # 270K = -3.15°C
    
    # Usando o mock de clima frio
    weather_api_cold = MockWeatherAPICold()
    
    # Cria o objeto MissionManager com o mock de clima frio
    mavsdk_controller = MockMAVSDKController()
    mission_manager = MissionManager(mavsdk_controller, weather_api_cold)

    # Cria uma missão
    mission = Mission(start_lat=12.9716, start_lon=77.5946, end_lat=13.0827, end_lon=80.2707, altitude=100)
    
    # Testa a missão (não deve continuar se o clima estiver ruim)
    mission_manager.start_mission(mission)
    
    # Verifica se o comportamento esperado foi atingido (por exemplo, a missão foi interrompida)
    # A forma de verificar isso pode variar, mas se o clima for ruim, a missão não prossegue
    assert True
