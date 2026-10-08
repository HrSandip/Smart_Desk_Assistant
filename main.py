from modules.speech_recognition import listen
from modules.command_processor import process_command

from modules.dictionary_api import (
    extract_word,
    get_definition
)

from modules.weather_api import (
    extract_city,
    get_weather
)

from modules.text_to_speech import speak


def main():

    speak("Hello! I am your smart desk assistant.")

    while True:

        # Listen
        command = listen()

        if command is None:
            continue

        # Identify command
        command_type = process_command(command)

        # Exit
        if command_type == "exit":

            speak("Goodbye! Have a nice day.")
            break

        # Dictionary
        elif command_type == "dictionary":

            word = extract_word(command)

            print(f"\nWord: {word}")

            definition = get_definition(word)

            speak(
                f"The definition of {word} is {definition}"
            )

        # Weather
        elif command_type == "weather":

            city = extract_city(command)

            if city is None:

                speak(
                    "Please tell me the city name."
                )

                continue

            print(f"\nCity: {city}")

            weather = get_weather(city)

            speak(weather)

        # Unknown
        else:

            speak(
                "Sorry, I don't know how to handle "
                "that command yet."
            )


if __name__ == "__main__":
    main()