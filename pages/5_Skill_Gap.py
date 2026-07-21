import streamlit as st
from modules.skill_gap import analyze_skill_gap

st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="🎯",
    layout="wide"
)

with open("styles/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.title("🎯 AI Skill Gap Analysis")

st.markdown(
    "Discover your missing skills and receive personalized learning recommendations."
)

st.markdown("---")

# Check if resume has been analyzed
if "resume_analysis" not in st.session_state:

    st.warning("⚠ Please complete Resume Analysis first.")

    st.stop()

target_role = st.selectbox(
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

if st.button("🚀 Analyze Skill Gap"):

    with st.spinner("Analyzing Skills..."):

        result = analyze_skill_gap(
            st.session_state.resume_analysis,
            target_role
        )

    st.success("Skill Gap Analysis Completed!")

    st.markdown(result)