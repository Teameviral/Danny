import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from Body.Listen import MicExecution
from Body.Speak import Speak

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "biography" in Query:
        Nameofweb=Query.replace("biography ", "")
        Link= f"https://en.everybodywiki.com/index.php?title=+Special%3ASearch&search={Nameofweb}&go=Go&ns0=1"
        webbrowser.open(Link)
        Speak(f"Searching the Query {Nameofweb}. Here is the result based on your information")
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("open ","")

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True
