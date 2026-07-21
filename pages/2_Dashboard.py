import streamlit as st
import re


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Performance Dashboard",
    page_icon="📊",
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
# CHECK REGISTRATION
# ==========================================

required_fields = [

    "name",

    "email",

    "college",

    "role",

    "difficulty",

    "interview_type"

]


missing_fields = [

    field

    for field in required_fields

    if field not in st.session_state

]


if missing_fields:

    st.warning(
        "⚠️ Please register from the Home Page first."
    )

    st.stop()


# ==========================================
# PAGE HEADER
# ==========================================

st.title(
    "📊 Interview Performance Dashboard"
)


st.markdown(
    f"### Welcome back, {st.session_state.name}! 👋"
)


st.markdown("---")


# ==========================================
# CHECK INTERVIEW COMPLETION
# ==========================================

if "score" not in st.session_state:

    st.warning(
        "⚠️ Your interview has not been completed yet."
    )

    st.info(
        "🎤 Complete the AI Mock Interview first to view your performance dashboard."
    )

    st.stop()


# ==========================================
# CANDIDATE INFORMATION
# ==========================================

st.subheader(
    "👤 Candidate Information"
)


info1, info2, info3, info4 = st.columns(4)


with info1:

    st.metric(
        "Candidate",
        st.session_state.name
    )


with info2:

    st.metric(
        "Target Role",
        st.session_state.role
    )


with info3:

    st.metric(
        "Difficulty",
        st.session_state.difficulty
    )


with info4:

    st.metric(
        "Interview Type",
        st.session_state.interview_type
    )


st.markdown("---")


# ==========================================
# OVERALL SCORE
# ==========================================

score = st.session_state.score


st.subheader(
    "🏆 Overall Performance"
)


score_col1, score_col2, score_col3 = st.columns(3)


with score_col1:

    st.metric(
        "Overall Score",
        f"{score}%"
    )


with score_col2:

    if score >= 80:

        performance = "Excellent 🏆"

    elif score >= 60:

        performance = "Good 👍"

    elif score >= 40:

        performance = "Average 📈"

    else:

        performance = "Needs Improvement 💪"


    st.metric(
        "Performance Level",
        performance
    )


with score_col3:

    st.metric(
        "Questions",
        len(st.session_state.questions)
    )


st.progress(
    score / 100
)


st.markdown("---")


# ==========================================
# SCORE INTERPRETATION
# ==========================================

st.subheader(
    "📈 Performance Summary"
)


if score >= 80:

    st.success(
        "🌟 Excellent performance! You demonstrated strong interview readiness."
    )


elif score >= 60:

    st.info(
        "👍 Good performance! Continue practicing to improve your interview skills."
    )


elif score >= 40:

    st.warning(
        "📈 Average performance. Focus on improving your technical and communication skills."
    )


else:

    st.error(
        "💪 More practice is recommended. Keep learning and improving!"
    )


st.markdown("---")


# ==========================================
# QUESTION-WISE EVALUATION
# ==========================================

st.subheader(
    "📝 Question-wise AI Evaluation"
)


evaluations = st.session_state.get(
    "evaluations",
    []
)


questions = st.session_state.get(
    "questions",
    []
)


answers = st.session_state.get(
    "answers",
    []
)


for i, evaluation in enumerate(evaluations):

    with st.expander(
        f"Question {i + 1}"
    ):

        if i < len(questions):

            st.markdown(
                "### 🤖 Question"
            )

            st.write(
                questions[i]
            )


        if i < len(answers):

            st.markdown(
                "### ✍️ Your Answer"
            )

            st.write(
                answers[i]
            )


        st.markdown(
            "### 🧠 AI Evaluation"
        )

        st.write(
            evaluation
        )


st.markdown("---")


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "📊 Dashboard"
)


st.sidebar.write(
    f"👤 **Candidate:** "
    f"{st.session_state.name}"
)


st.sidebar.write(
    f"💼 **Role:** "
    f"{st.session_state.role}"
)


st.sidebar.metric(
    "Overall Score",
    f"{score}%"
)


st.sidebar.markdown("---")


st.sidebar.success(
    "🎉 Interview Completed!"
)