import streamlit as st
from .page import Page

def generate_story(story):
    for line in story:
        yield line

class FinalStoryPage(Page):
    def __init__(self, game_interaction):
        super().__init__(game_interaction)

    def display(self):
        st.title("Final Story:")
        story = self.game_interaction.get_final_story(st.session_state.game_id, st.session_state.player_id)
        for line in story:
            st.write(line)
        # delete stuff from database
