<h1 align="center"> DANNY </h1>

Meet Danny, your comprehensive AI-based virtual assistant that transforms your desktop experience into a realm of convenience and efficiency. Danny isn't just an assistant; it's your ultimate tool for seamless desktop management, communication, and information access.

- Automated Tasks: Danny is your personal automation wizard. It can handle tasks like sending emails, automating WhatsApp messages, and opening applications effortlessly. Need to schedule routine actions? Danny is your reliable timekeeper with its alarm-setting capabilities.

- Communication Made Easy: Stay connected effortlessly with Danny. Whether it's sending important emails or automating WhatsApp messages, Danny streamlines your communication. Just tell it what you need, and it takes care of the rest.

- Weather and Time Updates: No need to search for weather updates or check the time manually. Danny provides real-time weather forecasts and announces the current time, keeping you informed without lifting a finger.

- Set Personalized Alarms: Never miss an important event again. Danny's alarm feature ensures you're always on time and organized. Whether it's a meeting, a deadline, or a reminder, Danny has you covered.

- Effortless Information Retrieval: Curious about the weather? Wondering about the time in a different time zone? Need to access specific files or applications? Danny swiftly retrieves information, opens applications, and finds files, saving you valuable time.

- Customizable Experience: Danny adapts to your preferences. Customize its responses, behavior, and notifications to align with your unique needs and style. Danny is here to serve you exactly the way you want.

- Enhanced Productivity: With Danny as your AI desktop assistant, you'll experience heightened productivity and reduced manual effort. Let Danny handle repetitive tasks while you focus on what truly matters—your work, projects, and passions.

- Your AI Desktop Companion: Danny is designed for users like you who seek to simplify their digital life. From managing tasks to staying connected, from accessing information to setting reminders, Danny is the ultimate AI companion that seamlessly integrates into your desktop environment.

- Clap and Wakeup detection.




## How to run it?

- First Download Zip and Extract it

```
pip install -r requirements.txt
```

- Run the jarvis.py 

```
python jarvis.py
```

- If you use old python based functions then run 
```
python allinone.py
```

### Project Directory Structure

```bash
│   .gitignore
│   LICENSE
│   jarvis.py
│   allinone.py
│   main.py
│   README.md
│   requirements.txt
│   
│
├───Body
│   │   Listen.py
│   │   Speak.py
├───Brain
│   │   AIBrain.py
│   │   Qna.py
├───Data
│   │   Api.txt
│   │   Tasks.json
├───Features
│    alarm.py
│    clap.py
│    mail.py
│    temparature.py
│    Wakeup.py
├───Datsbase
│      alarm.txt
│      chatlog.txt
│      chromedriver.exe    
└───__pycache__
            main.cpython-310.pyc
            whatsapp.cpython-310.pyc

```