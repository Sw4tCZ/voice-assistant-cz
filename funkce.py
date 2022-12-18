from body.Speak import *
import datetime

# Definování funkcí (čas, den, datum, pozdravení a oslovení)

def time():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(time)
        print(time)

def day():
    now = datetime.datetime.now()
    dny_v_tydnu = {0: "pondělí", 1: "úterý", 2: "středa", 3: "čtvrtek", 4: "pátek", 5: "sobota", 6: "neděle"}

    den = dny_v_tydnu[now.weekday()]
    speak("Dnes je: {}".format(den))

def date():
    date = int(datetime.datetime.now().day)
    now = (datetime.datetime.now())
    from month import months
    month = (months[now.month])
    year = int(datetime.datetime.now().year)

    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Vítejte zpět")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 9:
        speak("Dobré ráno")
    elif hour >= 9 and hour <= 11:
        speak("Dobré dopoledne")
    elif hour == 12:
        speak("Dobré poledne")
    elif hour >= 12 and hour <= 17:
        speak("Dobré odpoledne")
    elif hour >= 17 and hour <= 23:
        speak("Dobrý večer")
    else:
        speak("Dobrou noc")

    speak("Jak vám mohu pomoci?")