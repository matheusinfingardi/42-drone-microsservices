# src/adapters/controllers/connect_controller.py

from fastapi import APIRouter, HTTPException
from src.domain.usecases.connect_drone import ConnectDrone
from src.adapters.repositories.drone_repository import DroneRepository

# Instancia o repositório
drone_repo = DroneRepository()

# Instancia o caso de uso, passando o repositório
connect_use_case = ConnectDrone(drone_repo)

router = APIRouter()

@router.post("/connect")
async def connect_drone(drone_id: str):
    try:
        # Aqui, agora estamos usando o caso de uso corrigido
        success = await connect_use_case.execute(drone_id)
        if success:
            return {"message": f"Conectado com sucesso ao drone {drone_id}."}
        else:
            raise HTTPException(status_code=500, detail="Falha ao conectar ao drone.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
