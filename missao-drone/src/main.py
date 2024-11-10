import os
from src.app.interfaces.api import app  # O app Flask é importado de api.py

if __name__ == "__main__":
    # Só entra neste bloco quando você executar diretamente com python (não no render)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
