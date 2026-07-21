import streamlit as st

from modules.ai_client import ask_ai
from modules.text_to_speech import speak_text, stop_speaking


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="💬",
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

if "assistant_messages" not in st.session_state:

    st.session_state.assistant_messages = []


# ==========================================
# HEADER
# ==========================================

st.title(
    "💬 AI Chat Assistant"
)


st.markdown(
    """
    ### 🤖 Your Personal Interview & Career Assistant

    Ask questions about:

    🎤 Interview Preparation  
    💻 Technical Questions  
    🐍 Python  
    🤖 AI / ML  
    🔐 Cybersecurity  
    📄 Resume Improvement  
    🎯 Career Guidance
    """
)


st.markdown("---")


# ==========================================
# CHAT HISTORY
# ==========================================

for index, message in enumerate(

    st.session_state.assistant_messages

):


    if message["role"] == "user":

        st.markdown(
            "### 👤 You"
        )


        st.markdown(
            f"""
            <div class="user-message">
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


    else:

        st.markdown(
            "### 🤖 AI"
        )


        st.markdown(
            f"""
            <div class="ai-message">
            {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


        col1, col2 = st.columns(2)


        with col1:

            if st.button(
                "🔊 Play Voice",
                key=f"assistant_play_{index}",
                use_container_width=True
            ):

                speak_text(
                    message["content"],
                    key=f"assistant_speech_{index}"
                )


        with col2:

            if st.button(
                "⏹ Stop Voice",
                key=f"assistant_stop_{index}",
                use_container_width=True
            ):

                stop_speaking()


    st.markdown("---")


# ==========================================
# TYPE QUESTION
# ==========================================

st.subheader(
    "💬 Ask Your Question"
)


question = st.text_area(

    "Type your question below:",

    height=130,

    key="assistant_question"

)


# ==========================================
# SEND QUESTION
# ==========================================

if st.button(

    "🚀 Send Question",

    use_container_width=True

):


    if question.strip() == "":

        st.warning(
            "⚠️ Please type a question first."
        )


    else:

        st.session_state.assistant_messages.append(

            {

                "role": "user",

                "content": question

            }

        )


        with st.spinner(
            "🤖 AI is thinking..."
        ):


            response = ask_ai(

                f"""
You are InterviewIQ AI.

The user asks:

{question}

Give a clear, helpful answer.

You can help with:

- Interview preparation
- Technical questions
- Python
- AI and Machine Learning
- Cybersecurity
- Resume improvement
- Career guidance
"""

            )


        st.session_state.assistant_messages.append(

            {

                "role": "assistant",

                "content": response

            }

        )


        st.rerun()


# ==========================================
# CLEAR CHAT
# ==========================================

st.markdown("---")


if st.button(

    "🗑️ Clear Conversation",

    use_container_width=True

):

    st.session_state.assistant_messages = []

    st.rerun()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "💬 AI Chat Assistant"
)


st.sidebar.write(
    "💬 Type your questions."
)


st.sidebar.write(
    "🔊 Play AI answers."
)


st.sidebar.write(
    "⏹ Stop AI voice anytime."
)