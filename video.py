import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'yo' in command:
                command = command.replace('yo', '')
                print(command)
        
    except:
        pass

def take_command():
    print(command) 

def run_yo():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk ('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
