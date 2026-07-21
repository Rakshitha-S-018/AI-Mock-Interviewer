import streamlit as st
from modules.roadmap_generator import generate_roadmap

st.set_page_config(
    page_title="Career Roadmap",
    page_icon="🛣️",
    layout="wide"
)

with open("styles/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.title("🛣️ AI Career Roadmap")

st.markdown(
    "Generate a personalized AI-powered learning roadmap for your dream job."
)

st.markdown("---")

role = st.selectbox(
    "Select Target Role",
    [
        "Python Developer",
        "AI/ML Engineer",
        "Data Analyst",
        "Software Engineer",
        "Cyber Security Analyst",
        "Full Stack Developer"
    ]
)

skills = st.text_area(
    "Enter Your Current Skills (comma separated)",
    placeholder="Python, SQL, Git, HTML..."
)

if st.button("🚀 Generate Roadmap"):

    if skills.strip() == "":
        st.warning("Please enter your current skills.")
        st.stop()

    with st.spinner("🤖 AI is creating your roadmap..."):

        roadmap = generate_roadmap(role, skills)

    st.success("Roadmap Generated Successfully!")

    st.markdown(roadmap)