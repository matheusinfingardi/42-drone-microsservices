# src/adapters/controllers/drone_controller.py

from fastapi import APIRouter, HTTPException
from src.adapters.repositories.drone_repository import DroneRepository

# Instancia o repositório
drone_repo = DroneRepository()

# Criando o router para gerenciar as rotas relacionadas a drones
router = APIRouter()

# Endpoint GET para obter um drone pelo 'drone_id'
@router.get("/drones/{drone_id}")
async def get_drone(drone_id: str):
    try:
        # Obtém o drone com o 'drone_id' fornecido
        drone = await drone_repo.get_drone_by_id(drone_id)

        if drone:
            return {"drone": drone}  # Retorna os dados do drone encontrado
        else:
            raise HTTPException(status_code=404, detail="Drone não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
