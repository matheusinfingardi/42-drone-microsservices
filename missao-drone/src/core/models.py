
class Mission:
    def __init__(self, start_lat, start_lon, end_lat, end_lon, altitude):
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_lat = end_lat
        self.end_lon = end_lon
        self.altitude = altitude

class Weather:
    def __init__(self, temperature, wind_speed, conditions):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.conditions = conditions
