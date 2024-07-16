import streamlit as st
from .page import Page

class MainPage(Page):
    def __init__(self, game_interaction):
        super().__init__(game_interaction)

    def display(self):
        st.title("Welcome to Tele-Stories!")
        if st.button("Create Game"):
            st.session_state.page = 'create_game'
            st.rerun()
        if st.button("Join Game"):
            st.session_state.page = 'join_game'
            st.rerun()