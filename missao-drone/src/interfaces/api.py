# src/interfaces/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.use_cases.mission_manager import MissionManager
from src.interfaces.mavsdk_controller import MAVSDKController
from src.interfaces.weather_api import WeatherAPI
from src.core.models import Mission

app = FastAPI()

class MissionRequest(BaseModel):
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    altitude: float

@app.post("/start_mission")
async def start_mission(request: MissionRequest):
    mavsdk_controller = MAVSDKController()
    weather_api = WeatherAPI()
    mission_manager = MissionManager(mavsdk_controller, weather_api)

    mission = Mission(
        start_lat=request.start_lat,
        start_lon=request.start_lon,
        end_lat=request.end_lat,
        end_lon=request.end_lon,
        altitude=request.altitude
    )
    
    mission_manager.start_mission(mission)
    return {"message": "Missão iniciada"}
