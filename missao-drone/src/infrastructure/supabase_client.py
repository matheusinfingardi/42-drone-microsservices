# app/infrastructure/supabase_client.py

import os
from supabase_client import create_client, Client

def get_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")  # Lê a URL do Supabase da variável de ambiente
    key = os.getenv("SUPABASE_KEY")  # Lê a chave do Supabase da variável de ambiente
    
    if not url or not key:
        raise ValueError("A URL ou chave do Supabase não foi fornecida.")
    
    return create_client(url, key)
