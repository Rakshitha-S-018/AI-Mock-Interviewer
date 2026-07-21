import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        print("Listening...")

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        return text

    except:

        return ""