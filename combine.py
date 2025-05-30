import streamlit as st

creds_dict = st.secrets.get("google_sheets", None)
if creds_dict is None:
    st.error("Google Sheets credentials not found!")
