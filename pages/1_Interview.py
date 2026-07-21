import streamlit as st

from modules.question_generator import generate_questions
from modules.evaluator import evaluate_answer


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Mock Interview",
    page_icon="🎤",
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

    st.error(
        "⚠️ Please register from the Home Page first."
    )

    st.stop()


# ==========================================
# GENERATE QUESTIONS
# ==========================================

if "questions" not in st.session_state:

    with st.spinner(
        "🤖 AI is generating your interview questions..."
    ):

        st.session_state.questions = generate_questions(

            st.session_state.role,

            st.session_state.difficulty,

            st.session_state.interview_type

        )


# ==========================================
# INITIALIZE INTERVIEW STATE
# ==========================================

if "current_question" not in st.session_state:

    st.session_state.current_question = 0


if "answers" not in st.session_state:

    st.session_state.answers = [

        ""

        for _ in st.session_state.questions

    ]


# ==========================================
# HEADER
# ==========================================

st.title(
    "🎤 AI Mock Interview"
)


st.markdown(
    f"### Welcome, {st.session_state.name}! 👋"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        f"💼 Role\n\n{st.session_state.role}"
    )


with col2:

    st.info(
        f"📈 Difficulty\n\n{st.session_state.difficulty}"
    )


with col3:

    st.info(
        f"🎯 Type\n\n{st.session_state.interview_type}"
    )


st.markdown("---")


# ==========================================
# QUESTION DATA
# ==========================================

index = st.session_state.current_question

total = len(st.session_state.questions)


# ==========================================
# PROGRESS
# ==========================================

st.subheader(
    f"Question {index + 1} of {total}"
)


progress = (index + 1) / total


st.progress(progress)


st.markdown("---")


# ==========================================
# QUESTION
# ==========================================

st.markdown(
    "### 🤖 Interviewer"
)


st.info(
    st.session_state.questions[index]
)


# ==========================================
# ANSWER
# ==========================================

st.markdown(
    "### ✍️ Your Answer"
)


answer = st.text_area(

    "Write your answer below",

    value=st.session_state.answers[index],

    height=220,

    key=f"answer_{index}"

)


st.session_state.answers[index] = answer


st.markdown("---")


# ==========================================
# NAVIGATION
# ==========================================

previous_col, next_col = st.columns(2)


# ==========================================
# PREVIOUS
# ==========================================

with previous_col:

    if st.button(

        "⬅ Previous",

        use_container_width=True

    ):

        if index > 0:

            st.session_state.current_question -= 1

            st.rerun()


# ==========================================
# NEXT / FINISH
# ==========================================

with next_col:

    if index < total - 1:

        if st.button(

            "Next ➡",

            use_container_width=True

        ):

            st.session_state.current_question += 1

            st.rerun()


    else:

        if st.button(

            "✅ Finish Interview",

            use_container_width=True

        ):


            with st.spinner(

                "🤖 AI is evaluating your answers..."

            ):


                evaluations = []

                total_score = 0


                for question, answer in zip(

                    st.session_state.questions,

                    st.session_state.answers

                ):


                    if answer.strip() == "":

                        answer = "No answer provided."


                    result = evaluate_answer(

                        question,

                        answer

                    )


                    evaluations.append(

                        result

                    )


                    try:

                        score_text = (

                            result

                            .split("Score:")[1]

                            .split("/10")[0]

                            .strip()

                        )


                        score = int(

                            score_text

                        )


                    except Exception:

                        score = 5


                    total_score += score


                final_score = int(

                    (

                        total_score

                        /

                        (

                            len(

                                st.session_state.questions

                            )

                            * 10

                        )

                    )

                    * 100

                )


                st.session_state.score = final_score

                st.session_state.evaluations = evaluations


            st.success(

                "🎉 Interview Completed Successfully!"

            )


            st.balloons()


            st.info(

                "📊 Go to Dashboard to view your performance."

            )


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "📊 Interview Status"
)


st.sidebar.write(

    f"👤 **Candidate:** "

    f"{st.session_state.name}"

)


st.sidebar.write(

    f"💼 **Role:** "

    f"{st.session_state.role}"

)


st.sidebar.write(

    f"📈 **Progress:** "

    f"{index + 1}/{total}"

)


answered = sum(

    1

    for answer in st.session_state.answers

    if answer.strip() != ""

)


st.sidebar.metric(

    "Answered",

    answered

)


st.sidebar.metric(

    "Remaining",

    total - answered

)


st.sidebar.progress(

    answered / total

)


st.sidebar.markdown("---")


st.sidebar.success(

    "🚀 Keep Going!"

)