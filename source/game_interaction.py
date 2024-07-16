from .database.database_service import DatabaseService
from .utils.generate import generate_game_id

class GameInteraction:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    def create_game(self, num_rounds: int) -> str:
        game_id = generate_game_id()
        self.database_service.add_game(game_id, num_rounds)
        return game_id

    def update_game_rounds(self, game_id: str, num_rounds: int):
        self.database_service.update_num_rounds(game_id, num_rounds)

    def join_game(self, game_id, name):
        return self.database_service.add_player(name, game_id).data[0]['player_id']

    def has_game_started(self, game_id):
        return self.database_service.has_game_started(game_id).data[0]['is_started']

    def get_next_story(self, game_id, player_id):
        num_written = int(self.database_service.get_num_written(player_id).data[0]['num_written'])
        stories = self.database_service.get_stories(game_id).data
        related_story_index = 0
        for i in range(len(stories)):
            if int(stories[i]['player_id']) == player_id:
                related_story_index = i
                break
        num_rounds = int(self.database_service.get_num_rounds(game_id).data[0]['num_rounds'])
        print(related_story_index)
        print(stories)
        print(len(stories[(num_written + related_story_index) % len(stories)]['story']))
        print()
        if num_written == 0:
            return ["FIRST_ENTRY"], None
        elif len(stories[related_story_index]['story']) == num_rounds:
            return ["STORY_DONE"], None
        elif num_written != num_rounds and len(stories[(num_written + related_story_index) % len(stories)]['story']) == num_written:
            return stories[(num_written + related_story_index) % len(stories)]['story'], stories[(num_written + related_story_index) % len(stories)]['player_id']
        else:
            return ["WAITING_FOR_NEXT"], None

    def update_story(self, game_id, player_id, story):
        self.database_service.update_story(game_id, player_id, story)

    def get_final_story(self, game_id, player_id):
        stories = self.database_service.get_stories(game_id).data
        for i in range(len(stories)):
            if int(stories[i]['player_id']) == player_id:
                return stories[i]['story']
        return []

    def start_game(self, game_id):
        self.database_service.start_game(game_id)

