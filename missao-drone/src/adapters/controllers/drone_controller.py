# src/adapters/controllers/drone_controller.py

from fastapi import APIRouter, HTTPException
from src.adapters.repositories.drone_repository import DroneRepository

# Instância do repositório
drone_repo = DroneRepository()

# Criação do router para gerenciar as rotas de drones
router = APIRouter()

# Endpoint GET para buscar o drone pelo 'drone_id'
@router.get("/drones/{drone_id}")
async def get_drone(drone_id: str):
    try:
        # Busca o drone no repositório
        drone = await drone_repo.get_drone_by_id(drone_id)

        if drone:
            return {"drone": drone}  # Retorna o drone se encontrado
        else:
            raise HTTPException(status_code=404, detail="Drone não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
