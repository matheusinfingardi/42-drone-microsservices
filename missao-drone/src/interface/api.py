from flask import Flask, jsonify, request
from src.core.drone import Drone
from src.application.services.drone_service import DroneService
import asyncio

app = Flask(__name__)

@app.route('/drone/connect', methods=['POST'])
def connect_drone():
    data = request.get_json()
    drone_id = data['id']
    drone_name = data['name']

    drone = Drone(id=drone_id, name=drone_name)
    drone_service = DroneService(drone)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(drone_service.connect_drone())

    return jsonify({"status": "connected", "drone": str(drone)})

@app.route('/drone/arm', methods=['POST'])
def arm_drone():
    data = request.get_json()
    drone_id = data['id']

    drone = Drone(id=drone_id, name="Drone Name")
    drone_service = DroneService(drone)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(drone_service.arm_drone())

    return jsonify({"status": "armed", "drone": str(drone)})

@app.route('/drone/disarm', methods=['POST'])
def disarm_drone():
    data = request.get_json()
    drone_id = data['id']

    drone = Drone(id=drone_id, name="Drone Name")
    drone_service = DroneService(drone)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(drone_service.disarm_drone())

    return jsonify({"status": "disarmed", "drone": str(drone)})

if __name__ == "__main__":
    app.run(debug=True)
