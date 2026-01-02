import os
from TTS.api import TTS

class TTSGenerator:
    def __init__(self):
        self.model_name = "tts_models/en/vctk/vits"
        self.speaker_id = "p270"

    def generate_tts(self, text):
        output_dir = "assets/TTS_output"
        os.makedirs(output_dir, exist_ok=True)
        output_filename = os.path.join(output_dir, "out.wav")

        print("Loading modelu TTS...")
        print()
        tts = TTS(model_name=self.model_name, progress_bar=False, gpu=True)
        print()

        print(f"Generate TTS with text: '{text}'...")
        print()
        tts.tts_to_file(
            text=text,
            speaker=self.speaker_id,
            file_path=output_filename
        )
        print()
        print(f"Ready! File: '{output_filename}'")
        print()