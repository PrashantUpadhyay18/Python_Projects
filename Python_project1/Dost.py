import pyttsx3 #use for voices
import datetime # use for date and time
import speech_recognition as sr  #for converting our speech into written text
import wikipedia #for excessing wikipedia stuffs
import webbrowser #for excessing webbrower site ex youtube, geeeks for geeks etc

#sapi5 used for voices
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

#System Speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wishing Function in starting
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12 and hour>=0:
        speak("A very happy Good morning sir !")
    elif hour>=12 and hour<18:
        speak("A very happy good after noon !")
    else:
        speak("Good evening !")

    speak("Hello i am alpha,a AI model created by Prashant Upadhyay. How can i help you sir")

#below function will take your speech and return a written text of your speech
def takeCommand():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("listening...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query} \n" )

    except Exception as e:
        print("Please repeat \n")
        return 'None'
    return query

#Main Function
if __name__ == "__main__":
    wishMe()
    temp=True
    while temp:
        query=takeCommand().lower()

        #logic for executing task based upon querry
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'open geeks for geeks' in query:
            webbrowser.open('https://www.geeksforgeeks.org/')
        elif 'open google'  in query:
            webbrowser.open('google.com') 
        elif 'alpha go' in query:
            speak("Thanks for using me")
            temp=False