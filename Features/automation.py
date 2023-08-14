import webbrowser
from Body.Listen import MicExecution
from Body.Speak import Speak
import keyboard
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from os import startfile
from pyautogui import click

# def play_video(video_number, search_results):
#     if video_number == 1:
#         link = f"https://www.youtube.com{search_results[0]['link']}"
#     elif video_number == 2:
#         link = f"https://www.youtube.com{search_results[1]['link']}"
#     else:
#         Speak("Sorry, I can only play the first or second video.")
#         return

#     Speak("")

# search_results = [
#     {'title': 'Video 1 Title', 'link': '/watch?v=video1'},
#     {'title': 'Video 2 Title', 'link': '/watch?v=video2'},
#     # ...
# ]

def chromeauto():
    Speak("Chrome automation activated. Please give a command.")
    
    while True:
        command = MicExecution()
        command = str(command).lower().strip()

        if 'new tab' in command:
            press_and_release('ctrl + t')
        elif 'close tab' in command:
            press_and_release('ctrl + w')
        elif 'new window' in command:
            press_and_release('ctrl + n')
        elif 'history' in command:
            press_and_release('ctrl + h')
        elif 'downloads' in command:
            press_and_release('ctrl + j')
        elif 'bookmark' in command:
            press_and_release('ctrl + d')
        elif 'switch tab' in command:
            Speak("To which tab?")
            tab = MicExecution()
            if tab.isdigit():
                Tab = int(tab)
                if Tab >= 1 and Tab <= 8:  # Assuming up to 8 tabs
                    press_and_release(f'ctrl + {Tab}')
                else:
                    Speak("Invalid tab number")
            else:
                Speak("Please enter a valid tab number")
        elif 'move tab' in command:
            tab = command.replace("move tab", "").strip()
            if tab.isdigit():
                Tab = int(tab)
                if Tab >= 1 and Tab <= 8:  # Assuming up to 8 tabs
                    press_and_release(f'ctrl + {Tab}')
                else:
                    Speak("Invalid tab number")
            else:
                Speak("Please enter a valid tab number")
        elif 'incognito' in command:
            press_and_release('ctrl + shift + n')
        elif 'exit' in command:
            Speak("Chrome automation deactivated.")
            break
        else:
            Speak("Invalid command. Please try again.")
    
    Speak("Work Done!")



# Call the chromeauto function with a command to execute
# chromeauto("move tab")





# def YouTubeAuto(command):
#     query=str(command)

#     if "pause" in query:
#         press_and_release('k')
#         return ""