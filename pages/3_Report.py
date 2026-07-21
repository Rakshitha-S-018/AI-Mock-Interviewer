import streamlit as st


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Interview Report",
    page_icon="📑",
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
# CHECK INTERVIEW COMPLETION
# ==========================================

if "score" not in st.session_state:

    st.warning(
        "⚠️ Please complete the interview first."
    )

    st.info(
        "🎤 Go to the Interview page and finish the interview to view your report."
    )

    st.stop()


# ==========================================
# HEADER
# ==========================================

st.title(
    "📑 Interview Performance Report"
)


st.markdown(
    "### 🤖 AI-Powered Interview Assessment"
)


st.markdown("---")


# ==========================================
# CANDIDATE DETAILS
# ==========================================

st.subheader(
    "👤 Candidate Details"
)


col1, col2 = st.columns(2)


with col1:

    st.write(
        f"**Name:** {st.session_state.name}"
    )

    st.write(
        f"**Email:** {st.session_state.email}"
    )

    st.write(
        f"**College:** {st.session_state.college}"
    )


with col2:

    st.write(
        f"**Target Role:** {st.session_state.role}"
    )

    st.write(
        f"**Difficulty:** {st.session_state.difficulty}"
    )

    st.write(
        f"**Interview Type:** {st.session_state.interview_type}"
    )


st.markdown("---")


# ==========================================
# SCORE
# ==========================================

score = st.session_state.score


st.subheader(
    "🏆 Overall Score"
)


score_col1, score_col2, score_col3 = st.columns(3)


with score_col1:

    st.metric(
        "Final Score",
        f"{score}%"
    )


with score_col2:

    if score >= 80:

        result = "Excellent 🏆"

    elif score >= 60:

        result = "Good 👍"

    elif score >= 40:

        result = "Average 📈"

    else:

        result = "Needs Improvement 💪"


    st.metric(
        "Performance",
        result
    )


with score_col3:

    st.metric(
        "Total Questions",
        len(st.session_state.questions)
    )


st.progress(
    score / 100
)


st.markdown("---")


# ==========================================
# AI EVALUATIONS
# ==========================================

st.subheader(
    "🧠 AI Question-wise Evaluation"
)


questions = st.session_state.get(
    "questions",
    []
)


answers = st.session_state.get(
    "answers",
    []
)


evaluations = st.session_state.get(
    "evaluations",
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
            "### 🧠 AI Feedback"
        )

        st.write(
            evaluation
        )


st.markdown("---")


# ==========================================
# FINAL RECOMMENDATION
# ==========================================

st.subheader(
    "🎯 Final Recommendation"
)


if score >= 80:

    st.success(
        """
        🌟 Excellent work!

        You show strong interview readiness. Continue practicing advanced questions and real-world problem solving.
        """
    )


elif score >= 60:

    st.info(
        """
        👍 Good performance!

        You have a solid foundation. Focus on improving weak areas and practice explaining your answers more clearly.
        """
    )


elif score >= 40:

    st.warning(
        """
        📈 Average performance.

        Continue practicing regularly and strengthen your technical fundamentals.
        """
    )


else:

    st.error(
        """
        💪 More preparation is recommended.

        Focus on your fundamentals, practice consistently, and try mock interviews regularly.
        """
    )


st.markdown("---")


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "📑 Interview Report"
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
    "Final Score",
    f"{score}%"
)


st.sidebar.success(
    "🎉 Report Generated!"
)