import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import wolframalpha
import pyjokes as pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zuno. Please tell me how may I help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        print("Stop.")

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def process_text(query):
    try:
        if "who are you" in query or "define yourself" in query:
            results = '''Hello, I am Zuno. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            speak(results)
            return

        elif "who made you" in query or "created you" in query:
            results = "I have been created by Team 7."
            speak(results)
            return

        elif "calculate" in query:

            app_id = "8822UV-3YH253JEGJ"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

    except Exception:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def open_application(query):
    if "age" in query:
        speak("Microsoft Edge")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        return

    elif "android studio" in query:
        speak("Opening android studio")
        os.startfile("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")
        return

    elif "vlc" in query:
        speak("Opening VLC media player")
        os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
        return

    elif "pycharm" in query:
        speak("Opening PyCharm")
        os.startfile("C:\\Program Files\\etBrains\\PyCharm\\bin\\pycharm64.exe")
        return


if __name__ == "__main__":
    wishMe()

    # while True:
    if 1:
        query = takeCommand().lower()

        # Logic for  executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\mange\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))  # random module

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'search' in query or 'play' in query:

            query = query.replace("search", ",")
            query = query.replace("play", ",")
            webbrowser.open(query)

        process_text(query)
        open_application(query)
