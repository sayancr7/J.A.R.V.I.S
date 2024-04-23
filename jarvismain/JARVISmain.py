import datetime
import operator
import os
import random
import smtplib
import sys
import time
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from turtle import title
from turtledemo.chaos import f

import cv2
import instaloader
import psutil
import pyautogui
import pyjokes
import pyjokes as pyjokes
import pyttsx3
import pywhatkit as kit
import requests
import self as self
import speech_recognition as sr
import speedtest
import wikipedia
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate, Qt, QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pywikihow import search_wikihow
from requests import get

#voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)

#text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    tt = time.strftime("%I:%M %p")

    if hour>=5 and hour<12:
        speak(f"good morning sir, its {tt}")
    elif hour==12:
        speak(f"good noon sir, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon sir,its {tt}")
    elif hour>=18 and hour<21:
        speak(f"good evening sir, its {tt}")
    else:
        speak(f"good night sir, its {tt}")
    speak("i am jarvis. please tell me how can i help you")


#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=fdd4431a92394ce89e3fbd5ed27afe4e'
    main_page = requests.get(main_url).json()
    #print(main page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
    for ar in articles:
        head.append(ar["title"])

    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    #to convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            #audio = r.listen(source,timeout=4,phrase_time_limit=8)

        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            #speak("say that again please...")
            return "none"
        query = query.lower()
        return query



    #Executing Tasks through voice commands
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()


            #logic building for task

            #introduction


            #open notepad
            if "open notepad" in self.query:
                apath = "C:\\Windows\\notepad.exe"
                os.startfile(apath)

            #introduction    
            elif "introduce" in self.query:
                speak("hello i am jarvis, just a really very intelligent system. i am a voice assistant make by sayan, shadman, akash and aditya from techno international batanagar. as we know python is an emerging language so it becomes easy to write a script for voice assistant in python. the instructions for the assistant can be handled as per the requirement of user. speech recognition is the process of converting speech into text. this is commonly used in voice assistants like alexa, siri, google assistant etc. in python there is an api or application programming interface callspeech recognition which allows us to convert speech into text.  in the current scenario, advancement in technologies is such that they can perform any task with same effectiveness or can say more effectively than them. functionalities of this project include: i can send emails, send text on whatsapp, open command prompt, notepad, play music, search in wikipedia, open websites like google, youtube, tell ip address, find location, measure the temperature, internet speed and basic conversations. thats all about me. thank you.")


            #open dev c++
            elif "open c program" in  self.query:
                bpath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                os.startfile(bpath)

            #open cmd
            elif "open command prompt" in self.query:
                os.system("start cmd")

            #open camera
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
                break

            #play music
            elif "play music" in self.query:
                music_dir = "D:\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            #to adjust volume
            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")

            #to know ip address
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            #to search in wikipedia
            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                query = self.query
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
            # print(results)

            #to open youtube
            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            #to open facebook
            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            #to open github
            elif "open github" in self.query:
                webbrowser.open("www.github.com")

            #to search in google
            elif "search google" in self.query:
                speak("sir,what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            #send whatsapp message
            elif "send message" in self.query:
                speak("what is the message?")
                mes = self.takecommand().lower()
                kit.sendwhatmsg_instantly("+919339595933",f"{mes}")
                pyautogui.click(1050, 950)
                time.sleep(2)
                pyautogui.press('enter')

            #to play song on youtube
            elif "play song on youtube" in self.query:
                speak("which song do i play?")
                pl = self.takecommand().lower()
                kit.playonyt(f"{pl}")

            #to close notepad
            elif "close notepad" in self.query:
                speak("okey sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")


            #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            #to shut down the system
            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")

            #to restart the system
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            #to sleep the system
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            #to switch window
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            #news
            elif "tell me news" in self.query:
                speak("Please wait sir, fetching the latest news!!!`")
                news()

            #to send mail
            elif "send mail" in self.query:

                speak("sir, what should i say?")
                query = self.takecommand().lower()
                if "send a file" in query:
                    email = 'striversayan7@gmail.com'
                    password = 'Chottu@2002'
                    send_to_email = 'sayanhalder2k20@gmail.com'
                    speak("okay sir, what is the subject for this email?")
                    query = self.takecommand().lower()
                    subject = query
                    speak("and sir, what is the messege for this email?")
                    query2 = self.takecommand().lower()
                    messege = query2
                    speak("sir, please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")

                    speak("please wait! i am sending the mail now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(messege, 'plain'))

                    #setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Context-Disposition', "attachment; filename- %s" % filename)

                    #attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to sayan")

                else:
                    email = 'striversayan7@gmail.com'
                    password = 'Chottu@2002'
                    send_to_email = 'sayanhalder2k20@gmail.com'
                    messege = query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, messege)
                    server.quit()
                    speak("email has been sent to sayan")

            #to check temperature
            elif "temperature" in self.query:
                search = "temperature in kolkata"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")

            #to activate how to do mode
            elif "activate how to do" in self.query:
                speak("how to do mode is activated please tell me what do you want to know?")
                how = self.takecommand().lower()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this!")

            #to check battery of system
            elif "how much power" in self.query or "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
                if percentage>=65:
                    speak("we have enough power to continue our work")
                elif percentage>=30 and percentage<65:
                    speak("we should connect our system to charging point")
                elif percentage>=15 and percentage<30:
                    speak("we don't have enough power, please connect to charging")
                elif percentage<15:
                    speak("we have very low power, connect to charger or i am going to sleep very soon!")

            #to check internet speed
            elif "internet speed" in self.query:
                speak("i am calculating sir, please wait for sometime")
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                dl2 = ((dl/8)/1024)
                up2 = ((up/8)/1024)
                speak(f"sir we have {dl2} KB per second download speed and {up2} KB per second upload speed")



            #to find address
            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    #state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, due to network issue i am not able to find our location")
                    pass


            #to check instagram profile
            elif "instagram profile" in self.query:
                speak("sir please enter the user name correctly")
                name = input("enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir, would you like to download profile picture of this account?")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass

            #to take screenshot
            elif "take screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for the next command")


            #to do calculation
            elif "do some calculation" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("say what you want to calculate, example: 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add, #plus
                        '-': operator.sub, #minus
                        'x': operator.mul, #multiplied by
                        'divided': operator.__truediv__, #divided
                    }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))

            #conversations
            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something?")

            elif "how are you" in self.query:
                speak("i am fine sir, what about you?")

            elif "good" in self.query or "fine" in self.query:
                speak("that's great to hear from you!")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("ok sir, i am going to sleep you can call me anytime")
                break

            elif "goodbye" in self.query or "that's all" in self.query:
                speak("thanks for using me sir, have a good day")
                sys.exit()
                break

startExecution = MainThread()

class Ui_jarvisUI(object):
    def setupUi(self, jarvisUI):
        jarvisUI.setObjectName("jarvisUI")
        jarvisUI.resize(1059, 666)
        self.centralwidget = QtWidgets.QWidget(jarvisUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1061, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Project JARVIS/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 620, 91, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 620, 91, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -40, 401, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/Project JARVIS/T8bahf.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(810, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(16)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        jarvisUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUI)
        QtCore.QMetaObject.connectSlotsByName(jarvisUI)

    def retranslateUi(self, jarvisUI):
        _translate = QtCore.QCoreApplication.translate
        jarvisUI.setWindowTitle(_translate("jarvisUI", "JARVISUI"))
        self.pushButton.setText(_translate("jarvisUI", "Run"))
        self.pushButton_2.setText(_translate("jarvisUI", "Close"))


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.shw)
        self.ui.pushButton_2.clicked.connect(self.terminateWindow)

    def terminateWindow(self):
        self.close()
        sys.exit()

    def shw(self):
        self.ui.movie = QtGui.QMovie("D:/Project JARVIS/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/Project JARVIS/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
       
        speakNow = MainThread()
        speakNow.start()
        while True:
            QApplication.processEvents()
            dt = datetime.datetime.now()
            self.ui.textBrowser.setText('Date :- %s:%s:%s' % (dt.day, dt.month, dt.year))
            self.ui.textBrowser_2.setText('Time :- %s:%s:%s' % (dt.hour, dt.minute, dt.second))
        

    



   



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

