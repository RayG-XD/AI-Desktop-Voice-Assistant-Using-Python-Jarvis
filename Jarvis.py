import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Roger")       
    #songs_dir = "C:\giaan"
    speak("Your personal AI assistant. Please tell me how can i help you?")
    #songs = os.listdir(songs_dir)
    #os.startfile(os.path.join(songs_dir, songs[0]))

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def main():
    wishMe()
    my_chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "wikipedia")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url = "youtube.com"
            # url = "https://www.youtube.com/"
            speak('Opening youtube...')
            chrome_path =my_chrome_path
            webbrowser.open(url)


        elif 'open google' in query:
            url = "google.com"
            speak('Opening google...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        #elif 'open instagram' in query:
         #   url = "instagram.com"
          #  speak('Opening instagram login page...')
           # chrome_path =my_chrome_path
            #webbrowser.open(url)


        elif 'open whatsapp' in query:
            url = "whatsapp.com"
            speak('Opening whatsapp login page...')
            chrome_path =my_chrome_path
            
            webbrowser.open(url)

        elif 'something about you in a song' in query:
            songs_dir = "C:\\giaan"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
            

        elif 'open github' in query:
            url = "github.com"
            speak('Opening github...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open facebook' in query:
            url = "facebook.com"
            speak('Opening facebook...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open weather' in query:
            url = "accuweather.com"
            speak('Opening accuweather...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open mathematics' in query:
            url = "https://meet.google.com/zjr-bjha-xrk"
            speak('Opening EM3 lecture on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open data structure' in query:
            url = "https://meet.google.com/cfb-rbbb-qhv"
            speak('Opening DS lecture on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open graph theory' in query:
            url = "https://meet.google.com/lookup/h6t5eqvlpc"
            speak('Opening DSGT lecture on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)   

        elif 'open computer architecture' in query:
            url = "https://meet.google.com/ctf-tfrp-yix/"
            speak('Opening DLCA lecture on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open computer graphics monday' in query:
            url = "https://meet.google.com/kho-cnxe-qex"
            speak('Opening CG monday link on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open computer graphics tuesday' in query:
            url = "https://meet.google.com/mqo-kpin-vmm"
            speak('Opening CG tuesday link on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open computer graphics thursday' in query:
            url = "https://meet.google.com/sgv-rkpp-tdv"
            speak('Opening CG thursday link on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open computer graphics friday' in query:
            url = "https://meet.google.com/ajk-cwtc-svv"
            speak('Opening CG friday link on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'open object oriented programming' in query:
            url = "https://meet.google.com/eyb-yuet-muy"
            speak('Opening OOP lecture on google meet...')
            chrome_path =my_chrome_path
            webbrowser.open(url)

        elif 'play music' in query:
            songs_dir = "C:\\music for jarvis"
            speak('Opening music...')
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine sir, thank you for asking!")   

        elif 'can you do' in query:
            speak("I can help you open various websites, apps and answer your search queries. I can even play some music for you")

        elif 'can you drive a car' in query:
            speak("I am not sure, but if you teach me, I might learn to drive as well")

        elif 'tell me a joke' in query:
            speak("okay, Have you heard about that new restaurant called karma, , , There is no menu: you get what you deserve... hehehehe")
            print("Have you heard about that new restaurant called karma, , , There is no menu: you get what you deserve")

        elif 'stop' or 'break' in query:
            speak("Roger shutting down")
            break

if __name__ == "_main_":
    main()