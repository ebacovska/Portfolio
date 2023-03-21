from send_email import send_email
import streamlit as st

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress")
    raw_user_text = st.text_area("Your message")
    user_text = f"""\
Subject: New email from {user_email}.

{raw_user_text}  
"""

     

    button = st.form_submit_button("Send")
    print(button)
    if button:
        send_email(user_text)
        st.info("Your email was sent succeessfully!")
