import pyttsx3 #importing the libraries

name = input("Enter your name : ") #input for user's name

engine = pyttsx3.init() #creating object
engine.setProperty('rate',110) #setting rate of speaking

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #voice 0 - male , 1 - female

engine.say(f"Hello {name} , Welcome to the world of Python.") #text-to-speech
engine.runAndWait() #program keeps running till speech is completed


