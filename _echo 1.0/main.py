# imports
from utils.voice_input import listen
from utils.core import core
from utils.plugin_manager import load_plugins, plugins
from utils.speak import speak

wake_word = ["echo", "hey echo", "okay echo"]

load_plugins()

# Main while
while True:
    user_input = listen()

    if user_input in wake_word:
        print("I wait 5 seconds for your question!")

        speak("uh")

        question = listen(timeout=5)

        if question:
            core(question, plugins)

        else:
            print("I don't got any question")
            continue

    elif any(trigger in user_input for trigger in ["echo"]):
        core(user_input, plugins)

    else:
        continue