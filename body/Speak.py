import pyttsx3

engine = pyttsx3.init("sapi5") # vymezení modulu a hlasu přes windows
voices = engine.getProperty('voices')
cs_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_csCZ_Jakub"
engine.setProperty('voice', cs_voice_id)
voicespeed = 180
engine.setProperty('rate', voicespeed)

#definování funkce speak

def speak(audio):
        engine.say(audio)
        engine.runAndWait()





