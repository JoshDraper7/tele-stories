import streamlit as st
from source.game_interaction import GameInteraction
from source.database.supabase_service import SupabaseService
from source.main import MainPage
from source.create_game import CreateGamePage
from source.join_game import JoinGamePage
from source.wait_to_start import WaitToStartPage
from source.write_story import WriteStoryPage
from source.final import FinalStoryPage

if __name__ == '__main__':
    # Init variables
    if 'page' not in st.session_state:
        st.session_state.page = 'main'
    if 'game_id' not in st.session_state:
        st.session_state.game_id = ''
    game_interaction = GameInteraction(SupabaseService())
    # Go to page
    if st.session_state.page == 'main':
        MainPage(game_interaction).display()
    elif st.session_state.page == 'create_game':
        CreateGamePage(game_interaction).display()
    elif st.session_state.page == 'join_game':
        JoinGamePage(game_interaction).display()
    elif st.session_state.page == 'wait_to_start':
        WaitToStartPage(game_interaction).display()
    elif st.session_state.page == 'write_story':
        WriteStoryPage(game_interaction).display()
    elif st.session_state.page == 'final':
        FinalStoryPage(game_interaction).display()