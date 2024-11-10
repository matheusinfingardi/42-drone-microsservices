# src/infrastructure/supabase_integration.py
import os
from supabase import create_client, Client  # Importando corretamente o cliente Supabase

def get_supabase_client() -> Client:
    """
    Retorna uma instância do cliente Supabase configurado.
    Lê as variáveis de ambiente SUPABASE_URL e SUPABASE_KEY.
    """
    url = os.getenv("SUPABASE_URL")  # Lê a URL do Supabase da variável de ambiente
    key = os.getenv("SUPABASE_KEY")  # Lê a chave do Supabase da variável de ambiente
    
    if not url or not key:
        raise ValueError("A URL ou chave do Supabase não foi fornecida.")
    
    return create_client(url, key)
