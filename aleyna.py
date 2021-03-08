from gtts import gTTS
import os
import speech_recognition as sr
from time import ctime
import time
import playsound
import pyautogui
import wikipedia
import random

def speak(audioString):
    print(audioString)
    num=0
    num += 1
    tts = gTTS(text=audioString, lang='en')
    file = str(num)+".mp3"
    tts.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "open code" in data:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)
        os.system('cd /home/tim/Dokumente/projects/Virtual_assistant')
        os.system('code .')

    elif "how are you" in data:
        speak("I am fine")

    elif "how was your day" in data:
        moods = "good", "okay", "not that bad", "acceptable"
        speak("it was " + random.choice(moods) + "thank you")
        
    elif "what time is it" in data:
        speak("it is" + ctime())

    elif "stop" in data:
        speak("Bye have a good day!")
        quit()

    elif "open terminal" in data:
        print("Opening Terminal")
        pyautogui.hotkey('ctrl', 't')

    elif "start zoom" in data:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.typewrite('zoom-client')
        pyautogui.press('enter')
        print("Starting Zoom-client")

    elif "start blender" in data:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)
        pyautogui.typewrite('blender')
        pyautogui.press('enter')

    elif "kill program" in data:
        pyautogui.hotkey('alt', 'f4')

    elif "discord" in data:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.typewrite("discord")
        pyautogui.press('enter')
        print("Starting Discord")

    elif "shut down" in data:
        print("Shutting down the pc...")
        speak("Goodbye Tim")
        os.system("poweroff")

    elif "reboot" in data:
        print("Rebooting the pc...")
        speak("I am rebooting now")        
        os.system("reboot")

    elif 'wikipedia' in data:
        speak('Searching Wikipedia')
        text =text.replace("wikipedia", "")
        results = wikipedia.summary(text, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

time.sleep(2)
speak("Hi Tim, my name is aleyna, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)



