import streamlit as st
from .page import Page


class JoinGamePage(Page):
    def __init__(self, game_interaction):
        super().__init__(game_interaction)

    def display(self):
        st.title("Join Game")
        if "first_join" not in st.session_state:
            game_id = st.text_input("Enter Game ID:")
        else:
            game_id = st.session_state.game_id
        name = st.text_input("Enter Name:")
        if st.button("Join"):
            if self.game_interaction.has_game_started(game_id):
                st.write("Game already started!!")
            else:
                st.session_state.player_id = self.game_interaction.join_game(game_id, name)
                if "first_join" in st.session_state:
                    self.game_interaction.start_game(game_id)
                st.session_state.game_id = game_id
                st.session_state.page = 'wait_to_start'
                st.rerun()
        if st.button("Back to Main"):
            st.session_state.page = 'main'
            st.rerun()
