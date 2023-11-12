import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
engine.setProperty('rate',160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

Dictapp = {"commandprompt":"cmd", "paint":"paint", "word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpoint,WhatsApp:WhatsApp"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("siri","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        web = "https://www."+ query
        webbrowser.open(web)
        # webbrowser.open(f"https://www.{query}")
    else:
        keys = list(Dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {Dictapp[app]}")

def closeappweb(query):
    speak("Closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        sleep(0,5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    
    else:
        keys = list(Dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill  /f  /in  {Dictapp[app].exe}")