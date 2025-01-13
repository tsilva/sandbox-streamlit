from dotenv import load_dotenv
load_dotenv()

import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)