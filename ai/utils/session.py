import streamlit as st

def init_session():

    defaults = {
        "cars":0,
        "persons":0,
        "bikes":0,
        "trucks":0,
        "traffic":0,
        "risk":"LOW",
        "recommendation":"Continue Driving",
        "safety":100
    }

    for key,value in defaults.items():
        if key not in st.session_state:
            st.session_state[key]=value