import streamlit as st


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

with open("styles/style.css") as css:

    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )


# ==========================================
# PAGE HEADER
# ==========================================

st.title(
    "⚙️ Settings"
)


st.write(
    "Manage your InterviewIQ AI preferences."
)


st.markdown("---")


# ==========================================
# PROFILE SETTINGS
# ==========================================

st.subheader(
    "👤 Profile Settings"
)


name = st.session_state.get(
    "name",
    ""
)


email = st.session_state.get(
    "email",
    ""
)


college = st.session_state.get(
    "college",
    ""
)


new_name = st.text_input(
    "Full Name",
    value=name
)


new_email = st.text_input(
    "Email",
    value=email
)


new_college = st.text_input(
    "College",
    value=college
)


if st.button(
    "💾 Save Profile",
    use_container_width=True
):

    st.session_state.name = new_name

    st.session_state.email = new_email

    st.session_state.college = new_college


    st.success(
        "✅ Profile updated successfully!"
    )


st.markdown("---")


# ==========================================
# INTERVIEW SETTINGS
# ==========================================

st.subheader(
    "🎤 Interview Preferences"
)


current_difficulty = st.session_state.get(
    "difficulty",
    "Medium"
)


difficulty = st.selectbox(

    "Default Difficulty",

    [
        "Easy",
        "Medium",
        "Hard"
    ],

    index=[
        "Easy",
        "Medium",
        "Hard"
    ].index(current_difficulty)

)


current_interview_type = st.session_state.get(

    "interview_type",

    "Technical"

)


interview_type = st.selectbox(

    "Default Interview Type",

    [
        "Technical",
        "HR",
        "Behavioral",
        "Aptitude"
    ],

    index=[
        "Technical",
        "HR",
        "Behavioral",
        "Aptitude"
    ].index(current_interview_type)

)


if st.button(

    "💾 Save Interview Preferences",

    use_container_width=True

):

    st.session_state.difficulty = difficulty

    st.session_state.interview_type = interview_type


    st.success(
        "✅ Interview preferences saved!"
    )


st.markdown("---")


# ==========================================
# APPLICATION INFO
# ==========================================

st.subheader(
    "ℹ️ About InterviewIQ AI"
)


st.info(
    """
    InterviewIQ AI is an AI-powered interview preparation platform.

    Features include:

    🤖 AI Mock Interviews

    📄 Resume Analysis

    🎯 Skill Gap Analysis

    🛣️ Career Roadmap

    🎤 Voice Interviews

    💬 AI Chat Assistant

    📊 Performance Reports
    """
)


st.markdown("---")


# ==========================================
# RESET DATA
# ==========================================

st.subheader(
    "🔄 Reset Application Data"
)


if st.button(
    "⚠️ Reset Session Data"
):

    for key in list(
        st.session_state.keys()
    ):

        del st.session_state[key]


    st.success(
        "Session data has been reset."
    )


    st.rerun()