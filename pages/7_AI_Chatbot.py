import streamlit as st
import speech_recognition as sr
import tempfile
import os

from modules.chatbot import chatbot_response
from modules.text_to_speech import speak_text, stop_speaking


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
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
# SESSION STATE
# ==========================================

if "chatbot_messages" not in st.session_state:

    st.session_state.chatbot_messages = []


if "chatbot_question" not in st.session_state:

    st.session_state.chatbot_question = ""


if "chatbot_audio" not in st.session_state:

    st.session_state.chatbot_audio = None


if "audio_deleted" not in st.session_state:

    st.session_state.audio_deleted = False


# ==========================================
# HEADER
# ==========================================

st.title(
    "🤖 InterviewIQ AI Chatbot"
)


st.markdown(
    """
    Ask InterviewIQ AI anything about:

    🎤 Interview Preparation  
    💻 Technical Questions  
    🐍 Python  
    🤖 Artificial Intelligence  
    🔐 Cybersecurity  
    📄 Resume Improvement  
    🎯 Career Guidance
    """
)


st.markdown("---")


# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for index, message in enumerate(
    st.session_state.chatbot_messages
):

    if message["role"] == "user":

        st.markdown("### 👤 You")

        st.markdown(
            f"""
            <div class="user-message">
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


    else:

        st.markdown("### 🤖 InterviewIQ AI")

        st.markdown(
            f"""
            <div class="ai-message">
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


        col1, col2 = st.columns(2)


        # ==========================================
        # PLAY VOICE
        # ==========================================

        with col1:

            if st.button(
                "🔊 Play Voice",
                key=f"play_voice_{index}",
                use_container_width=True
            ):

                try:

                    speak_text(
                        message["content"]
                    )

                except Exception as e:

                    st.error(
                        f"❌ Voice error: {e}"
                    )


        # ==========================================
        # STOP VOICE
        # ==========================================

        with col2:

            if st.button(
                "⏹ Stop Voice",
                key=f"stop_voice_{index}",
                use_container_width=True
            ):

                try:

                    stop_speaking()

                    st.success(
                        "⏹ Voice stopped."
                    )

                except Exception as e:

                    st.error(
                        f"❌ Error stopping voice: {e}"
                    )


    st.markdown("---")


# ==========================================
# TEXT INPUT
# ==========================================

st.subheader(
    "💬 Ask InterviewIQ AI"
)


question_text = st.text_area(

    "Type your question here:",

    height=120,

    key="question_text_widget"

)


# ==========================================
# VOICE INPUT
# ==========================================

st.markdown(
    "### 🎤 Or Ask Using Voice"
)


audio = st.audio_input(
    "🎤 Record Your Question"
)


# ==========================================
# SAVE NEW RECORDING
# ==========================================

if audio is not None:

    if not st.session_state.audio_deleted:

        st.session_state.chatbot_audio = audio


# ==========================================
# RESET DELETE FLAG
# ==========================================

if audio is None:

    st.session_state.audio_deleted = False


# ==========================================
# DISPLAY SAVED RECORDING
# ==========================================

if st.session_state.chatbot_audio is not None:

    st.markdown(
        "### 🎤 Recorded Question"
    )


    audio_col, delete_col = st.columns(
        [5, 1]
    )


    # ==========================================
    # AUDIO PLAYER
    # ==========================================

    with audio_col:

        st.audio(
            st.session_state.chatbot_audio
        )


    # ==========================================
    # DELETE RECORDING
    # ==========================================

    with delete_col:

        if st.button(
            "🗑️ Delete",
            key="delete_recording",
            use_container_width=True
        ):

            # Delete the saved recording

            st.session_state.chatbot_audio = None


            # Prevent Streamlit from saving
            # the same audio again

            st.session_state.audio_deleted = True


            st.rerun()


    # ==========================================
    # CONVERT VOICE TO TEXT
    # ==========================================

    if st.button(
        "📝 Convert Voice to Text",
        use_container_width=True
    ):

        audio_path = None


        try:

            # ----------------------------------
            # SAVE TEMPORARY AUDIO FILE
            # ----------------------------------

            with tempfile.NamedTemporaryFile(

                delete=False,

                suffix=".wav"

            ) as temp_audio:

                temp_audio.write(

                    st.session_state.chatbot_audio.getvalue()

                )

                audio_path = temp_audio.name


            # ----------------------------------
            # SPEECH RECOGNITION
            # ----------------------------------

            with st.spinner(
                "🎤 Converting voice to text..."
            ):

                recognizer = sr.Recognizer()


                with sr.AudioFile(
                    audio_path
                ) as source:

                    audio_data = recognizer.record(
                        source
                    )


                converted_text = recognizer.recognize_google(
                    audio_data
                )


            # ----------------------------------
            # SAVE CONVERTED QUESTION
            # ----------------------------------

            st.session_state.chatbot_question = converted_text


            st.success(
                "✅ Voice converted to text successfully!"
            )


            st.info(
                converted_text
            )


            # Remove recording after conversion

            st.session_state.chatbot_audio = None

            st.session_state.audio_deleted = True


            st.rerun()


        except sr.UnknownValueError:

            st.error(
                "❌ Could not understand your voice."
            )


        except sr.RequestError:

            st.error(
                "❌ Speech recognition service unavailable."
            )


        except Exception as e:

            st.error(
                f"❌ Error converting voice: {e}"
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
# SHOW CONVERTED QUESTION
# ==========================================

if st.session_state.chatbot_question != "":

    st.markdown(
        "### 📝 Converted Question"
    )


    st.info(
        st.session_state.chatbot_question
    )


# ==========================================
# ASK AI
# ==========================================

if st.button(
    "🚀 Ask InterviewIQ AI",
    use_container_width=True
):

    # --------------------------------------
    # GET TYPED QUESTION
    # --------------------------------------

    question = question_text.strip()


    # --------------------------------------
    # IF TEXT IS EMPTY, USE VOICE QUESTION
    # --------------------------------------

    if question == "":

        question = st.session_state.chatbot_question.strip()


    # --------------------------------------
    # VALIDATION
    # --------------------------------------

    if question == "":

        st.warning(
            "⚠️ Please type or record a question first."
        )


    else:

        # --------------------------------------
        # SAVE USER QUESTION
        # --------------------------------------

        st.session_state.chatbot_messages.append(

            {

                "role": "user",

                "content": question

            }

        )


        # --------------------------------------
        # GET AI RESPONSE
        # --------------------------------------

        with st.spinner(
            "🤖 InterviewIQ AI is thinking..."
        ):

            response = chatbot_response(
                question
            )


        # --------------------------------------
        # SAVE AI RESPONSE
        # --------------------------------------

        st.session_state.chatbot_messages.append(

            {

                "role": "assistant",

                "content": response

            }

        )


        # --------------------------------------
        # CLEAR QUESTION
        # --------------------------------------

        st.session_state.chatbot_question = ""


        st.rerun()


# ==========================================
# CLEAR CHAT
# ==========================================

st.markdown("---")


if st.button(
    "🗑️ Clear Chat",
    use_container_width=True
):

    st.session_state.chatbot_messages = []

    st.session_state.chatbot_question = ""

    st.session_state.chatbot_audio = None

    st.session_state.audio_deleted = True

    st.rerun()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "🤖 AI Chatbot"
)


st.sidebar.write(
    "💬 Type your question."
)


st.sidebar.write(
    "🎤 Ask using voice."
)


st.sidebar.write(
    "🔊 Play AI response when you want."
)


st.sidebar.write(
    "⏹ Stop voice anytime."
)