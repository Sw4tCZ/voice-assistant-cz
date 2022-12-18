
def time():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(time)
        print(time)

def date():
    date = int(datetime.datetime.now().day)
    now = (datetime.datetime.now())
    from month import months
    month = (months[now.month])
    #month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)

    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("Vítejte zpět")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 10:
        speak("Dobré ráno")
    elif hour >= 10 and hour <= 12:
        speak("Dobré dopoledne")
    elif hour == 12:
        speak("Dobré poledne")
    elif hour >= 12 and hour <= 18:
        speak("Dobré odpoledne")
    elif hour >= 18 and hour <= 24:
        speak("Dobrý večer")
    else:
        speak("Dobrou noc")

    speak("Jak vám mohu pomoci?")
