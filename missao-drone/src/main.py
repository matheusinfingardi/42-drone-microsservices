# src/main.py
from fastapi import FastAPI
from src.app.interfaces.api import app  # Aqui o app FastAPI está em api.py

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
