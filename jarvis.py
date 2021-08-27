import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import calendar
import WishList
from requests import get
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good morning sir.")

    elif 12 <= hour < 18:
        speak("Good afternoon sir.")

    elif 18 <= hour <= 20:
        speak("Good evening sir.")

    else:
        speak("Good night sir.")

    WishList.specialDay()

    speak("I am Zira your Personal Assistant. How may I help you?")


def takeCmd():
    """
    It take microphone from the user to give command to the jarvis and return string output.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)

        speak("I am sorry. Say that again please....")
        return "None"
    return query

def taskEse():
    pass

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCmd().lower()

        # logic to executing task based on query.
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipadd = requests.get('https://api.ipify.org').text
                # print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir, I am not sure, but I think we are in {city} city of {state} and the country is {country}")
            except Exception as e:
                speak("Sorry sir, due to network issue I am not able to find where we are.")
                pass

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            speak("Opening notepad fou you")

        elif "open command prompt" in query:
            os.system("start cmd")
            speak("opening command prompt for you")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening youtube")

        elif "play online music" in query:
            text = "Sir, Which song you want to listen"
            speak(text)
            scm = takeCmd().lower()
            kit.playonyt(scm)

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            ipAd = f"Your IP address is {ip}"
            speak(ipAd)

        elif "open google" in query:
            googlePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"
            speak("Sir, What should i search on google")
            cm = takeCmd().lower()
            webbrowser.open(cm)
            speak("Opening google")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")
            speak("Opening instagram")

        elif "play music" in query:
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            musicNumber = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[musicNumber]))
            speak("playing music" + songs[musicNumber])

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif "the date" in query:
            strDate = datetime.date.today()
            speak(f"Sir, The date is {strDate}")

        elif "the day" in query:
            def findDay():
                day = datetime.date.today().weekday()
                return calendar.day_name[day]


            date = datetime.date.today()
            weekDay = findDay()
            print(f"{weekDay} Sir")
            speak(f"{weekDay} Sir")

        elif "open code" in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening VS Code")

        elif "open pycharm" in query:
            pathOfCode = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe"
            os.startfile(pathOfCode)
            speak("Opening PyCharm")

        elif "open intell jdea" in query:
            intelljpath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.1.1\\bin\\idea64.exe"
            os.startfile(intelljpath)
            speak("Opening Intell JDEA")

        elif "open studio" in query:
            obsPath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obsPath)
            speak("Opening OBS Studio")

        elif "show me photo" in query:
            photoPath = "C:\\Users\\hp\\OneDrive\\Pictures\\pic"
            photo = os.listdir(photoPath)
            pic = random.randint(0, len(photo))
            os.startfile(os.path.join(photoPath, photo[pic]))
            speak("Opening photo")

        elif "what is my date of birth" in query:
            speak("Sir your date of birth is 26 June")

        elif "when you launch" in query:
            speak("17 March 2021")

        elif "no thanks" in query:
            speak("Thanks for using me sir have a nice day.")
            sys.exit()

        speak("Sir, do you have any other work for me.....")
