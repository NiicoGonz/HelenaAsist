import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='es-spanish')
            command = command.lower()
            if 'burbuja' in command:
                command = command.replace('burbuja', '')
                print(command)
    except:
        pass
    return command


def run_Pluto():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('reproduciendo' + song)
        pywhatkit.playonyt(song)
    elif 'dime la hora' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('La hora es  ' + time)
    elif 'busca en wikipedia' in command:
        person = command.replace('busca en wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'fecha' in command:
        talk('Lo siento tengo mala memoria')
    elif 'estás soltera' in command:
        talk('Tengo una relación con el wifi G2T1SM')
    elif 'broma' in command:
        talk(pyjokes.get_joke('es'))
    else:
        talk('por favor repita el comando nuevamente.')


while True:
    run_Pluto()
