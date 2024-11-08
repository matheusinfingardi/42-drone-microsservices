# src/interfaces/mavsdk_controller.py

class MAVSDKController:
    def __init__(self):
        # Inicialização do MAVSDK
        pass

    def connect(self, connection_url="udp://:14540"):
        # Conexão com o MAVSDK
        pass

    def arm_and_takeoff(self, altitude):
        # Lógica de armamento e decolagem
        pass

    def go_to(self, lat, lon, alt):
        # Lógica para enviar o drone para as coordenadas
        pass
