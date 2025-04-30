from transformers import WhisperProcessor, WhisperForConditionalGeneration
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import soundfile as sf
from gtts import gTTS
import os
import torch


os.makedirs("audio_inputs", exist_ok=True)
os.makedirs("audio_outputs", exist_ok=True)

# Load KinyaWhisper model & processor
processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")
model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")

def record_audio(filename="audio_inputs/input.wav", duration=5, sample_rate=16000):
    print(":loud_sound: Recording... (5 seconds)")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    write(filename, sample_rate, audio)
    return filename

# Transcribe audio using KinyaWhisper model
def transcribe_audio(audio_path):
    audio_data, samplerate = sf.read(audio_path)
    if len(audio_data.shape) > 1:  # If stereo, convert to mono
        audio_data = np.mean(audio_data, axis=1)
    inputs = processor(audio_data, sampling_rate=samplerate, return_tensors="pt")
    # Prepare decoder input ids
    decoder_input_ids = model.config.decoder_start_token_id
    decoder_input_ids = torch.tensor([[decoder_input_ids]], device=inputs.input_features.device)
    predicted_ids = model.generate(
        inputs.input_features,
        decoder_input_ids=decoder_input_ids,
    )
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription.strip()
# Q&A pairs
qa_pairs = {
    "muraho neza": "yego",
    "ninde": "njye ndi Nyirahabimana",
    "ndagukunda": "njye oya",
    "uri gutekereza": "yego ndi gutekereza",
    "murabeho": "turabashimiye"
}
def get_answer(question):
    # Basic normalization: lowercasing and removing punctuation
    question = question.lower().strip().replace('?', '')
    for key in qa_pairs:
        if key in question:
            return qa_pairs[key]
    return "Sinzi igisubizo."
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("audio_outputs/answer.mp3")
    # Play audio depending on OS
    if os.name == 'nt':  # Windows
        os.system("start audio_outputs/answer.mp3")
    else:  # Linux / Mac
        os.system("mpg321 audio_outputs/answer.mp3")
def main():
    audio_path = record_audio()
    print(":studio_microphone: Audio recorded.")
    question = transcribe_audio(audio_path)
    print(f":memo: Transcribed: {question}")
    answer = get_answer(question)
    print(f":robot_face: Answer: {answer}")
    speak(answer)
if __name__ == "__main__":
    main()





