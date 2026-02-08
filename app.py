import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="Story Telling Bot")
st.title("StoryBot ")
st.write("Enter your story idea and get a creative story generated!")

# User input
prompt = st.text_input("Enter your story idea:")

# Button to generate story
if st.button("Generate Story"):
    if prompt:
        try:
            # Call OpenAI Chat API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative story writer who creates story at least in 150 words."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            # Extract story
            story = response.choices[0].message.content.strip()
            st.subheader("Generated Story:")
            st.write(story)

        except Exception as e:
            st.error(f"Error generating story: {e}")

    else:
        st.warning("Please enter a story idea!")
