import datetime
import playsound
from jarvis import speak


def specialDay():
    if datetime.date(2021, 6, 26) == datetime.date.today():
        playsound.playsound("BirthdaySong.mp3")
        # webbrowser.open("https://music.youtube.com/watch?v=pk21s6tUjGY&list=RDAMVMpk21s6tUjGY")

    elif datetime.date(2021, 3, 29) == datetime.date.today():
        speak("Happy Holli sir.")

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

    elif datetime.date(2021, 6, 6) == datetime.date.today():
        speak("Hello Sir this date is same as today's date.")
