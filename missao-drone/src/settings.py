# src/settings.py

import os
from supabase import create_client, Client

class Settings:
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

    def __init__(self):
        self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

settings = Settings()
