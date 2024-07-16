from .database_service import DatabaseService
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class SupabaseService(DatabaseService):
    def __init__(self):
        super().__init__()
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def add_game(self, game_id: str, num_rounds: int):
        self.supabase.table("Games").insert({"game_id": game_id, "num_rounds": num_rounds}).execute()

    def add_player(self, name: str, game_id: str):
        new_player = self.supabase.table("Players").insert({"player_name": name, "game_id": game_id}).execute()
        self.supabase.table("Stories").insert({"game_id": game_id, "player_id": new_player.data[0]['player_id'], "story": []}).execute()
        return new_player

    def update_num_rounds(self, game_id: str, num_rounds: int):
        self.supabase.table("Games").update({"num_rounds": num_rounds}).eq("game_id", game_id).execute()

    def has_game_started(self, game_id: str):
        return self.supabase.table("Games").select('is_started').eq("game_id", game_id).execute()

    def get_stories(self, game_id):
        return self.supabase.table("Stories").select('story', 'player_id').eq("game_id", game_id).order("added", desc=False).execute()

    def get_num_rounds(self, game_id):
        return self.supabase.table("Games").select('num_rounds').eq("game_id", game_id).execute()

    def get_num_written(self, player_id):
        return self.supabase.table("Players").select('num_written').eq("player_id", player_id).execute()

    def update_story(self, game_id, player_id, story):
        self.supabase.table("Stories").update({"story": story}).eq("game_id", game_id).eq("player_id", player_id).execute()
        num_written = int(self.get_num_written(player_id).data[0]['num_written'])
        self.supabase.table("Players").update({"num_written": num_written + 1}).eq("player_id", player_id).execute()

    def start_game(self, game_id):
        self.supabase.table("Games").update({"is_started": True}).eq("game_id", game_id).execute()

