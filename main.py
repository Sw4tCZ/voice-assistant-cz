import os
import speech_recognition as sr
from googletrans import Translator
import pyttsx3
from time import sleep
import webbrowser
from funkce import date
from funkce import time
from funkce import wishme


#definování hlasu

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
cs_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_csCZ_Jakub"
engine.setProperty('voice', cs_voice_id)
voicespeed = 180
engine.setProperty('rate', voicespeed)


#definování funkcí speak a listen

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Listen():
    r = sr.Recognizer()


    with sr.Microphone() as source:
            print("Poslouchám...")
            r.pause_threshold = 1
            audio = r.listen(source,0,8)

    try:
            print("Přemýšlím...")
            query = r.recognize_google(audio,language="cs")

    except:
            return ""

    query = str(query).lower()
    return query


#definování překladu


def TranslationCsToEng(text):
        line = str(text)
        translate = Translator()
        result = translate.translate(line)
        data = result.text
        print(f"You : {data}")
        return data


def MicExecution():
        query = Listen()
        data = TranslationCsToEng(query)
        return data


#Základní část a výstup příkazů

if __name__ == "__main__":

    wishme()

    while True:
        query = MicExecution().lower()  # převezme příkaz
        print(query)

        if "time" in query:  # čas
            time()           
        elif "datum" in query:  # datum
            date()
        elif "log out" in query:          # odhlášení systému
            speak("Odhlásím za pět vteřin")
            sleep(5)
            os.system("shutdown - l")

        elif "restart" in query:          # restart systému
            speak("Restartuji za pět vteřin")
            sleep(5)
            os.system("shutdown /r /t 1")

        elif "turn off" in query:         # vypnutí systému
            speak("Vypínám za pět vteřin")
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "open the internet" in query:        # otevření prohlížeče na Google
            speak("Otevírám internet")
            webbrowser.open_new("https://www.google.com/")

        elif "offline" in query:  # quit to end the program       # vypnutí hlasového asistenta
            speak("Vypínám se, když budete něco potřebovat, ozvěte se!")
            quit()
