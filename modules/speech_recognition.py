import speech_recognition as sr
import pyaudio


def get_default_microphone():

    p = pyaudio.PyAudio()

    try:
        device = p.get_default_input_device_info()

        index = int(device["index"])
        name = device["name"]

        print("\nDefault Windows microphone:")
        print(f"Index: {index}")
        print(f"Device: {name}")

        return index

    except Exception as e:
        print(f"Could not find default microphone: {e}")
        return None

    finally:
        p.terminate()


def listen():

    recognizer = sr.Recognizer()

    microphone_index = get_default_microphone()

    if microphone_index is None:
        print("No microphone found.")
        return None

    try:

        with sr.Microphone(device_index=microphone_index) as source:

            print("\nAdjusting microphone...")
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Listening... Speak now!")

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        print("Processing...")

        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return None

    except sr.UnknownValueError:

        print("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError as e:

        print(f"Speech recognition service error: {e}")
        return None

    except Exception as e:

        print(f"Microphone error: {e}")
        return None