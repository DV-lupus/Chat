import streamlit as st
import openai

# Set your API key (DO NOT share this publicly!)
openai.api_key = "your-api-key-here"

st.title("🤖 Chat with ChatGPT")

# Input from the user
user_input = st.text_input("You:", placeholder="Type your message here...")

# When user types something
if user_input:
    with st.spinner("ChatGPT is thinking..."):
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        # Get the reply
        reply = response["choices"][0]["message"]["content"]

        # Show reply
        st.markdown(f"**ChatGPT:** {reply}")
