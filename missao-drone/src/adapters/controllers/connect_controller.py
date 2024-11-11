from fastapi import APIRouter, HTTPException
from src.services.connection_service import ConnectionService
from src.adapters.repositories.drone_repository import DroneRepository

# Instanciando o repositório e o serviço de conexão
drone_repo = DroneRepository()
connection_service = ConnectionService(drone_repo)

router = APIRouter()

@router.post("/connect")
async def connect_drone(drone_id: str):
    """Endpoint para conectar o drone"""
    try:
        # Chama o serviço de conexão
        result = await connection_service.connect_drone(drone_id)
        if result['status'] == "success":
            return {"message": result['message']}
        else:
            raise HTTPException(status_code=400, detail=result['message'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar o drone: {str(e)}")
