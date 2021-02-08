import pyttsx3
import speech_recognition as sr
import sys


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            print("\nRecognizing...\n")
            said = r.recognize_google(audio)
            print(f"Me : {said}")

        except Exception as e:
            print("Didn't hear properly :(")
    return said


print("\n")
print("############################################################")
print("#    Code For       : My Girlfriend                        #")
print("#    Code Language  : Python                               #")
print("#    Code Author    : Md. Tareq Ahamed Jony                #")
print("############################################################")
print("\n")

print("Listening...")
while True:
    user_input = get_audio()
    # user_input = user_input.lower()
    if user_input == "stop":
        print("Quiting!!!")
        speak("Quitting. Farewell")
        sys.exit()
    elif "hello" in user_input:
        txt = "Hi!Tareq. How are you?"
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "I am fine and you" in user_input:
        txt = "I'm fine too."
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "hey I have something to tell you" in user_input:
        txt = "Go on."
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "do you remember the day when we first met" in user_input:
        txt = "Yes. You were just staring at me"
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "yes because you stole my heart" in user_input:
        txt = "What's the matter? Are you okay?"
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "yes I am ok" in user_input:
        txt = "Than, tell me what do you want to tell me"
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "I just want to tell you that I love you" in user_input:
        txt = "What?? Are you serious?"
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "yes I am" in user_input:
        txt = "Babe, I love you too."
        print(f"Tanya7 : {txt}")
        speak(txt)
    elif "will you marry me" in user_input:
        txt = "Sure. I would love too."
        print(f"Tanya7 : {txt}")
        speak(txt)
        speak("This was our story. What's yours?")
    else:
        speak("Didn't here properly :(")


