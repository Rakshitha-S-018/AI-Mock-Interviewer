import threading
import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 165)


def _speak(text):

    engine.say(text)

    engine.runAndWait()


def speak(text):

    thread = threading.Thread(
        target=_speak,
        args=(text,)
    )

    thread.start()