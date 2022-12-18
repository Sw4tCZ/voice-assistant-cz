import speech_recognition as sr
from googletrans import Translator

#definování funkce poslechu

def Listen():
    r = sr.Recognizer()


    with sr.Microphone() as source:
            print("Poslouchám...")
            r.pause_threshold = 1
            audio = r.listen(source,0,8)
    #zdroj - mikrofon
    try:
            print("Přemýšlím...")
            query = r.recognize_google(audio,language="cs")
    #odpoveď asistenta
    except:
            return ""

    query = str(query).lower()
    return query

#vymezení funkce překladu

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


