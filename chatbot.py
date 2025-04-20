import streamlit as st
import google.generativeai as genai

GENAI_API_KEY = "api_key"
genai.configure(api_key=GENAI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def generate_response(query):
    try:
        response = chat.send_message(query)
        return response.text
    except Exception as e:
        return f"Red Dragon Error: {e}"

# Streamlit UI
st.set_page_config(page_title="Red Dragon", page_icon="🐉")
st.markdown("<h1 style='color: crimson;'>🐉 Red Dragon - AI Chat Assistant</h1>", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Type your message here...")

if query:
    st.session_state.history.append(("You", query))
    response = generate_response(query)
    st.session_state.history.append(("Red Dragon", response))

for sender, message in st.session_state.history:
    st.markdown(f"**{sender}:** {message}")