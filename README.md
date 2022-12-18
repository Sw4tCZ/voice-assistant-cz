# voice-assistant-cz

HLASOVÝ ASISTENT 

Pro funkční program v Pythonu je potřeba:
                                          1. Stáhnout hlas ve Windows - Nastavení/Datum a čas/Řeč/Hlasy/MicrosoftJakub (nutné zde nainstalovat jazykovou sadu - Čeština - Microsoft Jakub)
                                          2. Pokud hlas nebude funkční, a jazyková sada se nainstalovala do registru jiné složky, je nutné zapnout ve složce Register příslušný soubor registru a dále se automaticky příslušný registr zaktualizuje
                                          3. Nutně do Pythonu (3.11) stáhnout příslušné moduly: 
                                                          
                                                          3.1 Speech Recognization - pip install SpeechRecognition        (Knihovna pro provádění rozpoznávání řeči s podporou rozhraní API, online i offline.)
                                                          3.2 GoogleTrans - pip install googletrans                       (Bezplatná knihovna pythonu, která implementovala rozhraní Google Translate API. Ale, jelikož funguje na principu API, tak je nutné mít připojení k internetu.)
                                                          3.3 PYTTSX3 - pip install pyttsx3                               (Knihovna pro převod textu na řeč v Pythonu. Funguje i offline)
                                                          3.4 PYAUDIO - pip install PyAudio                               (Poskytuje audio knihovnu pro přehrávání hlasu)
                                                          3.5 PIPWIN - pip install pipwin                                 (Nástroj pro pip)
                                                          (pokud bude házet pyaudio chybu, tak je nutné do pipwinu nahrát pyaudio! - pipwin install pyaudio)
                                                          
                                                          
                                                
                                                          
                                        
