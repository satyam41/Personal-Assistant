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
# print(voices[1])
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good morning sir.")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir.")
    
    elif hour>=18 and hour<=20:
        speak("Good evening sir.")

    else:
        speak("Good night sir.")

    speak("I am your Personal Assistant. How may I help you?")
    if datetime.date(2021,6,26) == datetime.date.today():
        speak("Happy Birthday sir")
    
    elif datetime.date(2021,3,29) == datetime.date.today():
        speak("Happy Holy sir.")
    
    elif datetime.date(2021,8,15) == datetime.date.today():
        speak("Happy Independence Day sir")

    elif datetime.date(2021,10,15) == datetime.date.today():
        speak("Happy Dussehra sir")
    
    elif datetime.date(2021,11,4) == datetime.date.today():
        speak("Happy Diwali sir")
    
    elif datetime.date(2021,11,10) == datetime.date.today():
        speak("Happy Chhat puja sir.")
    
    elif datetime.date(2022,1,26) == datetime.date.today():
        speak("Happy Republic day sir")
    # speak("My name is Jayanti Hari")

def takeCmd():
    ''' 
    It take microphone from the user to give command to the jarvis and return string output.    
    '''
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
            query = query.replace("wikipidia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube")

        elif "play ram siya ram" in query:
            webbrowser.open("https://music.youtube.com/watch?v=iqpUko_ceN0&list=RDAMVMiqpUko_ceN0")
            speak("ram siya ram by Sachet Tandon, Sure. Playing on YouTube Music")
        
        elif "play friend" in query:
            webbrowser.open("https://music.youtube.com/watch?v=X-x7eZOdBFM&list=RDAMVMX-x7eZOdBFM")
            speak("FRIENDS by Anne-Marie,Sure. Playing on youtube music")
        
        elif "play online music" in query:
            webbrowser.open("music.youtube.com")
            speak("playing some music on YouTube music")
        
        elif "play dil chahte ho" in query:
            webbrowser.open("https://music.youtube.com/watch?v=0ApQaG8wNsU&list=RDAMVM0ApQaG8wNsU")
            speak("dil chahte to by Jubin Nauyiyal and Payal Dev, Sure. Playing on youtube music.")

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
            musicNumber = random.randint(0,len(songs))    
            os.startfile(os.path.join(music_dir, songs[musicNumber]))
            speak("playing music")
        
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

        elif "open studio" in query:
            obsPath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obsPath)
            speak("Opening OBS Studio")
        
        elif "show me photo" in query:
            photoPath = "C:\\Users\\hp\\OneDrive\\Pictures\\pic"
            photo = os.listdir(photoPath)
            pic = random.randint(0,len(photo))
            os.startfile(os.path.join(photoPath, photo[pic]))
            speak("Opening photo")

        elif "change your voice" in query:
            engine.setProperty('voice', voices[0].id)
            speak("Thank you for choose me for as your personal assistant. How may I help you?")
        
        elif "how are you" in query:
            speak("I am fine. thank you for asking me")
        
        elif "marry me" in query:
            speak("I am a robot so I can not marry with you.")
        
        elif "what is your name" in query:
            lst = ["My name is Zira.","you can know because you have developed me."]
            try:
                rand = random.randint(0,len(lst)-1)
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

        elif "hi" in query:
            speakList = ["Hi sir", "Namaste, how can I help?"]
        
        elif "tell me a joke" in query:
            listOfJoke = ["Why did the tomato blush?\nBecause it saw the salad dressing"]
            try:
                randomJokes = random.randint(0,len(listOfJoke)-1)
                print(listOfJoke[randomJokes])
                speak(listOfJoke[randomJokes])
            except:
                pass
        
        elif "one more" in query:
            speak("Here we go")
            joke = ["Why don't some couples go to the gym?\nBecause some relationship don't work out.", "What movie does the hopeless clock watch?\nKal Ho Naa Ho", "What do you call a rose that wants to go to moon?\nGulab ja Moon", "What do you call a dinosaur that cannot see?\nA Do-you-think-he-saurus.", "I love how in horror movie the person call out, 'Hello?'\nAs if the ghost will answer, 'Hey what's up, I am in the kitchen. Want a Sandwich.'"]
            try:
                randomJoke = random.randint(0,len(joke)-1)
                print(joke[randomJoke])
                speak(joke[randomJoke])
            except:
                pass

        elif "go to sleep" in query:
            speak("Ok Sir. I am wating for your next response.")
            break
