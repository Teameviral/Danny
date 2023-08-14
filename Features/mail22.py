# import os
# import webbrowser
# from Body.Speak import Speak
# from Body.Listen import MicExecution
# import openai
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

# # ... (your existing code)

# driver = webdriver.Chrome(executable_path="DataBase\chromedriver.exe")

# def send_mail(Query):
#     Query = str(Query).lower()

#     if "send mail" in Query or "mail" in Query or "email" in Query:
#         Speak("Please write the recipient's email address.")
#         recipient = input("Recipient Email: ")

#         Speak("Please write the subject of the email.")
#         subject = input("Subject: ")

#         Speak("Please write the body of the email.")
#         body = input("Body: ")

#         if send_email_via_gmail(recipient, subject, body):
#             Speak("Email sent successfully.")
#         else:
#             Speak("Sorry, there was an error sending the email.")

#         return True

#     elif "start" in Query:
#         Nameoftheapp = Query.replace("open ", "")

#         if "chrome" in Nameoftheapp:
#             os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
#             return True

# # ... (your existing code)

# def send_email_via_gmail(recipient, subject, body):
#     # Replace this with your actual Gmail login credentials
#     email = "neuralelectronicsconsortium@gmail.com"
#     password = "Fingapara2#"

#     # Check if Gmail is already open
#     if "mail.google.com" not in driver.current_url:
#         # Open Gmail in Chrome and wait for it to load
#         webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
#         try:
#             WebDriverWait(driver, 10).until(EC.title_contains("Gmail"))
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
#         except TimeoutException:
#             Speak("Failed to open Gmail. Please check your internet connection and try again.")
#             print("Failed to open Gmail. Please check your internet connection and try again.")
#             return False

#     try:
#         email_field = driver.find_element(By.XPATH, "//input[@type='email']")
#         email_field.send_keys(email)
#         driver.find_element(By.ID, "identifierNext").click()
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
#         password_field = driver.find_element(By.XPATH, "//input[@type='password']")
#         password_field.send_keys(password)
#         driver.find_element(By.ID, "passwordNext").click()
#         WebDriverWait(driver, 10).until(EC.title_contains("Gmail"))
#     except NoSuchElementException:
#         # If the email input field is not found, raise an exception and return False
#         Speak("Failed to find the email input field. Please try again.")
#         print("Failed to find the email input field. Please try again.")
#         return False
#     except TimeoutException:
#         Speak("Failed to login to Gmail. Please check your internet connection and try again.")
#         print("Failed to login to Gmail. Please check your internet connection and try again.")
#         return False

#     # Rest of the code remains unchanged
#     # Compose and send the email
#     try:
#         driver.find_element(By.CSS_SELECTOR, "div[role='button'][gh='cm']").click()
#         sleep(2)
#         driver.find_element(By.NAME, "to").send_keys(recipient)
#         driver.find_element(By.NAME, "subjectbox").send_keys(subject)
#         driver.find_element(By.CSS_SELECTOR, "div[role='textbox']").send_keys(body)
#         driver.find_element(By.CSS_SELECTOR, "div[role='button'][data-tooltip='Send ‪(Ctrl-Enter)‬']").click()
#         sleep(5)
#         return True
#     except NoSuchElementException:
#         Speak("Failed to send the email. Please check your input and try again.")
#         print("Failed to send the email. Please check your input and try again.")
#         return False
    






