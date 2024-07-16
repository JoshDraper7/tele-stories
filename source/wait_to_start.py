import streamlit as st
from .page import Page
import time


class WaitToStartPage(Page):
    def __init__(self, game_interaction):
        super().__init__(game_interaction)

    def display(self):
        st.write("Waiting to start...")
        # st.write(f"Your player_id is: {st.session_state.player_id}")
        while True:
            if self.game_interaction.has_game_started(st.session_state.game_id):
                break
            time.sleep(5)
        st.session_state.page = 'write_story'
        st.rerun()