import speech_recognition as sr
r = sr.Recognizer()
def listen():
    with sr.Microphone() as mic:
        print("Say something!")
        audio = r.listen(mic,phrase_time_limit=5)
        
        rec = r.recognize_google(audio)

        rec = rec.lower()
        return rec

