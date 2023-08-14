from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution
import pathlib

# Your existing code for initializing the driver and other settings...

ListWeb = {'didi': "+919831143669",
            'dost': "+91",
            "pote": '+91'}

def WhatsappSender(driver, Name, Message):
    Speak(f"Preparing To Send a Message To {Name}")
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        Speak("Message Sent")
    except:
        Speak("Invalid Number")


def InitializeWhatsApp():
    options = Options()

    # Define scriptDirectory here
    scriptDirectory = pathlib.Path().absolute()

    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
    os.system("")
    os.environ["WDM_LOG_LEVEL"] = "0"
    PathofDriver = "DataBase\\chromedriver.exe"
    driver = webdriver.Chrome(PathofDriver, options=options)
    driver.maximize_window()

    return driver
