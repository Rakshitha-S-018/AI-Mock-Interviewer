import streamlit as st


def speak_text(text, key=None):

    """
    Browser-based text-to-speech.
    """

    if not text or text.strip() == "":
        return


    safe_text = (

        text

        .replace("\\", "\\\\")

        .replace("`", "\\`")

        .replace("${", "\\${")

    )


    component_key = key or "speech_component"


    st.components.v1.html(

        f"""
        <script>

        function speakText() {{

            window.speechSynthesis.cancel();

            const text = `{safe_text}`;

            const speech =
                new SpeechSynthesisUtterance(text);

            speech.lang = "en-US";

            speech.rate = 1.0;

            speech.pitch = 1.0;

            window.speechSynthesis.speak(speech);

        }}


        function stopSpeaking() {{

            window.speechSynthesis.cancel();

        }}

        </script>


        <button onclick="speakText()">

            ▶️ Play Voice

        </button>


        <button onclick="stopSpeaking()">

            ⏹ Stop Voice

        </button>

        """,

        height=70,

        scrolling=False

    )


def stop_speaking():

    """
    Compatibility function.

    Browser speech is stopped using JavaScript.
    """

    st.components.v1.html(

        """
        <script>

        window.speechSynthesis.cancel();

        </script>

        """,

        height=0

    )