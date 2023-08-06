from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Danny : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Danny : Wait For Few Seconds More")
from Main import MainTaskExecution

def is_stop_command(text):
    return "stop" in text.lower() or "close" in text.lower()

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

        elif "who created you" in Data:
            Speak("I was created by Avishek Bhattacharjee")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

