# src/main.py

from fastapi import FastAPI
from src.adapters.controllers.connect_controller import router as connect_router
from src.adapters.repositories.drone_repository import DroneRepository
from src.domain.usecases.connect_drone import ConnectDrone
from src.settings import settings

# Inicializa o FastAPI
app = FastAPI()

# Inicializa o repositório
drone_repo = DroneRepository()

# Agora, instanciando o caso de uso, passando o drone_repo
connect_use_case = ConnectDrone(drone_repo)

# Inclui o controlador de conexão no FastAPI
app.include_router(connect_router)
