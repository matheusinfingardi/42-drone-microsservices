# src/main.py

from fastapi import FastAPI
from src.adapters.controllers.connect_controller import router as connect_router
from src.adapters.repositories.drone_repository import DroneRepository
from src.domain.usecases.connect_drone import ConnectDrone
from src.settings import settings

# Inicializa o FastAPI
app = FastAPI()

# Inicializa o repositório, caso de uso e controlador
drone_repo = DroneRepository()
connect_use_case = ConnectDrone(drone_repo)

# Inclui o controlador de conexão no FastAPI
app.include_router(connect_router)

# Se você quiser que o FastAPI rode diretamente, como no desenvolvimento local:
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
