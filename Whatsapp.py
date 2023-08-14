from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.Speak import Speak
import pathlib
from Body.Listen import MicExecution

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
Speak("Initializing The Whatsapp Software.")

ListWeb = {'mother' : "+918981824963",
            'dost': "+91",
            "pote": '+91'}

def WhatsappSender(Name):
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(10)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        Speak("Message Sent")
        
    except TimeoutException:
        Speak("Timeout: Send button not clickable")
    except Exception as e:
        print("Error:", e)


# ListWeb = {'mother' : "+918981824963",
#             'arunava': "+917980523133",
#             "pote": '+91'}

# def normalize_name(name):
#     # Normalize the name (convert to lowercase, remove spaces, etc.)
#     # You can use regex or string manipulation functions here
#     # For example: return name.replace(" ", "").lower()
#     return name

# def get_recipient_name():
#     while True:
#         Speak("To whom do you want to send a message?")
#         recipient_name = MicExecution().lower()
#         normalized_recipient_name = normalize_name(recipient_name)

#         if normalized_recipient_name in ListWeb:
#             return normalized_recipient_name
#         else:
#             Speak("Recipient not recognized. Please try again or say 'cancel' to cancel.")

# # Rest of your code

# def WhatsappSender():
#     recipient_name = get_recipient_name()
    
#     if recipient_name == "cancel":
#         Speak("Message sending canceled.")
#         return
#     Speak(f"Preparing To Send a Message To {recipient_name}")
#     Speak("What's The Message By The Way?")
#     Message = MicExecution()
    
#     Number = ListWeb.get(recipient_name)
#     if Number is None:
#         Speak("Recipient not recognized.")
#         return
    
#     LinkWeb = f'https://web.whatsapp.com/send?phone={Number}&text={Message}'
#     driver.get(LinkWeb)
    
#     try:
#         # Wait for the send button to become clickable
#         send_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
#         )
#         send_button.click()
#         Speak("Message Sent")
#     except TimeoutException:
#         Speak("Timeout: Send button not clickable")
#     except Exception as e:
#         print("Error:", e)





# def WhatsappSender(Name):
#     Speak(f"Preparing To Send a Message To {Name}")
#     Speak("What's The Message By The Way?")
#     Message = MicExecution()
#     Number = ListWeb[Name]
#     LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
#     driver.get(LinkWeb)
#     sleep(5)
#     try:
#         driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
#         Speak("Message Sent")
        
#     except:
#         print("Invalid Number")

