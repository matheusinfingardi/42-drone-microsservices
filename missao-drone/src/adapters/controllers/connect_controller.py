# src/adapters/controllers/connect_controller.py

from fastapi import APIRouter, HTTPException
from src.domain.usecases.connect_drone import ConnectDrone

router = APIRouter()

@router.post("/connect")
async def connect_drone(drone_id: str):
    try:
        connect_use_case = ConnectDrone()
        success = await connect_use_case.execute(drone_id)
        if success:
            return {"message": f"Conectado com sucesso ao drone {drone_id}."}
        else:
            raise HTTPException(status_code=500, detail="Falha ao conectar ao drone.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
