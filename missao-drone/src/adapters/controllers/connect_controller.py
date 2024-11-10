# src/adapters/controllers/connect_controller.py

from fastapi import APIRouter, HTTPException
from src.adapters.repositories.drone_repository import DroneRepository

# Instância do repositório
drone_repo = DroneRepository()

# Criação do router para gerenciar as rotas de conexão
router = APIRouter()

# Endpoint POST para conectar ao drone
@router.post("/connect")
async def connect_drone(drone_id: str):
    try:
        # Conecta ao drone e atualiza o status no repositório
        result = await drone_repo.connect_to_drone(drone_id)

        if result["status"] == "connected":
            return {"message": f"Drone {drone_id} conectado com sucesso!"}
        else:
            raise HTTPException(status_code=400, detail=result.get("error", "Erro ao conectar"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
