import os
import subprocess
from Body.Speak import Speak
from Body.Listen import MicExecution
from datetime import datetime, timedelta
import speech_recognition as sr

def set_alarm(date, time, minutes, seconds):
    # Convert date and time to a datetime object
    alarm_datetime = datetime.strptime(date + ' ' + time, '%d %b %Y %I:%M %p')

    # Get the current datetime
    current_datetime = datetime.now()

    # Calculate the time difference
    time_difference = alarm_datetime - current_datetime

    if time_difference.total_seconds() > 0:
        # Calculate the time until the alarm in seconds
        time_until_alarm = time_difference.total_seconds()

        # Use the Windows built-in 'at' command to schedule the alarm
        alarm_command = f"cmd /c at {time_until_alarm:.0f} /interactive cmd /c start {os.path.abspath('alarm_sound.wav')}"
        subprocess.call(alarm_command, shell=True)
        print("Alarm set successfully!")
    else:
        print("Invalid alarm time. Please set an alarm for a future time.")

def set_reminder():
    recognizer = sr.Recognizer()
    
    # Get the current date and time
    current_date = datetime.now().strftime('%d %b %Y')
    current_time = datetime.now().strftime('%I:%M %p')
    
    # Ask the user to speak the reminder details
    with sr.Microphone() as source:
        print("Speak the reminder details:")
        audio = recognizer.listen(source)
    
    try:
        reminder_text = recognizer.recognize_google(audio)
        print("You said:", reminder_text)
        
        # Parse the reminder details
        reminder_time = "10:00 PM"  # Extract time from reminder_text
        reminder_task = "Example task"  # Extract task from reminder_text
        
        # Convert the reminder time to a datetime object
        reminder_datetime = datetime.strptime(current_date + ' ' + reminder_time, '%d %b %Y %I:%M %p')
        
        # Calculate the time difference for the reminder
        time_difference = reminder_datetime - datetime.now()
        
        if time_difference.total_seconds() > 0:
            # Store the reminder task in a text file
            with open("reminder.txt", "a") as file:
                file.write(f"{reminder_datetime}: {reminder_task}\n")
            print("Reminder set successfully!")
        else:
            print("Invalid reminder time. Please set a reminder for a future time.")
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand your input.")