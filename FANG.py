import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
webbrowser.register('chrome',
	                 None,
	                 webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
import wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning! saakeath");print("Good Morining saketh!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon! saakeath");print("Good Afternoon saketh!")
    elif hour>=17 and hour<20:
        speak("Good Evening! saakeath");print("Good Evening saketh!")
    elif hour<=23 and hour<4:
        speak("Good Night saakeath");print("Good Night Saketh!")
        speak("Don't mind ")
        speak("why are you still awake saakeath!");print("Dont Mind!\tWhy are you still awake saketh?")
        speak("go and have some sleep we can do work tomorrow");print('Go and have some sleep,we can do work tomorrow!')
    speak("It's me fangg !");print("FANG HERE!")
    speak("how can i help you!");print("How can i help you?")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        text= takecommand().lower()

        if 'open youtube' in text:
            speak("opening youtube")
            webbrowser.get('chrome').open("youtube.com")

        elif 'open'+' '+'in google' in text:
            command = text.split()
            code = command[1]
            speak("opening"+code)
            webbrowser.get("chrome").open(code+'.com')

        elif 'open google' in text:
            speak("opening google")
            webbrowser.get('chrome').open("google.com")

        elif 'open github' in text:
            speak("opening github")
            webbrowser.get('chrome').open('github.com')

        elif 'open udemy' in text:
            speak("opening udemy")
            webbrowser.get('chrome').open("udemy.com")

        elif 'what is ' in text:
            query = text.replace(' what is ', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia");print("According to Wikipedia")
            print(result)
            speak(result)

        elif 'play music' in text:
            print("Playing One of your Favourite Song\n")
            speak("Playing One of your Favourite Song")
            path = r"E:\Songs"
            songs = os.listdir(path)
            os.startfile(os.path.join(path, songs[random.randint(0, len(songs))]))

        elif 'time' in text:
            print("Currrent Time is\n")
            speak("Current Time is")
            timestr = datetime.datetime.now().strftime("%H:%M:%S")
            print(timestr)
            speak(timestr)

        elif 'open code'+' ' in text:
            command=text.split()
            code=command[-1]
            lst=['waste','heart']
            if code in lst:
                codepath = ("C:\\Users\\saketh\\PycharmProjects\\untitled\\" + code + ".py")
                speak("opening code")
                os.startfile(codepath)
            else:
                speak("sorry cant find your code! check the name again");print("Sorry! can't find your code!\ncheck the code name again")

        elif 'date' in text:
            print("Todays Date is\n")
            speak("Todays Date is")
            timestr = datetime.datetime.now().date()
            print(timestr)
            speak(timestr)

        elif 'yourself' in text:
            print("I'm FANG ! I Am Your Personal Desktop Assistant\n");speak("im fang And I Am Your Personal Desktop Assistant")
            print("I Can Do The Following Things For You\n");speak("I Can Do The Following Things For You")
            print("I Can Open Any Website for you in google");speak("I Can Open Any Website For You")
            print("I Can Search Anything Over Internet For You in wikipedia");speak("I Can Search Anything Over Internet For You")
            print("I Can Tell Your Plans For The Week");speak("I Can Tell You About Your Plans For The Week")
            #print("I Can Push Your Repositries To Your Github");speak("I Can Push Your Repositries To Your Github")
            print("I Can Play Your Favourite Music");speak("I Can Play Your Favourite Music")
            print("I Can Set Reminders For You");speak("I Can Set Reminders For You")
            print("I Also Care For You, So I Will Remind You To Drink Water After Every 45 Minutes");speak("I Also Care For You, So I Will Remind You To Drink Water After Every 45 Minutes")

        #elif 'plans' in text:
            #for pn in f:
                #print(pn)
                #speak(pn)
        elif 'remind' in text:
            with open("reminder.txt", "a") as fh:
                text.replace("remind", "")
                try:
                    text.replace("jojo", "")
                except:
                    pass
                fh.write(f"{text}\n")
            print("Okay Sir I Will Remind You")
            speak("Okay Sir I Will Remind You")
