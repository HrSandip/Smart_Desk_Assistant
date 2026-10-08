import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    print(f"Assistant: {text}")

    engine.say(text)
    engine.runAndWait()