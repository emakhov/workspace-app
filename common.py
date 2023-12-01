import streamlit as st


def get_or_init_state(key, init_value):
    if key not in st.session_state:
        st.session_state[key] = init_value

    return st.session_state.get(key)


def init_state(key, init_value):
    if key not in st.session_state:
        st.session_state[key] = init_value
