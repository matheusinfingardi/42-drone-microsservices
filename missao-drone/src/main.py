# src/main.py

from fastapi import FastAPI
from src.adapters.controllers.drone_controller import router as drone_router
from src.adapters.controllers.connect_controller import router as connect_router

# Inicializa a aplicação FastAPI
app = FastAPI()

# Inclui os routers com as rotas '/drones/{drone_id}' e '/connect'
app.include_router(drone_router)
app.include_router(connect_router)
