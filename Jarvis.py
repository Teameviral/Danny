from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Danny : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
from Features.mail import send_mail
# print(">> Started The Danny : Wait For Few Seconds More")
from Main import MainTaskExecution
import webbrowser
from Features.Open import OpenExe
from Features.automation import chromeauto
import os
# from Whatsapp import WhatsappSender, InitializeWhatsApp, ListWeb

def is_stop_command(text):
    return "stop" in text.lower() or "end task" in text.lower()

def MainExecution():
    Speak("Hey Whatsup")
    Speak("I'm Danny, I'm Ready To Assist You Sir.")

    while True:
        Data = MicExecution()
        Data = str(Data).replace(".", "")

        # Check for stop command
        if is_stop_command(Data):
            Speak("Listening stopped. Start Again If You Need My Help")
            break

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            pass

        elif len(Data) < 3:
            pass

        elif "whatsapp message" in Data:
            pass

        elif "turn on the tv" in Data:  # Specific COmmand
            Speak("Ok..Turning On The Android TV")
        elif "youtube search" in Data:
            Speak("I am searching! please wait...")
            Data= Data.replace("youtube search ", "")
            Data= Data.replace("Danny ", "")
            ignore_words = [',','?','/','.','!']
            for elements in ignore_words:
                if elements in Data:
                  Data= Data.replace(elements, "")
            Link=f"https://www.youtube.com/results?search_query={Data}"
            webbrowser.open(Link)
            Speak("Here is the result..")
            # if "play first video" or "start first video" in Data:
            #     play_video(1, search_results)
            # elif "play second video" in Link or "start second video" in Data:
            #     play_video(2, search_results)
        elif "chrome auto" in Data:
            chromeauto()

        elif "close chrome" in Data:
            os.system("TASKKILL /f /im Chrome.exe")
        # elif "close youtube" or "remove youtube" in Data:
        #     os.system("TASKKILL /f /im Chrome.exe")
        
        elif "who created you" in Data or "who is your owner" in Data or "who made you" in Data or "creator" in Data:
            Speak("I was created by Avishek Bhattacharjee")
        elif "send mail" in Data or "mail" in Data or "email" in Data:
            send_mail(Data)
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
        elif 'new chrome' in Data:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'see facebook' in Data:
            webbrowser.open('https://www.facebook.com/')
        elif 'see instagram' in Data:
            webbrowser.open('https://www.instagram.com/')
        elif 'find map' in Data:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        # elif "biography" in Data:

            # Nameofweb=Data.replace("biography ", "")
            # Link= f"https://en.everybodywiki.com/index.php?title=+Special%3ASearch&search={Nameofweb}&go=Go&ns0=1"
            # webbrowser.open(Link)
            # Speak(f"Searching the Query {Nameofweb}. Here is the result based on your information")

        # elif "open whatsApp" in Data:
        #     driver.get("https://web.whatsapp.com/")
        #     Speak("Initializing the WhatsApp Software.")
        # elif "send message to whatsApp" in Data:
        #     Speak("To whom do you want to send a message?")
        #     Recipient = MicExecution().lower()
        #     if Recipient in ListWeb:
        #         Speak("What's the message?")
        #         Message = MicExecution()
        #         WhatsappSender(driver, Recipient, Message)  # Adjust this call
        #     else:
        #         Speak("Recipient not recognized.")

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        # driver = InitializeWhatsApp()  # Create the driver instance
        print("")
        MainExecution()
        # MainExecution(driver)  # Pass the 'driver' instance to MainExecution
        # driver.quit()  # Don't forget to quit the driver when done
    else:
        pass


ClapDetect()

