import speech_recognition as sr
import os


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

        print("I am sorry. Say that again please....")
        return "None"
    query = query.lower()
    return query


while True:
    wakeUp = takeCmd()
    if "wake up" in wakeUp:
        os.startfile("E:\\Jarvis AI\\jarvis.py")
    else:
        print("Nothing")
