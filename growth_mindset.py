
import streamlit as st
import random

st.title("🌱 Growth Mindset App")

# Motivation
st.subheader("💡 Stay Motivated!")
motivation = random.choice([
    "Believe in yourself! 🌟",
    "Mistakes help you grow. Keep going! 💪",
    "Every day is a new chance to learn. 📚",
    "Small steps lead to big success! 🚀",
])

st.write(motivation)


# Challenge

st.subheader("🎯 Try This Challenge!")
challenge = random.choice([
    "Read something new for 5 minutes. 📖",
    "Try a small task outside your comfort zone. 💪",
    "Tell yourself a positive affirmation. 🌈",
    "Help someone today, even in a small way. ❤️"
])

st.write(challenge)

# User Feedback
st.subheader("✍️ What Did You Learn Today?")
reflection = st.text_area("Write your thoughts here...")

if st.button("Submit"):
    if reflection:
        st.success("Amazing! Keep learning and growing! 🌟")
    else:
        st.warning("Try writing something to build self-awareness. 😊")
