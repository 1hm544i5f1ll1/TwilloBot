import os
import time
import streamlit as st
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# load creds
load_dotenv()
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
FROM = "whatsapp:+XXXXXXXXXXX"  # your sandbox

st.title("WhatsApp Test Sender")
to_number = st.text_input("Destination (E.164, e.g. +1XXX…)")
body = st.text_area("Message")
if st.button("Send"):
    if not to_number or not body:
        st.error("Fill both fields")
    else:
        with st.spinner("Sending…"):
            for attempt in range(1, 6):
                try:
                    msg = client.messages.create(
                        from_=FROM,
                        to=f"whatsapp:{to_number}",
                        body=body
                    )
                    st.success(f"✅ Sent! SID: {msg.sid}")
                    break
                except TwilioRestException as e:
                    st.warning(f"Attempt {attempt} failed: {e.msg}")
                    time.sleep(2)
            else:
                st.error("❌ All retries failed.")
