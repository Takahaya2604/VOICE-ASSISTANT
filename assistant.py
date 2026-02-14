import speech_recognition as sr
import pyttsx3
import speech_recognition
import pyttsx3
import pyaudio


# text to speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


# speech to text
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""


def reply(text):

    if "hello" in text:
        return "Hello, how are you"

    elif "your name" in text:
        return "My name is simple python bot"

    elif "time" in text:
        import datetime
        return datetime.datetime.now().strftime("The time is %H:%M")

    elif "bye" in text:
        return "Goodbye"
    
    else:
        return "Sorry, I did not understand"


# main loop
speak("Voice bot started")

while True:
    user_text = listen()

    if user_text == "":
        continue

    answer = reply(user_text)

    print("Bot:", answer)
    speak(answer)

    if "bye" in user_text:
        break
