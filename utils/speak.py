import random
import os
import winsound

# play sound from TTS (speak)
def speak():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "\out\out.wav")
    
    if os.path.exists(file_path):
        winsound.PlaySound(file_path, winsound.SND_FILENAME)
    else:
        print(f"ERROR: I didn't see file: '{file_path}'.")
        print()