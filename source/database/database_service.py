class DatabaseService:
    def __init__(self):
        pass

    def add_game(self, game_id: int, num_rounds: int): ...

    def add_player(self, name: str, game_id: str): ...

    def update_num_rounds(self, game_id: str, num_rounds: int): ...

    def has_game_started(self, game_id: str): ...

    def get_stories(self, game_id): ...

    def get_num_rounds(self, game_id): ...

    def get_num_written(self, player_id): ...

    def update_story(self, game_id, player_id, story): ...

    def start_game(self, game_id): ...