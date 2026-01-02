# 🎙️ Echo

**Echo** is a simple voice assistant written in Python – something like **Siri** or **Alexa**, but in an open-source and experimental form 🚀.  
The project is in its early stage, but it can already listen, talk, and perform basic tasks.  

---

## ✨ Features

✅ Speech recognition (STT – Google Speech Recognition)  
✅ Text-to-speech (TTS – Coqui AI)  
✅ Response generation (OpenAI API)  
✅ Web search (Exa API)  
✅ Play music from Spotify (Spotipy)  
✅ Send messages on Discord (Discord API)  
✅ Weather information (Open-Meteo API)  
✅ Current time in different cities (`datetime` + `zoneinfo`)  

---

## 🛠️ Planned Features

- Smart home control  
- Full Linux compatibility  
- Visual interface (possibly as a plugin)   
- Support for multiple AI models (not only OpenAI)  
- Extended plugin system  

---

## ⚙️ Tech Stack

- **Python 3.10.11**  
- **STT**: Google Speech Recognition  
- **TTS**: Coqui AI  
- **AI Responses**: OpenAI API  
- **Search**: Exa API  
- **Spotify**: Spotipy  
- **Discord**: Discord API  
- **Weather**: Open-Meteo API  
- **Timezones**: datetime + zoneinfo  
- **Audio output**: winsound (Windows, Linux support planned)  

---

## 🚀 Installation & Usage

1. Clone the repository:  
   ```bash
   git clone https://github.com/YourAccount/Echo.git
   cd Echo
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run Echo:  
   ```bash
   python main.py
   ```

📌 Requirements: microphone + speakers/headphones.  
📌 Activation: include the word **“Echo”** in your spoken sentence.  

---

## 🔌 Plugins

Echo supports a **plugin system**, making it easy to extend functionality.  
Documentation for plugins is still in progress – but check the repository for early examples.  

---

## 📌 Project Status

🧪 Echo is in an **early development stage** – it works, but some dependencies may be missing and errors can occur.  
The project is continuously updated and improved.  

---

## 📄 License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute it.  

---