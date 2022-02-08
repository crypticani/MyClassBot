# codetantrabot
This is python program to attend class on myclass(codetantra)

# Prerequisites
- You should have Python3 and Pip installed on your system
- Run the following command to install the dependencies
 ` pip install -r requirements.txt`
- Then, open settings.py, replace ID, Password and path of chrome browser as per your own.

# Run the Bot
- open cmd in the folder containing the codes
- Run the command:
` python bot.py`
- The bot will automatically open Chrome, login to MyClass, find the ongoing class, click on join and then join using microphone mode.
- If there is not any ongoing(green) class, it will sleep for sometime and then will try again. 
- Leave everything to the bot, even polls

## What about polls
- The bot will wait for 30 seconds after the poll is given.
- You can change the poll delay time as per your own convenience.
- If poll not answered by you within 30 seconds, it will automatically mark first option of the poll

# Credits
- This bot is a fork from https://github.com/iron-war/codetantrabot/
