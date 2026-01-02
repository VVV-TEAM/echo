from src.speech.STT_generator import STTGenerator
from src.speech.TTS_generator import TTSGenerator
from src.core.ai_client import AIclient
from src.audio.speaker import Speaker

class VoiceAssistant:
    def __init__(self):
        self.wake_word = ["echo", "hey echo", "okay echo"]

    def run(self):
        while True:
            user_input = STTGenerator().listen()

            if user_input in self.wake_word:
                Speaker().ready_sound("yes")
                print("I wait 5 seconds for your question!")
                print()
                question = STTGenerator().listen(timeout=5)
                if question:
                    response = AIclient().ai_respond(question)
                    TTSGenerator().generate_tts(response)
                    Speaker().ready_sound("out")

                else:
                    print("I don't got any question")
                    print()

            elif any(trigger in user_input for trigger in self.wake_word):
                response = AIclient().ai_respond(user_input)
                TTSGenerator().generate_tts(response)
                Speaker().ready_sound("out")

            else:
                continue