# from Body.Listen import MicExecution
# from Body.Speak import Speak
# from bs4 import BeautifulSoup


# def Temp():
#     search = "temperature in delhi"
#     url = f"https://www.google.com/search?q={search}"
#     r = requests.get(url)
#     data = BeautifulSoup(r.text,"html.parser")
#     temperature = data.find("div",class_ = "BNeawe").text
#     Speak(f"The Temperature Outside Is {temperature} celcius")

#     Speak("Do I Have To Tell You Another Place Temperature ?")
#     next = takecommand()

# if 'yes' in next:
#     Speak("Tell Me The Name Of tHE Place ")
#     name = takecommand()
#     search = f"temperature in {name}"
#     url = f"https://www.google.com/search?q={search}"
#     r = requests.get(url)
#     data = BeautifulSoup(r.text,"html.parser")
#     temperature = data.find("div",class_ = "BNeawe").text
#     Speak(f"The Temperature in {name} is {temperature} celcius")

# else:
#         Speak("no problem sir")