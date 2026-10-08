from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import io
import wave

from modules.ai_assistant import ask_ai
from modules.dictionary_api import extract_word, get_definition
from modules.weather_api import extract_city, get_weather


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def process_command_text(command):

    command = command.strip()

    if not command:
        return "I did not receive any command."

    print(f"\nUser: {command}")

    text = command.lower().strip()

    # ==========================================
    # EXIT
    # ==========================================

    exit_commands = [
        "exit",
        "quit",
        "goodbye",
        "bye",
        "stop assistant"
    ]

    if text in exit_commands:

        response = "Goodbye! Have a nice day."

        print(f"Assistant: {response}")

        return response


    # ==========================================
    # WEATHER
    # ==========================================

    weather_keywords = [
        "weather in",
        "temperature in",
        "forecast in",
        "weather of",
        "temperature of",
        "weather for",
        "temperature for"
    ]

    if any(keyword in text for keyword in weather_keywords):

        city = extract_city(command)

        if city is None:

            response = "Please tell me the city name."

        else:

            print(f"Weather city: {city}")

            response = get_weather(city)

        print(f"Assistant: {response}")

        return response


    # ==========================================
    # DICTIONARY
    # ==========================================

    dictionary_keywords = [
        "define ",
        "definition of ",
        "meaning of ",
        "what does "
    ]

    if any(keyword in text for keyword in dictionary_keywords):

        word = extract_word(command)

        print(f"Dictionary word: {word}")

        definition = get_definition(word)

        # If dictionary API fails, use Groq
        if (
            not definition
            or "service is currently unavailable" in definition.lower()
            or "could not connect" in definition.lower()
        ):

            print("Dictionary API unavailable.")
            print("Using Groq AI for definition...")

            response = ask_ai(
                f"Define the word '{word}' in simple English. "
                f"Give a short and clear definition suitable for voice output."
            )

        else:

            response = f"The definition of {word} is {definition}"

        print(f"Assistant: {response}")

        return response


    # ==========================================
    # EVERYTHING ELSE → GROQ AI
    # ==========================================

    print("Sending request to Groq AI...")

    response = ask_ai(command)

    print(f"Assistant: {response}")

    return response


# ==========================================
# TEXT PROCESSING API
# ==========================================

@app.route("/process", methods=["POST"])
def process():

    data = request.get_json()

    command = data.get("command", "")

    response = process_command_text(command)

    return jsonify({
        "response": response
    })


# ==========================================
# SPEECH TRANSCRIPTION
# ==========================================

@app.route("/transcribe", methods=["POST"])
def transcribe():

    if "audio" not in request.files:

        return jsonify({
            "success": False,
            "error": "No audio received."
        }), 400


    try:

        audio_file = request.files["audio"]

        audio_bytes = audio_file.read()

        wav_file = wave.open(
            io.BytesIO(audio_bytes),
            "rb"
        )

        sample_rate = wav_file.getframerate()

        sample_width = wav_file.getsampwidth()

        channels = wav_file.getnchannels()

        frames = wav_file.readframes(
            wav_file.getnframes()
        )

        wav_file.close()


        print("\nAudio received")

        print("Sample rate:", sample_rate)

        print("Channels:", channels)

        print("Sample width:", sample_width)


        recognizer = sr.Recognizer()

        audio_data = sr.AudioData(
            frames,
            sample_rate,
            sample_width
        )


        print("Converting speech to text...")


        text = recognizer.recognize_google(
            audio_data,
            language="en-IN"
        )


        print("Recognized:", text)


        response = process_command_text(text)


        return jsonify({

            "success": True,

            "text": text,

            "response": response

        })


    except sr.UnknownValueError:

        return jsonify({

            "success": False,

            "error": "I could not understand your speech."

        })


    except sr.RequestError as e:

        return jsonify({

            "success": False,

            "error": f"Speech recognition service error: {e}"

        })


    except Exception as e:

        print("Transcription error:", e)

        return jsonify({

            "success": False,

            "error": str(e)

        })


# ==========================================
# START FLASK
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )