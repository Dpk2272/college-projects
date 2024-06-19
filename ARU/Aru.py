from urllib import request
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib 
import pyautogui
from playsound import playsound
import time

engine=pyttsx3.init('sapi5')       #voice recognition and synthesis provided by Microsoft
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',175)

def speak(audio):        # this function will program to speak something by assisstant 
    engine.say(audio)
    engine.runAndWait()

    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        print('Hey good morning sir')
        speak('Hey good morning sir')
    elif hour>=12 and hour<=18 :
        print('Afternoon sir')
        speak('Afternoon sir')
    else:
        print('Good Night Sir')
        speak('Good Night Sir')
    print('Mai ARU Hu Sir.')
    print('How May I Help You..')    
    speak('Mai ARU Hu Sir. How may I help You...')

def takecommand():
    r=sr.Recognizer()      # a class used to recognise class
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=1  # seconds of non speaking audio before a phrase is considered complete 
        audio=r.listen(source)
    try:
        print('Recognizing')
        query=r.recognize_google(audio,language='en-in')
        print(f'You mean : {query}\n')
    except Exception as e:
        print('Did not Recognize please Say Again...!')
        speak('Did not Recognize please Say Again...!')
        return 'none'    
    return query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('garga8149@gmail.com', 'gmlznudxuqhvqdsj')
        server.sendmail ('arpitsaxenabtp@gmail.com', to, content)
        server.close()




if __name__ == '__main__':
    wishme()

    query = takecommand().lower()

    if 'wikipedia' in query:
        speak('wait... Searching Wikipedia')
        query = query.replace('wikipedia',"")
        result = wikipedia.summary(query, sentences=2)
        speak('According to Wikipedia')
        print(result)
        speak(result)

    elif "start" in query:
        query = query.replace("open","")
        query = query.replace("ARU","")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(3)
        pyautogui.press("Enter")    
        
    elif 'open google' in query:
        wb.open("https://www.google.co.in/") 

    elif 'open youtube' in query:
        wb.open("https://www.youtube.com/")

    elif 'apna college' in query:
        wb.open("http://www.ecbharatpur.ac.in/")    
    
    elif 'play music' in query:
        music_dir = "D:\\New Songs 2k20"
        songs = os.listdir(music_dir)
        print('songs')
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'play video' in query:
        music_dir = "D:\\video"
        songs = os.listdir(music_dir)
        print('Video')
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S:")
        print(strTime)
        speak(f"Sir, Time is{strTime}")

    elif 'open pycharm' in query:
        codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
        os.startfile(codePath)

    elif 'email to gc' in query:
        try:
            speak("what should i say?")
            content = takecommand().lower()
            to = "arpitsaxenabtp@gmail.com"
            sendEmail(to, content)
            speak("email sent sucessfully")
        except Exception as e:
            print(e)
            speak("Email is not sent")

    elif "alarm" in query:
        speak ("Sir please time btaiye!")
        time = input(":Sir please time btaiye:")

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")
            playsound('D:\\m')

    elif "where i am" in query or "where we are" in query:
        speak("wait sir, let me check")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            speak(f"sir i am not sure, but we are in {city} city of {country} country")
        except Exception as e:
         print("sorry sir,  Due to network issue i am not able to find where you are ??")
         speak("sorry sir,  Due to network issue i am not able to find where you are ??")
        pass
    
    elif " instagram profile" in query:
        speak("Sir please enter the user name correctly.")
        print("Sir please enter the user name correctly.")
        name = input("Enter username here:")
        wb.open(f"www.instagram.com/{name}")
        speak(f"Sir here is the profile of the user {name}")
        time.sleep(5)
        speak("sir would you like to download profile picture of this account.")
        condition = takecommand().lower()
        if "yes" in condition:
            mod = instaloader.Instaloader()
            mod.download_profile(name, profile_pic_only=True)
            speak("I am done sir,profile picture is saved in our main folder.")
        else:
            pass

    elif "take a screenshot" in query:
        speak("sir,please tell me the name for screenshot file")
        name = takecommand().lower()
        print("please sir hold the screen for few seconds, i am taking screenshot")
        speak("please sir hold the screen for few seconds, i am taking screenshot")
        time.sleep(3)
        img =pyautogui.screenshot()
        speak("Done sir")         
    