import speech_recognition as sr

# listen user voice
def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎙️ I listen you")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-US")
        print("👂 You:", text)
        print()
        return text.lower()
    
    except sr.UnknownValueError:
        print("😕 I don't understant.")
        print()
        return ""
    
    except sr.RequestError:
        print("🚫 Google doesn't respone.")
        print()
        return ""