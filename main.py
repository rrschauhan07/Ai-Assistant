import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from dotenv import load_dotenv

recognizer = sr.Recognizer()
engine = pyttsx3.init()

load_dotenv()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(api_key= os.getenv('OPENAI_KEY'))

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named alex, skilled in general tasks like similar to assistants like Alexa and Gemini assistant and keep it short."},
        {"role": "user", "content": command}
    ]
    )

    return(completion.choices[0].message.content)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open stackoverflow" in c.lower():
        webbrowser.open("https://www.stackoverflow.com")    
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={os.getenv('NEWS_API')}")

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for i, article in enumerate(articles[:3]):
                speak(article["title"])
        
    else:
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Alex... ")
    while True:
        # Listening to the user
        r = sr.Recognizer()
        
        print("Recognizing...")

    # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == "alex"):
                speak("Yes")
                #Listen to command
                with sr.Microphone() as source:
                    print("Alex Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print("Error; {0}" .format(e))