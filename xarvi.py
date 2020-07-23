import pyttsx3
import wikipedia
import webbrowser
import os
import random
import speech_recognition as sr
import datetime


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am xarvis sir. please tell me how may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say tha again please...")
        return "None"
    return(query)
if __name__ == '__main__':
    wishme()
    #while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open greeks for greeks' in query:
            webbrowser.open("greeks for greeks.com")

        elif 'play music' in query:
            music_dir ='C:\\NEW FOLDERBHO'
            songs=os.listdir(music_dir)
            print(songs)
            j=random.randint(0,len(songs))

            os.startfile(os.path.join(music_dir,songs[j]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\ASUS\\Downloads"
            os.startfile(codePath)

        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'jarvis quit' in query:
            speak("thanks you sir!")
            exit()
