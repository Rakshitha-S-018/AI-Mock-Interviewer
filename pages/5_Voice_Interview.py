import streamlit as st
import speech_recognition as sr
import tempfile
import os

from modules.question_generator import generate_questions
from modules.evaluator import evaluate_answer
from modules.text_to_speech import speak_text


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Voice Interview",
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

    st.warning(
        "⚠️ Please register from the Home Page first."
    )

    st.stop()


# ==========================================
# GENERATE QUESTIONS
# ==========================================

if "voice_questions" not in st.session_state:

    with st.spinner(
        "🤖 AI is preparing your voice interview..."
    ):

        st.session_state.voice_questions = generate_questions(

            st.session_state.role,

            st.session_state.difficulty,

            st.session_state.interview_type

        )


# ==========================================
# INITIALIZE SESSION STATE
# ==========================================

if "voice_current_question" not in st.session_state:

    st.session_state.voice_current_question = 0


if "voice_answers" not in st.session_state:

    st.session_state.voice_answers = [

        ""

        for _ in st.session_state.voice_questions

    ]


if "voice_feedback" not in st.session_state:

    st.session_state.voice_feedback = ""


# ==========================================
# HEADER
# ==========================================

st.title(
    "🤖 InterviewIQ AI"
)


st.markdown(

    f"### 🎤 Voice Interview — Welcome {st.session_state.name}!"

)


st.markdown("---")


# ==========================================
# INTERVIEW STATUS
# ==========================================

index = st.session_state.voice_current_question


total = len(

    st.session_state.voice_questions

)


question = st.session_state.voice_questions[index]


st.progress(

    (index + 1) / total

)


st.write(

    f"Question {index + 1} of {total}"

)


st.markdown("---")


# ==========================================
# AI QUESTION
# ==========================================

st.markdown(
    "### 🤖 AI"
)


st.info(
    question
)


# ==========================================
# AI QUESTION VOICE
# ==========================================

st.markdown(
    "### 🔊 Listen to Question"
)


speak_text(

    question,

    key=f"question_voice_{index}"

)


st.markdown("---")


# ==========================================
# VOICE INPUT
# ==========================================

st.markdown(
    "### 🎤 Your Answer"
)


st.write(

    "Click the microphone button and speak your answer."

)


audio = st.audio_input(

    "🎤 Start Recording"

)


# ==========================================
# PROCESS AUDIO
# ==========================================

if audio is not None:


    st.audio(

        audio

    )


    st.success(

        "🎤 Recording captured successfully!"

    )


    if st.button(

        "📝 Convert Speech to Text",

        use_container_width=True

    ):


        audio_path = None


        try:


            # --------------------------------------
            # SAVE AUDIO TEMPORARILY
            # --------------------------------------

            with tempfile.NamedTemporaryFile(

                delete=False,

                suffix=".wav"

            ) as temp_audio:


                temp_audio.write(

                    audio.getvalue()

                )


                audio_path = temp_audio.name


            # --------------------------------------
            # SPEECH TO TEXT
            # --------------------------------------

            with st.spinner(

                "🎤 Converting your speech to text..."

            ):


                recognizer = sr.Recognizer()


                with sr.AudioFile(

                    audio_path

                ) as source:


                    audio_data = recognizer.record(

                        source

                    )


                text = recognizer.recognize_google(

                    audio_data

                )


            # --------------------------------------
            # SAVE ANSWER
            # --------------------------------------

            st.session_state.voice_answers[index] = text


            st.success(

                "✅ Speech converted successfully!"

            )


        except sr.UnknownValueError:


            st.error(

                "❌ Sorry, I could not understand your speech."

            )


        except sr.RequestError:


            st.error(

                "❌ Speech recognition service is unavailable."

            )


        except Exception as e:


            st.error(

                f"❌ Error processing audio: {e}"

            )


        finally:


            if audio_path is not None:


                if os.path.exists(

                    audio_path

                ):


                    os.remove(

                        audio_path

                    )


# ==========================================
# DISPLAY CURRENT ANSWER
# ==========================================

st.markdown("---")


st.markdown(

    "### 📝 Current Answer"

)


current_answer = st.session_state.voice_answers[index]


if current_answer.strip() != "":


    st.info(

        current_answer

    )


else:


    st.write(

        "No answer recorded yet."

    )


# ==========================================
# TEXT FALLBACK
# ==========================================

st.markdown("---")


st.markdown(

    "### ✍️ Or Type Your Answer"

)


typed_answer = st.text_area(

    "Your Answer",

    value=st.session_state.voice_answers[index],

    height=180,

    key=f"typed_answer_{index}"

)


if typed_answer.strip() != "":


    st.session_state.voice_answers[index] = typed_answer


# ==========================================
# EVALUATE ANSWER
# ==========================================

st.markdown("---")


if st.button(

    "🤖 Submit Answer for AI Evaluation",

    use_container_width=True

):


    answer = st.session_state.voice_answers[index]


    if answer.strip() == "":


        st.warning(

            "⚠️ Please record or type an answer first."

        )


    else:


        with st.spinner(

            "🤖 AI is evaluating your answer..."

        ):


            feedback = evaluate_answer(

                question,

                answer

            )


        st.session_state.voice_feedback = feedback


        st.success(

            "🎉 AI evaluation completed!"

        )


# ==========================================
# DISPLAY AI FEEDBACK
# ==========================================

if st.session_state.voice_feedback:


    st.markdown("---")


    st.markdown(

        "### 🤖 AI Feedback"

    )


    st.write(

        st.session_state.voice_feedback

    )


    st.markdown(

        "### 🔊 Listen to AI Feedback"

    )


    speak_text(

        st.session_state.voice_feedback,

        key=f"feedback_voice_{index}"

    )


# ==========================================
# NEXT QUESTION
# ==========================================

st.markdown("---")


if index < total - 1:


    if st.button(

        "➡️ Next Question",

        use_container_width=True

    ):


        st.session_state.voice_current_question += 1


        st.session_state.voice_feedback = ""


        st.rerun()


else:


    st.success(

        "🎉 You have completed the voice interview!"

    )


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(

    "🎤 Voice Interview"

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

    for answer in st.session_state.voice_answers

    if answer.strip() != ""

)


st.sidebar.metric(

    "Answered",

    answered

)


st.sidebar.markdown("---")


st.sidebar.success(

    "🎤 Voice Mode Active"

)