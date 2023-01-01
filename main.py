from body.Listen import *
from funkce import *
import os
from time import sleep
import webbrowser

if __name__ == "__main__":

    wishme()    # Pozdravení

    while True:
        query = MicExecution().lower()  # Příkazy
        print(query)

        if "time" in query:  # Čas
            time()
        elif "datum" in query:  # Datum
            date()
        elif "day" in query:    # Den
            day()
        elif "log out" in query:    # Odhlášení ze systému
            speak("Odhlásím za pět vteřin")
            sleep(5)
            os.system("shutdown /l")

        elif "restart" in query:    # Restart systému
            speak("Restartuji za pět vteřin")
            sleep(5)
            os.system("shutdown /r /t 1")

        elif "turn off" in query:   # Vypnutí systému
            speak("Vypínám za pět vteřin")
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "open the internet" in query:  # Otevření internetu
            speak("Otevírám internet")
            webbrowser.open_new("https://www.google.com/")

        elif "offline" in query:  # Vypnutí programu
            speak("Vypínám se, když budete něco potřebovat, ozvěte se!")
            quit()
