# kin-voice-assistant
# 🤖 Kinyarwanda Voice Assistant

A voice-enabled Kinyarwanda assistant that simulates how intelligent humanoid robots hear, understand, and speak in local languages. This project showcases a full speech pipeline — from audio input to voice output — tailored for the Rwandan context.

---

## 🧠 Project Overview

Modern intelligent robots rely heavily on voice interaction to communicate with humans. But most speech technology overlooks African languages like Kinyarwanda.

This project bridges that gap.

By combining Automatic Speech Recognition (ASR), Natural Language Processing (NLP), and Text-to-Speech (TTS), this assistant enables a robot to:
- **Listen** to spoken Kinyarwanda (via KinyaWhisper),
- **Understand** the meaning using basic NLP,
- **Respond** clearly through speech (using TTS).

It’s a lightweight yet powerful prototype that brings robotics closer to local communities.

---

## 🎯 Key Features

- 🎙️ **Speech-to-Text** with [KinyaWhisper}
- 🧠 **Question Understanding** using a simple NLP logic
- 🔊 **Text-to-Speech** via gTTS or Coqui TTS
- 🗂️ Modular and beginner-friendly code structure
- 🌍 Focused on **Kinyarwanda**, Rwanda’s national language

---

## 🚀 How It Works

1. **User speaks** in Kinyarwanda (recorded or live audio).
2. **KinyaWhisper** transcribes the audio to text.
3. **NLP module** matches the transcribed question to a known response.
4. **TTS module** converts the answer to speech.
5. **Robot replies** in Kinyarwanda.

---

## 🛠️ Tech Stack

- Python 3.x
- [KinyaWhisper] for ASR
- gTTS or Coqui TTS for speech synthesis
- Optional: Gradio or Streamlit for UI
- Git + GitHub for version control

---

## 📦 Installation

```bash
git clone https://github.com/Emmy-Grettv/kin-voice-assistant.git
cd kinyarwanda-voice-assistant
pip install -r requirements.txt

