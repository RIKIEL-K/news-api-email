import requests
from send_email import send_email
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

topic = "tesla"
API_Key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-01-06&sortBy=publishedAt&apiKey={API_Key}&language=en"
request = requests.get(url)
content = request.json()

st.header("Get our newsletter")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    msg = "Subject: Today's news \n\n"
    btn = st.form_submit_button()
    if btn:
           for article in content["articles"][:20]:
                  if article["title"] is not None and article["description"] is not None:
                         msg += article["title"] + "\n" + article["description"] + article["url"] + 2 * "\n"
           msg = msg.encode('utf-8')
           send_email(message=msg,receiver_email=user_email)
           st.info("NewsLetter sended !")