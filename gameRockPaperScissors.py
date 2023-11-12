import pyttsx3
import speech_recognition as sr
import random

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
        r.energy_threshold = 300
        # r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source,0,4)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"Say that again")
        return "None"
    return query


def gameplay():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    speak("Lets Play....")
    i = 0
    me_score = 0
    com_score = 0
    while(i < 4):
        choose = ("rock","paper","scissors")
        com_choose = random.choice(choose)
        speak("choose any one [rock], [paper], [scissors]")
        query = takeCommand().lower()
        if (query == "rock"):
            if(com_choose == "rock"):
                speak("rock")
                speak("you two are choosing same")
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            elif(com_choose == "paper"):
                speak("paper")
                com_score += 1
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            else:
                speak("scissor")
                me_score += 1
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")

            i = i + 1

        elif (query == "paper"):
            if(com_choose == "rock"):
                speak("rock")
                me_score += 1
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            elif(com_choose == "paper"):
                speak("paper")
                speak("you two are choosing same")
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            else:
                speak("scissor")
                com_score += 1
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            i = i + 1

        elif (query == "scissors"  or query == "scissor" or query == "scizzor"):
            if(com_choose == "rock"):
                speak("rock")
                com_score += 1
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            elif(com_choose == "paper"):
                speak("paper")
                me_score += 1
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            else:
                speak("scissor")
                speak("you two are choosing same")
                print(f"score:- Me :- {com_score} : You :- {me_score}")
                speak(f"score,:- Me :- {com_score} : You :- {me_score}")
            i = i + 1


