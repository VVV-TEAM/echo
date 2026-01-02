import random
import os
import winsound

# play sound from TTS (speak)
def speak(sound=None):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    if sound == "uh":
        file_path = os.path.join(parent_directory, "out", "Uh-huh.wav")
    else:
        file_path = os.path.join(parent_directory, "out", "out.wav")

    if os.path.exists(file_path):
        winsound.PlaySound(file_path, winsound.SND_FILENAME)
    else:
        print(f"ERROR: I didn't see file: '{file_path}'.")
        print()