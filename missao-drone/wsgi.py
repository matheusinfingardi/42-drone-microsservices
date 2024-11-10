import sys
import os

# Adiciona o diretório src ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.interface.api import app  # Agora o Gunicorn pode encontrar a aplicação Flask

# A variável 'application' é usada pelo Gunicorn para iniciar o servidor
application = app
