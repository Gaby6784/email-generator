import streamlit as st
import ollama

# Streamlit App
st.set_page_config(page_title="Local GPT Email Generator", page_icon="✉️")
st.title("Email Generator")
st.write("Generate professional emails from bullet points.")

# Input
context = st.text_area("Bullet Points", height=200, placeholder="- Reschedule the meeting\n- Apologize\n- Confirm new time")

tone = st.selectbox("Choose a tone", ["Professional", "Friendly", "Persuasive", "Apologetic"])

if st.button("Generate Email") and context.strip():
    with st.spinner("Thinking... Generating your email..."):
        prompt = f"""
        You are a professional assistant. Based on the following bullet points, write a complete, well-structured, and natural-sounding {tone.lower()} email.

        Make sure the email flows logically and reads as if it were written by a human. Do not just list items — integrate the ideas into two paragraphs.

        Bullet points:
        {context.strip()}
        """

        try:
            response = ollama.chat(
                model="mistral",
                messages=[{"role": "user", "content": prompt}]
            )
            generated_email = response['message']['content']
            st.subheader("Generated Email")
            st.markdown(f"<div style='white-space: pre-wrap; font-size: 1.1em;'>{generated_email}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
