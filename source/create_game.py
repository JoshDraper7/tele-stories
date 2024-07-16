import streamlit as st
from .page import Page
from .game_interaction import GameInteraction


class CreateGamePage(Page):
    def __init__(self, game_interaction: GameInteraction):
        super().__init__(game_interaction)

    def display(self):
        st.title("Create Game")
        num_rounds = st.number_input("Enter number of rounds: ", min_value=2, max_value=25, value=12)
        if not st.session_state.game_id:
            st.session_state.game_id = self.game_interaction.create_game(num_rounds)
        st.write(f"Your game ID is: {st.session_state.game_id}")
        if st.button("Start Game"):
            self.game_interaction.update_game_rounds(st.session_state.game_id, num_rounds)
            st.session_state.first_join = 'TRUE'
            st.session_state.page = 'join_game'
            st.rerun()
        if st.button("Back to Main"):
            st.session_state.page = 'main'
            st.rerun()
