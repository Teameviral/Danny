import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai
import os
import webbrowser
from Body.Speak import Speak
from Body.Listen import MicExecution
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Brain.AIBrain import ReplyBrain

# Initialize OpenAI API with your API key
openai.api_key = "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"

# ... (your existing code)

driver = webdriver.Chrome(executable_path="DataBase\chromedriver.exe")

def send_email_via_gmail(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create a MIMEText object for the email content
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the Gmail SMTP server
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email, sender_password)

        # Send the email
        mail.sendmail(sender_email, recipient_email, message.as_string())
        mail.close()

        return True
    except Exception as e:
        print(e)
        return False
    
def generate_email_body(subject, name, designation):
    # Create a prompt for the email body generation
    prompt = f"Subject: {subject}\nName: {name}\nDesignation: {designation}\n\n"

    # Call the OpenAI API to generate the email body
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine for your use case
        prompt=prompt,
        temperature=0.7,  # Adjust the temperature to control the randomness of the generated text
        max_tokens=250,   # Adjust the max_tokens to limit the length of the generated text
        n=1               # Number of completions to generate
    )

    # Extract the generated email body from the API response
    email_body = response['choices'][0]['text'].strip()

    return email_body


def send_mail(Query):
    Query = str(Query).lower()

    if "send mail" in Query or "mail" in Query or "email" in Query:
        Speak("Please write your email address from which you want to send the email.")
        sender_email = input("Your Email Address: ")

        Speak("Please write the password for your email account. Remember the password should be the apppassword after turning on the twostep")
        sender_password = input("Password: ")

        Speak("Please write the recipient's email address.")
        recipient_email = input("Recipient Email: ")

        Speak("Please tell the subject of the email.")
        subject=MicExecution()
        subject = str(subject)

        Speak("Please tell your name?")
        name = MicExecution()
        name=str(name).lower()

        Speak("Please write your sender designation like sir/ma'am/dear/bro.")
        designation = input("Designation: ")

        # Read the email body from a file (e.g., 'Data\Api.txt') or generate it as per your requirement
        # Here, I'll assume you have a file 'Data\Api.txt' with the email body
        email_body = generate_email_body(subject, designation, name)
        print(email_body)

        if send_email_via_gmail(sender_email, sender_password, recipient_email, subject, email_body):
            Speak("Email sent successfully.")
        else:
            Speak("Sorry, there was an error sending the email.")

        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("open ", "")

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True

# ... (your existing code)
