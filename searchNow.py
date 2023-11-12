import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
engine.setProperty('rate',160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("siri","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("siri","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


def searchWikipedia(query,num_sentences=2):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("siri","")

        # results = wikipedia.summary(query,sentence = 2)
        # speak("According to wikipedia...")
        # print(results)
        # speak(result)
        
                # Get the full Wikipedia content for the given query
        content = wikipedia.page(query).content
        
        # Split the content into sentences
        sentences = content.split('. ')
        
        # Take the first 'num_sentences' sentences to create a summary
        summary = '. '.join(sentences[:num_sentences])
        
        speak("According to Wikipedia...")
        print(summary)
        speak(summary)

        # searchWikipedia("Python programming language", num_sentences=2)


