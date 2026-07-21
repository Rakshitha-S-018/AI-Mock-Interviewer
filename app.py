import streamlit as st
import re
import base64


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="InterviewIQ AI",
    page_icon="🎤",
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

with open("styles/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# ==========================================
# HOMEPAGE BACKGROUND
# ==========================================

def set_background(image_path):

    with open(image_path, "rb") as image_file:

        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()


    st.markdown(

        f"""
        <style>

        /* MAIN BACKGROUND */

        .stApp {{

            background-image:

            linear-gradient(

                rgba(3, 8, 25, 0.45),

                rgba(3, 8, 25, 0.45)

            ),

            url(
                "data:image/png;base64,{encoded_image}"
            );

            background-size: cover;

            background-position: center;

            background-attachment: fixed;

        }}


        /* BRIGHT TEXT */

        .stApp h1,

        .stApp h2,

        .stApp h3,

        .stApp h4,

        .stApp p,

        .stApp label,

        .stApp span {{

            color: #ffffff;

        }}


        /* INPUT BOXES */

        .stTextInput input,

        .stTextArea textarea,

        .stSelectbox div,

        .stFileUploader div {{

            background-color: rgba(0, 0, 0, 0.35);

            color: white;

        }}


        /* INPUT TEXT */

        input,

        textarea {{

            color: white !important;

        }}


        /* PLACEHOLDER TEXT */

        input::placeholder,

        textarea::placeholder {{

            color: rgba(255, 255, 255, 0.80) !important;

        }}


        /* SIDEBAR */

        section[data-testid="stSidebar"] {{

            background-color: rgba(3, 8, 25, 0.90);

        }}


        /* BUTTON TEXT */

        .stButton button {{

            font-weight: bold;

        }}

        </style>
        """,

        unsafe_allow_html=True

    )


# ==========================================
# APPLY BACKGROUND
# ==========================================

set_background(
    "assets/interview_background.png"
)


# ==========================================
# SESSION STATE
# ==========================================

if "registered" not in st.session_state:

    st.session_state.registered = False


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "🎤 InterviewIQ AI"
)

st.sidebar.markdown("---")

st.sidebar.subheader(
    "✨ Platform Features"
)


features = [

    "🤖 AI Mock Interview",

    "📄 Resume Analysis",

    "📊 Performance Dashboard",

    "🎯 Skill Gap Analysis",

    "🛣 Learning Roadmap",

    "📑 PDF Report",

    "🎤 Voice Interview",

    "💬 AI Chat Assistant"

]


for feature in features:

    st.sidebar.write(
        feature
    )


st.sidebar.markdown("---")

st.sidebar.success(
    "🚀 GenAI Project"
)


# ==========================================
# HERO SECTION
# ==========================================

st.title(
    "🎤 InterviewIQ AI"
)


st.markdown(

    """
    ## 🚀 AI-Powered Mock Interview & Career Assessment Platform

    Practice interviews with AI.

    Analyze your resume.

    Discover your skill gaps.

    Improve your confidence.

    Get AI-powered feedback.
    """

)


st.markdown("---")


# ==========================================
# CANDIDATE REGISTRATION
# ==========================================

st.subheader(
    "👤 Candidate Registration"
)


col1, col2 = st.columns(2)


# ==========================================
# LEFT COLUMN
# ==========================================

with col1:

    name = st.text_input(

        "👤 Full Name",

        placeholder="Enter your full name"

    )


    email = st.text_input(

        "📧 Email Address",

        placeholder="example@gmail.com"

    )


    college = st.text_input(

        "🏫 College",

        placeholder="Enter your college name"

    )


# ==========================================
# RIGHT COLUMN
# ==========================================

with col2:

    role = st.selectbox(

        "💼 Target Role",

        [

            "Python Developer",

            "AI/ML Engineer",

            "Software Engineer",

            "Full Stack Developer",

            "Cyber Security Analyst",

            "Data Analyst"

        ]

    )


    difficulty = st.selectbox(

        "📈 Difficulty",

        [

            "Easy",

            "Medium",

            "Hard"

        ]

    )


    interview_type = st.selectbox(

        "🎯 Interview Type",

        [

            "Technical",

            "HR",

            "Behavioral",

            "Aptitude"

        ]

    )


st.markdown("---")


# ==========================================
# RESUME UPLOAD
# ==========================================

resume = st.file_uploader(

    "📄 Upload Resume (PDF)",

    type=["pdf"]

)


st.markdown("---")


# ==========================================
# START INTERVIEW
# ==========================================

if st.button(

    "🚀 Start Interview",

    use_container_width=True

):


    # ==========================================
    # CLEAN INPUTS
    # ==========================================

    name = name.strip()

    email = email.strip()

    college = college.strip()


    # ==========================================
    # NAME VALIDATION
    # ==========================================

    if name == "":

        st.error(

            "⚠️ Please enter your full name."

        )


    elif not name.replace(

        " ",

        ""

    ).isalpha():

        st.error(

            "⚠️ Name should contain only letters and spaces."

        )


    # ==========================================
    # EMAIL VALIDATION
    # ==========================================

    elif email == "":

        st.error(

            "⚠️ Please enter your email address."

        )


    elif not re.match(

        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",

        email

    ):

        st.error(

            "⚠️ Please enter a valid email address."

        )


    # ==========================================
    # COLLEGE VALIDATION
    # ==========================================

    elif college == "":

        st.error(

            "⚠️ Please enter your college name."

        )


    # ==========================================
    # SUCCESS
    # ==========================================

    else:


        # ==========================================
        # SAVE REGISTRATION DATA
        # ==========================================

        st.session_state.registered = True


        st.session_state.name = name

        st.session_state.email = email

        st.session_state.college = college

        st.session_state.role = role

        st.session_state.difficulty = difficulty

        st.session_state.interview_type = interview_type

        st.session_state.resume = resume


        # ==========================================
        # RESET PREVIOUS INTERVIEW DATA
        # ==========================================

        st.session_state.pop(

            "questions",

            None

        )


        st.session_state.pop(

            "answers",

            None

        )


        st.session_state.pop(

            "current_question",

            None

        )


        st.session_state.pop(

            "evaluations",

            None

        )


        st.session_state.pop(

            "score",

            None

        )


        # ==========================================
        # SUCCESS MESSAGE
        # ==========================================

        st.success(

            "✅ Registration Successful!"

        )


        # ==========================================
        # OPEN INTERVIEW PAGE
        # ==========================================

        st.switch_page(

            "pages/1_Interview.py"

        )


# ==========================================
# PLATFORM FEATURES
# ==========================================

st.markdown("---")


st.subheader(

    "✨ Why Choose InterviewIQ AI"

)


c1, c2, c3 = st.columns(3)


with c1:

    st.info(

        "🤖 AI Generated Interview Questions"

    )


with c2:

    st.info(

        "📄 AI Resume Analysis"

    )


with c3:

    st.info(

        "📊 Performance Dashboard"

    )


c4, c5, c6 = st.columns(3)


with c4:

    st.info(

        "🎯 Skill Gap Analysis"

    )


with c5:

    st.info(

        "📑 PDF Report"

    )


with c6:

    st.info(

        "🎤 Voice Interview"

    )