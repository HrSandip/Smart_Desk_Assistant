from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from modules.dictionary_api import extract_word, get_definition
from modules.weather_api import extract_city, get_weather
from modules.knowledge_api import get_knowledge
from modules.ai_assistant import ask_ai


# =========================================================
# TRAINING DATA
# =========================================================

training_data = {

    "dictionary": [

        # Definition
        "define machine",
        "define computer",
        "define algorithm",
        "define data",
        "define programming",
        "define software",
        "define hardware",
        "define database",
        "define variable",
        "define function",
        "define class",
        "define object",

        # Meaning
        "meaning of machine",
        "meaning of computer",
        "meaning of algorithm",
        "meaning of data",
        "meaning of software",
        "meaning of hardware",

        # What does
        "what does machine mean",
        "what does computer mean",
        "what does algorithm mean",
        "what does data mean",

        # What is
        "what is a machine",
        "what is a computer",
        "what is an algorithm",
        "what is data",
        "what is software",
        "what is hardware",
        "what is a database",
        "what is a variable",
        "what is a function",
        "what is a class",
        "what is an object",
        "what is a list",
        "what is a tuple",

        # Natural language
        "can you define machine",
        "can you define computer",
        "can you explain algorithm",
        "give me the meaning of machine",
        "give me the definition of computer",
        "tell me the meaning of algorithm",
        "i want to know what machine means",
        "i want to know what a computer is"
    ],


    "weather": [

        "weather",
        "weather today",
        "current weather",
        "today weather",
        "weather forecast",
        "forecast",
        "temperature",
        "current temperature",
        "temperature today",

        "what is the weather",
        "what is the weather today",
        "what is the temperature",
        "what is the temperature today",

        "weather in delhi",
        "weather in mumbai",
        "weather in cuttack",
        "weather in bhubaneswar",

        "temperature in delhi",
        "temperature in mumbai",
        "temperature in cuttack",
        "temperature in bhubaneswar",

        "what is the weather in delhi",
        "what is the weather in mumbai",
        "what is the weather in cuttack",

        "what is the temperature in delhi",
        "what is the temperature in mumbai",
        "what is the temperature in cuttack",

        "will it rain",
        "will it rain today",
        "is it raining",
        "is it going to rain",
        "is it hot today",
        "is it cold today",

        "tell me the weather",
        "tell me today's weather",
        "tell me the temperature",
        "give me weather information"
    ],


    "knowledge": [

        "what is python",
        "tell me about python",
        "explain python",
        "information about python",
        "about python",

        "who invented python",
        "who created python",
        "who developed python",
        "creator of python",

        "when was python created",
        "when was python invented",

        "what is india",
        "tell me about india",
        "information about india",
        "where is india",

        "who is albert einstein",
        "tell me about albert einstein",

        "what is artificial intelligence",
        "tell me about artificial intelligence",
        "explain artificial intelligence",

        "what is machine learning",
        "tell me about machine learning",
        "explain machine learning",

        "what is deep learning",
        "tell me about deep learning",

        "what is data science",
        "tell me about data science",

        "what is programming",
        "tell me about programming",

        "tell me about computers",
        "explain computers",

        "can you explain python",
        "can you explain machine learning",
        "give me information about python"
    ],


    "exit": [

        "exit",
        "quit",
        "stop",
        "goodbye",
        "bye",
        "good bye",
        "close assistant",
        "stop assistant",
        "shut down",
        "shutdown"
    ]
}


# =========================================================
# PREPARE TRAINING DATA
# =========================================================

training_sentences = []
training_labels = []

for intent, sentences in training_data.items():

    for sentence in sentences:

        training_sentences.append(sentence)
        training_labels.append(intent)


# =========================================================
# TF-IDF MODEL
# =========================================================

vectorizer = TfidfVectorizer(

    lowercase=True,

    # Understand phrases as well as individual words
    ngram_range=(1, 2),

    # Ignore extremely rare words
    min_df=1,

    # Give more importance to useful terms
    sublinear_tf=True
)


X = vectorizer.fit_transform(training_sentences)


# =========================================================
# LOGISTIC REGRESSION
# =========================================================

model = LogisticRegression(

    max_iter=2000,

    # Helps when classes have different numbers of examples
    class_weight="balanced"
)


model.fit(X, training_labels)


# =========================================================
# COMMAND PROCESSOR
# =========================================================

def process_command(command):
    """Classify a user command into a supported intent."""
    text = (command or "").strip()

    if not text:
        return "unknown"

    lowered = text.lower()

    if any(keyword in lowered for keyword in ["exit", "quit", "stop", "goodbye", "bye", "shutdown"]):
        return "exit"

    if any(keyword in lowered for keyword in ["weather", "temperature", "forecast", "rain", "raining", "cold", "hot"]):
        return "weather"

    if any(keyword in lowered for keyword in ["define", "definition", "meaning of", "what does", "what is the meaning of", "what is the definition of"]):
        return "dictionary"

    if any(keyword in lowered for keyword in ["what is", "who is", "who created", "who invented", "when was", "tell me about", "explain", "information about"]):
        return "knowledge"

    prediction = model.predict(vectorizer.transform([text]))[0]
    return prediction


def process_command_text(command):
    command = command.strip()

    if not command:
        return "I did not receive any command."

    print(f"\nUser: {command}")

    command_type = process_command(command)

    if command_type == "dictionary":

        word = extract_word(command)

        print(f"Word: {word}")

        definition = get_definition(word)

        response = f"The definition of {word} is {definition}"

    elif command_type == "weather":

        city = extract_city(command)

        if city is None:
            response = "Please tell me the city name."

        else:
            print(f"City: {city}")

            response = get_weather(city)

    elif command_type == "knowledge":

        response = get_knowledge(command)

    elif command_type == "exit":

        response = "Goodbye! Have a nice day."

    else:

        # Send unknown/general questions to Groq AI
        response = ask_ai(command)

    print(f"Assistant: {response}")

    return response