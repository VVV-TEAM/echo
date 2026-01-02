import random
import os
import winsound

class Speaker:
    def __init__(self):
        self.yes_sound = "assets/sounds/wake.wav"
        self.error_sound = "assets/sounds/error.wav"
        self.out_sound = "assets/TTS_output/out.wav"

        self.script_directory = os.path.dirname(os.path.abspath(__file__))
        self.project_root = os.path.dirname(os.path.dirname(self.script_directory))

    def ready_sound(self, sound):
        match sound:
            case "yes":
                self.speak(self.yes_sound)
            case "out":
                self.speak(self.out_sound)
            case "error":
                self.speak(self.error_sound)
            case _:
                self.speak(self.error_sound)

    def speak(self, sound):
        file_path = os.path.normpath(os.path.join(self.project_root, sound))

        if os.path.exists(file_path):
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        else:
            print(f"ERROR: I didn't see file: '{file_path}'.")
            winsound.PlaySound("error.wav", winsound.SND_FILENAME)
            print()