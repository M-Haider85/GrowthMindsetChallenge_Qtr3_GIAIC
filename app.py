#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="✴")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🌿 Welcome to the Growth Journey!")
st.write("Embrace challenges, learn from mistakes & unlock your full potential. This web app will help you to develop a growth mindset with reflection, challenges and achievements. 🌱")

#quote section
st.header("🌟 Today's Growth Mindset Quote")
st.write(" ❝Success is not final, Failure is not fatal: it is the courage to continue that counts.❞ - Winston Churchill")

st.header(" 💡 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

#condition

if user_input:
    st.success(f"🔎You are facing: {user_input}. Keep pushing yourself and remember that challenges are opportunities to grow! 🎓")
else:
    st.warning("Tell us about your challenge to get started! 🔑")

#reflection section
st.header("✒️ Reflection on your Learning")
reflection = st.text_area("Write your reflection here:")
if reflection:
    st.success("✨ Great Insight! Your reflection: {reflection}")
else:
    st.warning("Reflecting on past experiences can help you grow. Share your difficulties here! 📝")


#achievements section
st.header("🏆 Celebrate your wins!")
achievement = st.text_input("Share something you've accomplished:")

if achievement:
    st.success(f"🎉 Congratulations! You've accomplished: {achievement}. Keep up the great work! 🔆")
else:
    st.info("Big or small, every achievement counts! Share it now 🎈")    

#footer
st.write("- - - - -")
st.write("💎 Keep believing in yourself. Growth is a journey, not a destination! ✨")  
st.write(" **©Made by Haider Asghar** ")   