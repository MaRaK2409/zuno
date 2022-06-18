# importing speech recognition package from google api
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations

num = 1


def speak(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:

        speak("Could not understand your audio, PLease try again !")
        return 0


# Driver Code
if __name__ == "__main__":
    speak("What's your name, Human?")
    name = 'Human'
    name = get_audio()
    speak("Hello, " + name + '.')

    while (1):

        speak("What can i do for you?")
        text = get_audio().lower()

        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            speak("Ok bye, " + name + '.')
            break

        # calling process text to process the query
        process_text(text)


def process_text(query):
    try:
        if 'search' in query or 'play' in query:
            # a basic web crawler using selenium
            search_web(query)
            return

        elif "who are you" in query or "define yourself" in query:
            speak = '''Hello, I am Person. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            speak(speak)
            return

        elif "who made you" in query or "created you" in query:
            speak = "I have been created by Sheetansh Kumar."
            speak(speak)
            return

        elif "geeksforgeeks" in query:  # just
            speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
            speak(speak)
            return

        elif "calculate" in query.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)
            return

        elif 'open' in query:

            # another function to open
            # different application available
            open_application(query.lower())
            return

        else:

            speak("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(query)
            else:
                return
    except:

        speak("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(query)


def search_web(query):

    driver = webdriver.Edge()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in query.lower():

        speak("Opening in youtube")
        indx = query.lower().split().index('youtube')
        query = query.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in query.lower():

        speak("Opening Wikipedia")
        indx = query.lower().split().index('wikipedia')
        query = query.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in query:

            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in query:

            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(query.split()))

        return


# function used to open application
# present inside the system.
def open_application(query):

    if "edge" in query:
        speak("Microsoft Edge")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        return

    elif "visual studio code" in query or "vs code" in query:
        speak("Opening visual studio code")
        os.startfile("C:\\Users\\mange\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        return

    elif "vlc" in query:
        speak("Opening VLC media player")
        os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
        return

    elif "pycharm" in query:
        speak("Opening PyCharm")
        os.startfile("C:\\Program Files\\etBrains\\PyCharm\\bin\\pycharm64.exe")
        return

    else:
        speak("Application not available")
        return

