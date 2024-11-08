# src/infrastructure/mavsdk_driver.py
from mavsdk import System

class MAVSDKController:
    def __init__(self):
        self.drone = System()

    def connect(self, connection_url="udp://:14540"):
        self.drone.connect(system_address=connection_url)

    def arm_and_takeoff(self, altitude):
        # Lógica de armamento e decolagem
        pass

    def go_to(self, lat, lon, alt):
        # Lógica de navegação do drone
        pass
