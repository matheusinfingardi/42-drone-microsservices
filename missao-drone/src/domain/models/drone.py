# src/domain/models/drone.py

from typing import Optional

class Drone:
    def __init__(self, connection_status: bool = False):
        self.connection_status = connection_status
