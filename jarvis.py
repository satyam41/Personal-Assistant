import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
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

    if datetime.date(2021, 6, 26) == datetime.date.today():
        webbrowser.open("https://music.youtube.com/watch?v=pk21s6tUjGY&list=RDAMVMpk21s6tUjGY")

    elif datetime.date(2021, 3, 29) == datetime.date.today():
        speak("Happy Holy sir.")

    elif datetime.date(2021, 8, 15) == datetime.date.today():
        speak("Happy Independence Day sir")

    elif datetime.date(2021, 10, 15) == datetime.date.today():
        speak("Happy Dussehra sir")

    elif datetime.date(2021, 11, 4) == datetime.date.today():
        speak("Happy Diwali sir")

    elif datetime.date(2021, 11, 10) == datetime.date.today():
        speak("Happy Chhat puja sir.")

    elif datetime.date(2022, 1, 26) == datetime.date.today():
        speak("Happy Republic day sir")

    # elif datetime.date(2021, 6, 2) == datetime.date.today():
    #     webbrowser.open("https://music.youtube.com/watch?v=pk21s6tUjGY&list=RDAMVMpk21s6tUjGY")
    # speak("My name is Jayanti Hari")
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


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCmd().lower()

        # logic to executing task based on query.
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening youtube")

        elif "play ram siya ram" in query:
            webbrowser.open("https://music.youtube.com/watch?v=iqpUko_ceN0&list=RDAMVMiqpUko_ceN0")
            speak("ram siya ram by Sachet Tandon, Sure. Playing on YouTube Music")

        elif "play friend" in query:
            webbrowser.open("https://music.youtube.com/watch?v=X-x7eZOdBFM&list=RDAMVMX-x7eZOdBFM")
            speak("FRIENDS by Anne-Marie,Sure. Playing on youtube music")

        elif "play online music" in query:
            webbrowser.open("https://music.youtube.com/")
            speak("playing some music on YouTube music")

        elif "play 2002" in query:
            webbrowser.open("https://music.youtube.com/watch?v=ee2mcqcGL_c&list=RDAMVMee2mcqcGL_c")
            speak("2002 by Anne-Marie, Sure. Playing on youtube music.")

        elif "open google" in query:
            googlePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"
            os.startfile(googlePath)
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
            def findDay(date):
                day = datetime.date.today().weekday()
                return (calendar.day_name[day])


            date = datetime.date.today()
            weekDay = findDay(date)
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

        elif "change the voice" in query:
            engine.setProperty('voice', voices[0].id)
            speak("Thank you for choose me for as your personal assistant. i am David. How may I help you?")

        elif "change it again" in query:
            engine.setProperty('voice', voices[1].id)
            speak("Thank you for choose me for as your personal assistant. i am Zira. How may I help you?")

        elif "how are you" in query:
            speak("I am fine. thank you for asking me. how are you?")

        elif "marry me" in query:
            speak("I am a robot so I can not marry with you.")

        elif "what is your name" in query:
            lst = ["My name is Zira.", "you can know because you have developed me.", "My name is David."]
            try:
                rand = random.randint(0, len(lst) - 1)
                speak(lst[rand])
            except:
                pass

        elif "i am fine" in query:
            speak("Ok sir I wish for your good health.")

        elif "who developed you" in query:
            speak("You have develop me. Thank you for developing me as your personal assistant.")

        elif "what is my name" in query:
            speak("Your name is Satyam and you are my inventor.")

        elif "what is my date of birth" in query:
            speak("Sir your date of birth is 26 June")

        elif "when you launch" in query:
            speak("17 March 2021")

        elif "hello" in query:
            speakList = ["Hi sir", "Namaste, how can I help?", "Radhe-Krishna", "Sita-Ram", "Ram-Ram"]
            try:
                randomspeak = random.randint(0, len(speakList) - 1)
                speak(speakList[randomspeak])
            except:
                pass

        elif "thank you" in query:
            speak("Welcome sir its my pleasure.")

        elif "go to sleep" in query:
            speak("Ok Sir. I am waiting for your next response.")
            break
