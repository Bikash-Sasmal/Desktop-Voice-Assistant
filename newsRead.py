import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"Say that again")
        return "None"
    return query

def latestNews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3de91c406f6a4e8b82f0e4202a40a164",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3de91c406f6a4e8b82f0e4202a40a164",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3de91c406f6a4e8b82f0e4202a40a164",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3de91c406f6a4e8b82f0e4202a40a164",
               }
    content = None
    url = None
    speak("which field news do you want, [business], [health], [technology], [entertainment]")
    print("which field news do you want, [business], [health], [technology], [entertainment]")
    # field = takeCommand().lower()
    # print(field)
    field = input("Type field news that you want: ")
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url news found")
            break
        else:
            url = True
    if url is True:
        print("url not found")
    
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more information visit: {news_url}")
        speak("for more information visit this url")

        speak("[press 1 to continue] and [press 0 to stop]")
        num = input("[press 1 to continue] and [press 0 to stop]: ")

        if str(num) == "1":
            pass
        elif str(num) == "0":
            break

        speak("Thats all")
                