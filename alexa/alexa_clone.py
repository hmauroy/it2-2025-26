import speech_recognition as sr
import pyttsx3
from vitser import Vitser
from random import randint

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
teller = 0
for voice in voices:
    #print(voice)
    if "nb" in voice.languages[0]:
        print(f"Voice {voice.languages} ved index {teller}")
        print("----------------------")
    teller += 1
#engine.setProperty("voice", voices[60].id) # Henrik-google-stemmen nr 60
engine.setProperty("voice", voices[99].id) # Nora-google-stemmen, nr 84
#engine.setProperty("voice", voices[85].id) # Nora enhanced, nr 85
rate = 190
engine.setProperty('rate', rate)

vitser = Vitser()



def writeFile(filename,text):
    with open(filename, 'w') as f:
        f.write(text)

def writeToSpeechLog(text):
    with open("speech_log.txt", 'a') as f:
        f.write(text)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                #command = listener.recognize_google(voice,language="no")
                command = listener.recognize_google(voice,language="no")
                return command
            except sr.UnknownValueError:
                talk("Beklager, det forstod jeg ikke")
                print("Google Speech Recognition could not understand audio")
                return ""
            except sr.RequestError as e:
                talk("Server er opptatt")
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return ""
    except Exception as err:
        print("Noe gikk galt.")
        pass

def talkBack(command):
    if ("har" in command and "du" in command and "bra") or ("hvordan går" in command and "med deg" in command):
        talk("Takk, det går bra med meg. Hva med deg?")
        command = take_command()
        command = command.lower()
        if "jeg" in command and "har" in command and "det" in command and "bra" in command:
            talk("Så godt å høre")
    elif "fortell en vits" in command or "fortelle en vits" in command:
        vits()
    elif "hvordan" in command and "været" in command:
        talk("Hvis du vil vite noe om været kan du sjekke yr. dot n o")
        talk("Eller du kan sjekke ikke-plag-assistenten-din-med-dette. dot com")
    elif "hils" in command and "it 2" in command:
        talk("Halla ite to! Velkommen til timen.")
        talk("smiley blunker")
    elif "du" in command and "er" in command and "morsom" in command:
        talk("takk skal du ha!")
        talk("her kommer en vits til")
        vits()
    elif "stopp lytting" in command or ("alexa" in command and "avslutt" in command):
            global listening
            listening = False
            talk("Avslutter, ha det bra!")
            print("Avslutter")
    elif "repeter etter meg" in command:
        diktat()
    else:
        talk("Det kan jeg ikke hjelpe deg med!")

def vits():
    v = vitser.getVits()
    print(v)
    talk(v)
    if randint(0,6) == 1:
        talk("haha")
    elif randint(0,6) == 2:
        talk("knegg knegg")
    elif randint(0,6) == 3:
        talk("hi. hi.") 

def diktat():
    talk("jeg er klar for diktat.")
    command = input("Skriv inn setning: ")
    command = command.lower()
    talk(command)
    #talk("Håper det var riktig!")

    

listening = True
def run_alexa():
    talk("Hei jeg er den norske og dårlige alexa klonen")
    while listening:
        talk("Hva kan jeg hjelpe deg med?")
        command = take_command()
        command = command.lower()
        print(command)
        writeToSpeechLog(command)
        talkBack(command)   

if __name__ == "__main__":
    run_alexa()
    talk("Hei, jeg er din personlige pappa vits forteller! Hør her!")
    #for i in range(10):
    #    vits()