import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key="your-api-key-here")

st.title("🤖 Chat with ChatGPT")

user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    with st.spinner("ChatGPT is thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.markdown(f"**ChatGPT:** {reply}")
