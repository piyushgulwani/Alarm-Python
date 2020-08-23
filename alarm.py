import pyttsx3 , time 
from datetime import datetime

def speak(audio):
    print(audio)
    engine = pyttsx3.init('sapi5')
    engine.say(audio)
    engine.runAndWait()
    
speak("Welcome to our alarm")
name = input("Enter your name:  ") 
input_time = input("Enter in 24 hour Format")
while True : 
    i = f"Wake up {name}"
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == input_time :
        for x in range(0,12):
            speak(i)
        break