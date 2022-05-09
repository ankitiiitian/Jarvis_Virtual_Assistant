import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
import random


engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning Sir");
    
    elif(hour==12):
        speak("Good Noon Sir");
    
    elif(hour>12 and hour<16):
        speak("Good Afternoon Sir");
    
    elif(hour>=16 and hour<21):
        speak("Good Evening Sir");
    
    elif(hour>=21 and hour<=23):
        speak("Good Night Sir");

    speak("Hello Sir, I am Your Virtual Assistant, named Sikha.Would you like to take help from me.");

def sendEmail(to, content):
    server  = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('majorankits136@gmail.com','@majorankit2')
    server.sendmail('majorankits136@gmail.com',to,content)
    server.close()



def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Sikha's Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing your words.....")
        speak('Recognizing your words')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry, Say that again please.....")
        speak('Sorry, Say that again please')
        return "None"
    
    return query

if __name__ == "__main__":
    #speak("Ankit Kumar is an IIITian, He is Study From Indian Institute of Information Technology Guwahati");
    wishMe()
    f=0 
    while f!=1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            speak('Searching Youtube......')
            webbrowser.open("youtube.com",1)
    
        elif 'open google' in query:
            speak("Searching Google......")
            webbrowser.open("google.com",1)
    
        elif 'open facebook' in query:
            speak("Searching Facebook.....")
            webbrowser.open("facebook.com",1)
    
        elif 'open geeks for geeks' in query:
            webbrowser.open('geeksforgeeks.com',1)
    
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com",1)
    
        elif 'who made you' and 'tumhe kisne banaya hai' in query:
            speak("I made by Sir Ankit Kumar,who is currently study Bachelor of technology from Indian Institute of Information Technology Guwahati")
    
        elif 'music' in query:
            music_dir = 'C:\\Users\\HP\\Music\\Playlists'
            songs = os.listdir(music_dir)
            n = random.randint(0,23)
            os.startfile(os.path.join(music_dir,songs[n]))
    
        elif 'next song' in query:
            music_dir = 'C:\\Users\\HP\\Music\\Playlists'
            songs = os.listdir(music_dir)
            n = random.randint(0,23)
            os.startfile(os.path.join(music_dir,songs[n]))
    
        elif "what's time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,At Now Time is {strTime}")
            print(strTime)
    
        elif 'weather' and 'mausam ka hal batao' in query:
            webbrowser.open("accuweather.com",1)
    
        elif 'email to ankit' in query:
            try:
                speak("What should I say??")
                content = takeCommand()
                to = "majorankits136@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully!!")
        
            except Exception as e:
                print(e)
                speak("Sorry Sir, I feel regret that I am not able to send your email")
    
        elif 'good bye' and 'nikal' in query:
            f=1
        
    speak("Thank you Sir! You have a nice day ahead!!")
    print('Sikha 1.0"Ak"')  


    