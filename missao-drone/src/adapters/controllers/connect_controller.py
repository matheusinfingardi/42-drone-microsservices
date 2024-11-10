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
        # Busca o drone pelo drone_id
        drone = await drone_repo.get_drone_by_id(drone_id)
        
        if drone:
            # Você pode utilizar outras colunas do drone, como `connection_type` ou `connection_status`
            # Para exemplo, aqui assumimos que você tentaria conectar com base nessas informações.
            # Lógica de conexão com o drone (conforme necessário)
            success = await connect_use_case.execute(drone_id)
            
            if success:
                return {"message": f"Conectado com sucesso ao drone {drone_id}."}
            else:
                raise HTTPException(status_code=500, detail="Falha ao conectar ao drone.")
        else:
            raise HTTPException(status_code=404, detail="Drone não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
