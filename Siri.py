import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import soupsieve
import requests
from bs4 import BeautifulSoup, SoupStrainer
import datetime
import pyautogui 
import os
from plyer import notification
from pygame import mixer
import speedtest

# passward logic

for i in range(3):
    a = input("Enter Passward to open jarvis:- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if(a == pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD UP")
        break
    elif(i == 2 and a != pw):
        exit()
    elif(a != pw):
        print("Try Agian")



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
engine.setProperty('rate',170)

# speak fnction
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# this function listen and after that recognize what you said 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source,0,4)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:

            # Fetch greetme function from GreetMe file
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir , You can call me anytime")
                    break

                # ######################## Siri: password change #######################################
                elif "change password" in query:
                    speak("what's the new password")
                    new_pw = input("Enter the new password:")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")

                ####################################################
                
                # You scheduled your tasks
            
                elif "schedule my day" in query:
                    tasks = [] # empty list
                    speak("Do you want to clear old tasks (plz type Yes or No)")
                    query = input("Enter [ Yes or No]:-")
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input( "Enter the tasks:- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                    elif "no" in query:
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input( "Enter the tasks:- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                # You can show you schedule also

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(  
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                # it will open your desktop search bar, type and open the application

                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("siri","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                 
                # You can take a screenshot 
                elif "screenshot" in query:
                    import pyautogui 
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                # You can click a photo 
                elif "click a photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile")
                    pyautogui.press("enter")

                # You can check your wifi internet speed
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576
                    download_net = wifi.download()/1048576
                    print("wifi upload speed", upload_net)
                    print("wifi download speed", download_net)
                    speak(f"wifi upload speed {upload_net}")
                    speak(f"wifi download speed {download_net}")

                elif "hello" in query:
                    speak("Hello sir, how are you ?")

                elif "your name" in query:
                    speak("my name: your voice assistant siri. My mission: To assist you. My favourite colour: Probably navy blue but it changes sometimes")

                elif "i am fine" in query:
                    speak("Good to hear, let me know if you need anything")

                elif "i am good" in query:
                    speak("that's great, sir")

                elif "your favourite car" in query:
                    speak("i'm the fan of self-driving car even though i's not a classic...yet!")

                elif "your favourite movie" in query:
                    speak("KGF is my favourite movie")

                elif "how are you" in query:
                    speak("i'm fine.You're very kind to ask, especially in these tempestuous times")

                elif "what about you" in query:
                    speak("Perfect sir")

                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                # Listen latest news also "business", "health", "entertainment", "technology"
                elif "news" in query:

                    # fetch latestNews function from newsRead file
                    from newsRead import latestNews
                    latestNews()
                
                # If you give command then it will sing your favorite song  (i gave only 4)
                elif "sing a song" in query:
                    speak("Playing your favorite songs, sir")
                    a = (1,2,3,4)
                    b  = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://youtu.be/H1YR5rsScC8?si=1R67Cr3yqTwgFwyW")
                    elif b ==2:
                        webbrowser.open("https://youtu.be/SxTYjptEzZs?si=KoX0TJVTcFfiK2oo")
                    elif b == 3:
                        webbrowser.open("https://youtu.be/WWXm39leYew?si=Hr2tzGwT6Ftp3UOK")
                    elif b == 4:
                        webbrowser.open("https://youtu.be/VuG7ge_8I2Y?si=ITJBdopyn3dDwX92")

                # Pause video which is running on your youtube
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")

                # If pause then Play video which is running on your youtube
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                
                # you can Mute
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                # You will also do volume up
                elif "volume up" in query:

                    # fetch the volumeup function from keyboard file
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()
                
                # You will also do volume down
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                
                # It can open your online webapp or your system app also
                elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)

                # It can close your online webapp or your system app also
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)
                
                # You can search something on google
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)

                # You can search something on Youtube
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                
                # You can search something on wikipedia and it will tell you 2 lines 
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query,num_sentences=2)

                # Show the current temperature
                elif "temperature" in query:
                    speak("Which place's temperature would you like to know?")
                    search = takeCommand().lower()
                    url = f"https://www.google.com/search?q=" + search 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data .find("div", class_ = "BNeawe").text
                    print(f"sir, current {search} is {temp}")
                    speak(f"sir, current {search} is {temp}")
                
                # Show the current weather
                elif "weather" in query:
                    speak("Which place's weather would you like to know?")
                    search = takeCommand().lower()
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    weather = data .find("div", class_ = "BNeawe").text
                    print(f"sir, current{search} is {weather}")
                    speak(f"sir, current{search} is {weather}")
                
                # Show the current time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    print(f"Sir, the time is {strTime}")
                    speak(f"Sir, the time is {strTime}")
                
                # if you say finally sleep then it will exit in this program
                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()

                # It remember what you have already said
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("siri","")
                    speak("you told me to" + rememberMessage)
                    remember = open("remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()

                # if you give this command then it will tell you what you told
                elif "do you remember" in query:
                    remember = open("remember.txt","r")
                    speak("you told me" + remember.read())

                # shutdown your system 
                elif "shutdown the system" in query:
                    speak("Are you sure sir you want to shutdown your system.(please speak yes or no)")
                    shutdown = takeCommand().lower()
                    # shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                # i add one of the poplar game is rock paper scissor you can enjoy
                elif "rock paper scissor game" in query or "rock paper scisor game" in query:
                    from gameRockPaperScissors import gameplay
                    gameplay()


