import streamlit as st
from .page import Page
import time

class WriteStoryPage(Page):
    def __init__(self, game_interaction):
        super().__init__(game_interaction)

    def display(self):
        st.write("Write a story!")
        if 'next_story' not in st.session_state or st.session_state.next_story[0] == "WAITING_FOR_NEXT":
            next_story = ["WAITING_FOR_NEXT"]
            while next_story[0] == "WAITING_FOR_NEXT":
                print(next_story[0])
                next_story, other_player_id = self.game_interaction.get_next_story(st.session_state.game_id, st.session_state.player_id)
                if next_story[0] == "WAITING_FOR_NEXT":
                    time.sleep(5)
            st.session_state.next_story = next_story
            st.session_state.other_player_id = other_player_id
        if st.session_state.next_story[0] == "STORY_DONE":
            st.session_state.page = 'final'
            st.rerun()
        else:
            if st.session_state.next_story[0] == "FIRST_ENTRY":
                story_entry = st.text_input("Start your story:")
                if st.button('Submit'):
                    self.game_interaction.update_story(st.session_state.game_id, st.session_state.player_id, [story_entry])
                    st.session_state.next_story = ["WAITING_FOR_NEXT"]
                    st.rerun()
            else:
                st.write(f"Last entry:\n{st.session_state.next_story[-1]}")
                story_entry = st.text_input("Continue the story:")
                if st.button('Submit'):
                    self.game_interaction.update_story(st.session_state.game_id, st.session_state.other_player_id, st.session_state.next_story + [story_entry])
                    st.session_state.next_story = ["WAITING_FOR_NEXT"]
                    st.rerun()




