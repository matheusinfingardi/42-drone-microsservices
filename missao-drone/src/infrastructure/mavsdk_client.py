# app/infrastructure/mavsdk_client.py
class MAVSDKClient:
    def __init__(self, drone_id: str):
        self.drone_id = drone_id

    async def connect(self):
        """Conectar ao drone via MAVSDK."""
        print(f"Conectando ao drone {self.drone_id}...")
        # Código de conexão real com o MAVSDK (simulação)
        return True

    async def arm_drone(self):
        """Armar o drone."""
        print(f"Drone {self.drone_id} armado.")
        return True

    async def disarm_drone(self):
        """Desarmar o drone."""
        print(f"Drone {self.drone_id} desarmado.")
        return True

    async def is_connected(self):
        """Verificar se o drone está conectado."""
        return True
