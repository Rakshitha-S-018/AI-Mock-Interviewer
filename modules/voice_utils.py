import speech_recognition as sr


# ==========================================
# SPEECH TO TEXT
# ==========================================

def speech_to_text(audio_file):

    recognizer = sr.Recognizer()


    try:

        with sr.AudioFile(audio_file) as source:

            audio = recognizer.record(source)


        text = recognizer.recognize_google(
            audio
        )


        return text


    except sr.UnknownValueError:

        return ""


    except sr.RequestError:

        return ""


    except Exception:

        return ""