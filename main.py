import speech_recognition as sr
import subprocess
from datetime import datetime,date
import time

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

print("welcome back")
text = "hello, i am espeak bot"
subprocess.run(['espeak',text])
while True:
    with mic as source:
        audio = r.listen(source, timeout=2, phrase_time_limit=6)
       
        try:
            words = r.recognize_google(audio)
           
            if words.lower() == "goodbye":
                subprocess.run(['espeak',"goodbye shutting the system now."])
                break
               
            if words.lower() == "what time is it":
                print(datetime.now().strftime('%Y %m %d %H:%M'))
                subprocess.run(['espeak',datetime.now().strftime('%Y %m %d %H:%M')])
           
            print(words)
               
        except sr.exceptions.UnknownValueError as e:
            print(e)
        except sr.exceptions.RequestError as e:
            print(e)
        except sr.exceptions.WaitTimeoutError as e:
            print(e)
           