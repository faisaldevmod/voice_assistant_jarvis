import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from pynput.keyboard import Key, Controller
import time
from requests import get

engine = pyttsx3.init('sapi5')
# voices= engine.getProperty('voices') #getting details of current voice
# engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.today().hour)
    speak("hello sir")
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Please tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        r.energy_threshold = 800
        audio = r.listen(source)
        
    try:     
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("try again");
        return "None"
    return query

def my_asistant():
    engine1 = pyttsx3.init()
    # print(voices[1].id)
    speak("Give me command")
    query=takeCommand().lower();
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(1)
    keyboard.type(query)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    return 0;

if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower() #Converting user query into lower case
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'call windows assistant' in query or 'call my assistant' in query or 'call windows' in query or 'call the assistant' in query or 'call my windows assistant' in query:
            speak("ok.. i am calling your windows assistant")
            my_asistant()

        elif 'open the code' in query or 'open code' in query or 'open visual studio' in query or 'open visual studio Code' in query:
            os.startfile("C:\\Users\\mubasheer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak("ok.. i am opening the Visual Studio Code")
        
        elif 'close the code' in query or 'close code' in query or 'close visual studio' in query or 'close visual studio Code' in query :
            os.system("TASKKILL /F /IM code.exe")
            speak("ok.. i am closing the Visual Studio Code")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak("ok.. i am opening the google chrome")
        
        elif 'close the chrome' in query or 'close chrome' in query or 'close google chrome' in query :
            os.system("TASKKILL /F /IM chrome.exe")
            speak("ok.. i am closing the google chrome")

        elif 'open youtube' in query:
            speak("ok.. i am opening the youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query or 'google' in query:
            speak("Sir, What should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            speak("ok.. i am opening the stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play song' in query or 'play music' in query:
            speak("ok.. i am playing music")
            music_dir = 'C:\\Users\\mubasheer\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))

        # elif 'play song on youtube' in query:
        #     kit.playonyt("see you again")

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mubaseer, the time is {strTime}")

        elif 'open command prompt' in query:
            speak("ok.. i am opening command prompt")
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(f"your IP address is {ip}")

        elif 'stop' in query or 'stop buddy' in query or 'stop buddy' in query:
            speak("good bye sir...... i will see you again ")
            break