from cgitb import text
from distutils.cmd import Command
from distutils.command.upload import upload
from fnmatch import translate
from modulefinder import IMPORT_NAME
from msilib import type_binary
from re import search
from tkinter import PAGES
from turtle import speed
from typing import Text
from unittest import result
from urllib import request
import pyjokes
import keyboard
import pyttsx3
import speech_recognition as sr
import webbrowser
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import pywhatkit
import wikipedia
from gtts import gTTS
import os 
import PyPDF2
import pyautogui
from playsound import playsound
from PyDictionary import PyDictionary as Diction
import datetime
from googletrans import Translator

Assertant = pyttsx3.init('sapi5')
voices = Assertant.getProperty('voices')
print(voices)
Assertant.setProperty('voices',voices[0].id)

def speak(audio):
    print("   ")
    Assertant.say(audio)
    print("   ")
    Assertant.runAndWait()

def takecommand():
    Command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        Command.pause_threshold = 1
        audio = Command.listen(source)
        
        try:
            print("Recognizing......")
            query = Command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")  
            
        except:
            return "None"
        
        return query.lower()
    
def TaskExe():
    
    speak("Hello , I am Soniya .")
    speak("How Can I Help You ?")
    
    def Music():
        speak("Tell Me The Name Of The Song!")
        musicName = takecommand()
        
        if 'Issey-Kehte-Hain-Hip-Hop' in musicName:
            os.startfile('C:\\song\\Issey-Kehte-Hain-Hip-Hop.mp3')
            
        elif 'Otilia---Bilionera' in musicName:
            os.startfile('c:\\song\\Otilia---Bilionera.mp3')  
            
        else: 
            pywhatkit.playonyt(musicName) 
            
        speak("Your Song Has Been Started! , Enjoy Sir!")        
    
    def OpenApp():
        speak("Ok Sir , Wait A Second!")
        
        if 'Code' in query:
            os.startfile("C:\\Users\\aksha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            
        elif 'Chrome'  in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")  
            
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')  
            
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/') 
            
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')         
            
        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@19.5320368,73.0995525,15z')
            
        speak("Your Command Has Been Completed Sir!")        
    
    def Speedtest():
        import speedtest
        speak("Checking speed.....")
        speed = speedtest.Speedtest()
        downloading = speed.downloade()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctupload =int(uploading/800000)
        
        if 'uploading' in query:
            speak(f"The Uploading Speed Is {correctupload} mbp s")
            
        elif 'downloading' in query:
            speak(f"The Downloading Speed Is {correctDown} mbp s")
            
        else:
            speak(f"The Downloading{correctDown} and The Uploading Speed{correctupload} mbp s")             
    
    def Dict():
        speak("Activated Dictionary")
        speak("Tell Me The problem!")
        prob1 = takecommand()
        
        if 'meaning' in prob1:
            prob1 = prob1.replace("What is the" ,"")
            prob1 = prob1.replace("soniya", "")
            prob1 = prob1.replace("of", "")
            prob1 = prob1.replace("meaning of", "")
            result = Diction.meaning(prob1)
            speak(f"The Meaning For {prob1} is {result}")
            
        elif 'synonym' in prob1: 
            prob1 = prob1.replace("What is the" ,"")
            prob1 = prob1.replace("soniya", "")
            prob1 = prob1.replace("of", "")
            prob1 = prob1.replace("synonym of", "")
            result = Diction.synonym(prob1)
            speak(f"The Synonym For {prob1} is {result}")  
            
        elif 'antonym' in prob1:
            prob1 = prob1.replace("What is the" ,"")
            prob1 = prob1.replace("soniya", "")
            prob1 = prob1.replace("of", "")
            prob1 = prob1.replace("antonym of", "")
            result = Diction.antonym(prob1)
            speak(f"The Antonym For {prob1} is {result}")  
            
        speak("Exited Dictionary!")      
    
    def CloseApp():
        speak("Ok Sir ,Wait A Second!")
        
        if 'youtube' in query:
            os.system("TASKILL /F /in chrome.exe")
            
        elif 'chrome' in query:
            os.system("TASKILL /F /in chrome.exe")
            
        elif 'code' in query:
            os.system("TASKILL /F /in Code.exe")  
            
        elif 'instagram' in query:
            os.system("TASKILL /F /in chrome.exe")  
            
        elif 'facebook' in query:
            os.system("TASKILL /F /in chrome.exe")  
            
        elif 'maps' in query:
            os.system("TASKILL /F /in chrome.exe")
            
        speak("Your Command Has Been Succesfully Completed!")                
     
    def YoutubeAuto():
        speak("Whats Your Command ?")
        comm = takecommand()
        
        if 'pause' in comm:
            keyboard.press('space bar')
            
        elif 'restart' in comm:
            keyboard.press('0')
            
        elif 'mute' in comm:
            keyboard.press('m')
            
        elif 'skip' in comm:
            keyboard.press('1')
            
        elif 'back' in comm:
            keyboard.press('j')
            
        elif 'full screen' in comm:
            keyboard.press('f')
            
        elif 'film mode' in comm:
            keyboard.press('t')
            
        speak("Done Sir")                            
    
    def Reader():
        speak("Tell Me The Name Of The Book!")
        
        name = takecommand()
        
        if 'indian' in name:
            
            os.startfile('C:\\Books\\Gray hat hacking\\ch 1.pdf')
            book = open('C:\\Books\\Gray hat hacking\\ch 1.pdf')
            pdfreader = PyPDF2.PdfFileReader(book)
            page = pdfreader.getNumPages()
            speak(f"Number Of Pages In The Book Are {page}")
            speak("From Which Pages I Hve To start Reading ?")
            numPages = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPages)
            text = page.extractText()
            speak("In Which Language , I Have To Read ?")
            lang = takecommand()
            
            if 'Hindi' in lang:
                trans1 =Translator()
                textHin = trans1.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                    
                except:
                    playsound('book.mp3')
                    
            else:
                speak(text)            
    
    def Temp():
        search = "temperature in maharashtra"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outsider Is {temperature} celcius")
               
    def Takehindi():
        Command = sr.Recognizer()
        with sr.Microphone() as source:
         print("Listening......")
        Command.pause_threshold = 1
        audio = Command.listen(source)
        
        try:
            print("Recognizing......")
            query = Command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")  
            
        except:
            return "None"
        
        return query.lower()
    
    def Tran():
        speak("Tell Me The Line!")
        line = Takehindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        speak(f"The Translation For This Line Is:" + Text)
    
    def ChromeAuto():
        speak("Chrome Autiomation starte!")
        
        Command = takecommand()
        
        if  'close this tab' in Command:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in Command:
            keyboard.press_and_release('ctrl + t') 
            
        elif 'open new window' in Command:
            keyboard.press_and_release('ctrl + n') 
            
        elif 'history' in Command:
            keyboard.press_and_release('ctrl + h')
                          
            
    while True:
        
        query = takecommand()
        
        if 'hello' in query:
            speak("Hello Sir , I Am soniya .")
            speak("Your Personal AI  Assistant!")
            speak("How May I Help You?")
            
        elif 'how are you' in query:
            speak("I Am Fine Sir!")
            speak("What About You?")
            
        elif 'you need a break' in query:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak("Just Say Wake Up Soniya!")
            break
            
        elif 'bye' in query:
            speak("Ok Sir , Bye!")
            break
             
        elif 'youtube search' in query:
            speak("Ok sir , this is What I Found For You searching!")
            query = query.replace("soniya", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' +  query  
            webbrowser.open(web) 
            speak("Done Sir!")    
            
        elif 'google search' in query:
            speak("This Is What I Found For Your Search Sir!")
            query = query.replace("soniya", "")
            query = query.replace("google searching", "") 
            pywhatkit.search(query)
            speak("Done Sir!")
            
        elif 'website' in query:
            speak("Ok Sir , Launching....")
            query = query.replace("soniya", "")
            query = query.replace("website", "")
            query = query.replace("  ", "")
            web1 = query.replace("Open", "")
            web2 = 'https://www.' + web1 + '.com' 
            webbrowser.open(web2)  
            speak("Launched!")
            
        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = takecommand() 
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")
            
        elif 'music' in query:
            Music()  
            
        elif 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("soniya", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query,2)
            speak(f"According To Wikipedia : {wiki}")
                       
        elif 'screenshote' in query:
            kk = pyautogui.screenshot()
            kk .save('C:\\')
            
        elif 'open facebook' in query:
            OpenApp()    
        
        elif 'open instagram' in query:
            OpenApp()
            
        elif 'open maps' in query:
            OpenApp()    
            
        elif 'open code' in query:
            OpenApp()    
             
        elif 'open youtube' in query:
            OpenApp()    
            
        elif 'open chrome' in query:
            OpenApp()    
            
        elif 'close chrome' in query:
            CloseApp() 
            
        elif 'close code' in query:
            CloseApp()
            
        elif 'close youtube' in query:
            CloseApp()
            
        elif 'close facebook' in query:
            CloseApp()
            
        elif 'close instagram' in query:
            CloseApp()
            
        elif 'close maps' in query:
            CloseApp()
            
        if 'pause' in query:
            keyboard.press('space bar')
            
        elif 'restart' in query:
            keyboard.press('0')
            
        elif 'mute' in query:
            keyboard.press('m')
            
        elif 'skip' in query:
            keyboard.press('1')
            
        elif 'back' in query:
            keyboard.press('j')
            
        elif 'full screen' in query:
            keyboard.press('f')
            
        elif 'film mode' in query:
            keyboard.press('t')     
            
        elif 'youtube tool' in query:
            YoutubeAuto()
            
        elif  'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t') 
            
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n') 
            
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')   
            
        elif 'chrome autiomation' in query:
            ChromeAuto()
            
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
                  
        elif 'repeat my words' in query:  
            speak("Speak Sir!")
            jj = takecommand()
            speak(f"You Said : {jj}")
            
        elif 'my location' in query:
            speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@19.5320368,73.0995525,15z')               
                                 
        elif 'dictionary' in query:
            Dict()
        
        elif 'translator' in query:
            Tran()
            
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that", "")
            remeberMsg = remeberMsg.replace("soniya", "")
            speak("You Tell Me To Remind You That :"+remeberMsg) 
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()
            
        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())       
         
        elif 'google searching' in query:
            import wikipedia as googlescrap
            query = query.replace("soniya", "")
            query= query.replace("google search", "")
            query = query.replace("google", "")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)
            
            try:
                result = googlescrap.summary(query,2)
                speak(result)
                
            except:
                speak("No Speakable Data Available!")
                               
        elif 'temperature' in query:
            Temp()
            
        elif 'book reade' in query:
            Reader()
            
        elif 'downloading speed' in query:
            Speedtest()
            
        elif 'uploadind speed' in query:
            Speedtest() 
            
        elif 'internet' in query:
            Speedtest()            
            
        elif 'how to' in query:
            speak("Getting Data From Internet")      
            op = query.replace("soniya","")
            max_result = 1 
            how_to_func = search_wikihow(op,max_result) 
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary) 
TaskExe()                            