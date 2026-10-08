import requests
import re


def extract_word(text):
    text = text.lower().strip()

    patterns = [
        r"what does (.+?) mean",
        r"what is the meaning of (.+)",
        r"what is the definition of (.+)",
        r"what is (.+)",
        r"define (.+)",
        r"definition of (.+)",
        r"meaning of (.+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            word = match.group(1).strip().rstrip("?")

            # Remove articles
            word = re.sub(r"^(a|an|the)\s+", "", word)

            return word

    return text


def get_definition(word):
    word = word.strip().lower()

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        print(f"Looking up definition of: {word}")

        response = requests.get(
            url,
            timeout=(5, 8)
        )

        if response.status_code == 200:

            data = response.json()

            meanings = data[0].get("meanings", [])

            for meaning in meanings:

                definitions = meaning.get("definitions", [])

                if definitions:

                    definition = definitions[0].get("definition")

                    if definition:
                        return definition

        elif response.status_code == 404:

            return f"Sorry, I could not find the word {word}."

        else:

            print("Dictionary API status:", response.status_code)

    except requests.exceptions.Timeout:

        print("Dictionary API timed out.")

    except requests.exceptions.ConnectionError:

        print("Could not connect to Dictionary API.")

    except requests.exceptions.RequestException as e:

        print("Dictionary API error:", e)

    except Exception as e:

        print("Unexpected dictionary error:", e)

    return "Sorry, the dictionary service is currently unavailable."