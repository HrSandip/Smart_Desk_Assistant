# 🤖 Voice-Controlled AI Smart Desk Assistant

A voice-controlled AI smart desk assistant built with Python, Flask, Groq AI, speech recognition, weather APIs, dictionary APIs, and text-to-speech.

The project is currently being developed and tested on Windows, with a future goal of deployment on NVIDIA Jetson hardware.

## ✨ Features

- 🧠 General AI conversation using Groq
- 🎤 Microphone-based voice input
- 💬 Text-based chat
- 🌤️ Weather information using Open-Meteo
- 📖 Word definitions using Dictionary API
- 🤖 Groq fallback for dictionary requests
- 🔊 Text-to-speech support
- 🌐 Flask-based web interface
- 🔐 Secure API-key management using `.env`
- 🧩 Modular Python architecture

## 🏗️ Architecture

```text
User
 │
 ├── Voice Input → Speech Recognition ─┐
 │                                     │
 └── Text Input ───────────────────────┤
                                       ↓
                                  Flask App
                                       ↓
                                 Command Router
                                       │
                         ┌─────────────┼─────────────┐
                         ↓             ↓             ↓
                     Weather      Dictionary      Groq AI
                       API            API             │
                         │             │              │
                         └─────────────┴──────────────┘
                                       ↓
                              Assistant Response
                                       ↓
                                 Text-to-Speech
                                       ↓
                                    Speaker
```

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core development |
| Flask | Web backend |
| Groq AI | AI conversation |
| SpeechRecognition | Speech-to-text |
| PyAudio | Audio input |
| pyttsx3 | Text-to-speech |
| Requests | API communication |
| Scikit-learn | ML components |
| Wikipedia | Knowledge retrieval |
| HTML/CSS/JavaScript | Web interface |
| Open-Meteo API | Weather |
| Dictionary API | Word definitions |
| python-dotenv | Environment variables |

## 📁 Project Structure

```text
Voice_Smart_Desk/
│
├── .env.example
├── .gitignore
├── README.md
├── app.py
├── main.py
├── requirements.txt
│
├── modules/
│   ├── __init__.py
│   ├── ai_assistant.py
│   ├── command_processor.py
│   ├── dictionary_api.py
│   ├── weather_api.py
│   ├── knowledge_api.py
│   ├── speech_recognition.py
│   └── text_to_speech.py
│
├── templates/
│   └── index.html
│
├── models/
├── data/
└── config/
    └── config.py
```

## ⚙️ Requirements

- Python 3.10+
- Git
- Working microphone
- Internet connection
- Groq API key

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Voice-Smart-Desk.git
cd Voice-Smart-Desk
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 🔑 Groq API Configuration

Create a `.env` file in the project root:

```text
Voice_Smart_Desk/
└── .env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Create your Groq API key from:

https://console.groq.com/keys

### ⚠️ Security

Never upload your real `.env` file to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
.vscode/
*.log
```

Use `.env.example` as a safe template:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## ▶️ Run the Application

Start Flask:

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 💬 Example Commands

### General AI

```text
What is Artificial Intelligence?
Explain machine learning in simple words.
What is Python?
Why is Python popular?
```

### Dictionary

```text
Define algorithm.
What does machine learning mean?
What is the definition of computer?
```

### Weather

```text
What is the weather in Bhubaneswar?
What's the temperature in Delhi?
Weather in Mumbai.
```

## 🔄 How It Works

### 1. User Input

The user provides a request through voice or text.

### 2. Speech Recognition

For voice input:

```text
Microphone
    ↓
Speech Recognition
    ↓
Text
```

### 3. Command Processing

The request is routed to the appropriate service.

```text
User Request
     ↓
Command Router
     ↓
 ┌───┼──────────┐
 ↓   ↓          ↓
Weather Dictionary Groq AI
```

### 4. Response

The selected API or AI model generates the response.

### 5. Voice Output

The response can be converted into speech:

```text
AI Response
     ↓
Text-to-Speech
     ↓
Speaker
```

## 🧠 Groq AI

Groq is currently used for general conversational requests.

The project loads the API key securely from `.env`.

Current model:

```text
openai/gpt-oss-120b
```

The assistant is configured to provide concise responses suitable for voice interaction.

## 🌐 APIs

### Groq API

Used for:

- General AI questions
- Conversational responses
- Dictionary fallback
- Future AI-agent functionality

### Open-Meteo

Used for:

- Temperature
- Humidity
- Wind speed
- Location-based weather information

### Dictionary API

Used for:

- Word definitions
- Meaning lookup

## 🚧 Current Limitations

This is currently a working prototype.

Planned improvements include:

- [ ] Continuous listening
- [ ] Wake-word detection
- [ ] Conversation memory
- [ ] Groq tool/function calling
- [ ] Streaming AI responses
- [ ] Voice interruption
- [ ] Calculator tool
- [ ] Time/date tools
- [ ] Web search
- [ ] Smart-device control
- [ ] Jetson deployment

## 🚀 Future Roadmap

### Version 2 — Intelligent AI Assistant

- Conversation memory
- Groq tool calling
- Calculator
- Time and date
- Better command routing
- Improved voice interaction

### Version 3 — Real-Time Voice Assistant

- Wake word
- Continuous listening
- Streaming responses
- Voice interruption
- Natural back-and-forth conversation

### Version 4 — Smart Desk

Future hardware integration:

```text
             AI Assistant
                  │
          ┌───────┴───────┐
          ↓               ↓
       Jetson           ESP32
          │               │
      Microphone      Smart Devices
          │          ┌────┼────┐
       Speaker       ↓    ↓    ↓
                    💡   🌀   📺
                  Light Fan Display
```

## 🤖 Future Jetson Deployment

The long-term goal is to deploy the assistant on NVIDIA Jetson hardware.

Potential hardware:

- NVIDIA Jetson Nano / Jetson Orin Nano
- USB microphone
- Speaker
- Display
- ESP32 / Arduino
- Sensors
- Smart devices

## 🎯 Project Goals

- Build a practical voice-controlled AI assistant
- Integrate LLMs with Python
- Work with external APIs
- Implement speech recognition
- Implement text-to-speech
- Build an interactive web interface
- Develop an AI-agent architecture
- Explore edge AI deployment
- Integrate AI with IoT hardware

## 📌 Project Status

**🟢 Working Prototype**

### Implemented

- [x] Flask backend
- [x] Web interface
- [x] Text input
- [x] Microphone input
- [x] Speech-to-text
- [x] Groq AI integration
- [x] Weather API
- [x] Dictionary API
- [x] Dictionary fallback to AI
- [x] Text-to-speech
- [x] Environment variable protection

### Planned

- [ ] Conversation memory
- [ ] Tool/function calling
- [ ] Wake-word detection
- [ ] Continuous listening
- [ ] Streaming responses
- [ ] Interrupt handling
- [ ] Smart-device control
- [ ] Jetson deployment

## 👨‍💻 Author

**Sandip Das**

AI/ML & Data Analytics Enthusiast

Interested in:

- Artificial Intelligence
- Machine Learning
- Generative AI
- Data Analytics
- Computer Vision
- Edge AI
- IoT

## ⭐ Future Vision

The goal is to transform this prototype into a real-time AI smart desk assistant capable of understanding natural voice commands, maintaining conversations, using external tools, controlling smart devices, and running on edge hardware.

```text
Current Prototype
       ↓
Voice Assistant
       ↓
AI Assistant
       ↓
AI Agent
       ↓
Real-Time Voice Assistant
       ↓
Smart Desk
       ↓
Jetson + AI + IoT
```

If you find this project interesting, consider giving the repository a ⭐.
