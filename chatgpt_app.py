import streamlit as st
from openai import OpenAI

# Set up the OpenAI client with your API key
client = OpenAI(api_key="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")

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
