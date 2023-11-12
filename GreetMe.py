import pyttsx3
# import webbrowser
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning,sir")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon,sir") 
    elif hour > 18 and hour <= 19:
        speak("Good Evening")
    elif hour > 19 and hour < 24:
        speak("Good Night")
    else:
        speak("Good Evening,sir")
    
    speak("Please tell me how can I help you")
    
