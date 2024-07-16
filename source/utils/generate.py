import random
import string

# Function to generate a random 8-character game ID
def generate_game_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))