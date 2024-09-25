import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':
    sites = ['youtube','google','amazon','kaggle','hackerrank','bing','udemy','wikipedia']
    speak("assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if "close" in query:
            exit(0)
        elif "open" in query:
            site = query.split(" ")[1]
            if site in sites:
                webbrowser.open(f"{site}.com")

