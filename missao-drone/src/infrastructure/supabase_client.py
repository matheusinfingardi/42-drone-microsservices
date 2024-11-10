from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Supondo que você tenha as variáveis de ambiente para URL e chave de API do Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

def get_supabase_client() -> Client:
    return create_client(url, key)
