from flask import Flask, jsonify, request
from src.core.drone import Drone
from src.application.services.drone_service import DroneService
import asyncio

app = Flask(__name__)

# Rota para conectar o drone
@app.route('/drone/connect', methods=['POST'])
def connect_drone():
    data = request.get_json()
    drone_id = data['id']
    drone_name = data['name']

    # Cria o objeto Drone
    drone = Drone(id=drone_id, name=drone_name)
    drone_service = DroneService(drone)

    # Executa a conexão do drone de maneira assíncrona
    loop = asyncio.get_event_loop()  # Usa o loop de eventos existente
    loop.run_until_complete(drone_service.connect_drone())

    return jsonify({
        "status": "connected",
        "drone": str(drone)
    })

# Rota para armar o drone
@app.route('/drone/arm', methods=['POST'])
def arm_drone():
    data = request.get_json()
    drone_id = data['id']

    # Cria o objeto Drone
    drone = Drone(id=drone_id, name="Drone Name")
    drone_service = DroneService(drone)

    # Executa o armamento do drone de maneira assíncrona
    loop = asyncio.get_event_loop()  # Usa o loop de eventos existente
    loop.run_until_complete(drone_service.arm_drone())

    return jsonify({
        "status": "armed",
        "drone": str(drone)
    })

# Rota para desarmar o drone
@app.route('/drone/disarm', methods=['POST'])
def disarm_drone():
    data = request.get_json()
    drone_id = data['id']

    # Cria o objeto Drone
    drone = Drone(id=drone_id, name="Drone Name")
    drone_service = DroneService(drone)

    # Executa o desarmamento do drone de maneira assíncrona
    loop = asyncio.get_event_loop()  # Usa o loop de eventos existente
    loop.run_until_complete(drone_service.disarm_drone())

    return jsonify({
        "status": "disarmed",
        "drone": str(drone)
    })

if __name__ == "__main__":
    # Inicia a aplicação Flask
    app.run(debug=True)
