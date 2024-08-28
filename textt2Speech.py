import pyttsx3

data=input("Enter Text : \n")

engine=pyttsx3.init()
engine.say(data)
engine.runAndWait()