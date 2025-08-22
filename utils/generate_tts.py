import os
from TTS.api import TTS

# Change to beter TTS
model_name = "tts_models/en/vctk/vits"
speaker_id = "p270"

def generate_tts(text):
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(output_dir, "out.wav")

    print("Loading modelu TTS...")
    print()
    tts = TTS(model_name=model_name, progress_bar=False, gpu=True)
    print()

    print(f"Generate TTS with text: '{text}'...")
    print()
    tts.tts_to_file(
        text=text,
        speaker=speaker_id,
        file_path=output_filename
    )
    print()
    print(f"Ready! File: '{output_filename}'")
    print()