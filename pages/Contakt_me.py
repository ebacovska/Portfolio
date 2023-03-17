import streamlit as st
import pandas as pd

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress")
    user_text = st.text_area("Your message")
    button = st.form_submit_button("Send")
    if button:
        print("hi")
