from pydantic import BaseModel

class Drone(BaseModel):
    id: str
    name: str
    is_armed: bool = False

    def __repr__(self):
        return f"Drone(id={self.id}, name={self.name}, is_armed={self.is_armed})"
