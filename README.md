# Codetantrabot
This is python program to attend class on MyClass(codetantra)

# Prerequisites
- You should have Python3 and Pip installed on your system
- Copy the path of chrome (In Linux, it is inside /opt folder, in Windows, it can be found in C:\Program files folder)
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


# Chanegelog
## v2.2 (current)
- Added feature to join next class automatically
- Note: This feature is still in the development. Currently, it closes the current class at 59 minutes, and login again to find next ongoing class.
- Issue: If the previous class is still running till 59 minutes, then it will join the previous class again and hence, fails to join the next class
## v2.1
- fixed crash issue while joining the microphone mode
## v2.0
- Restructured whole code and modularized it
- added settings.py file for all the credentials and customizations
## v1.1
- Skip microphone permission check
- added delay in polls (you can set your own delay in creds.py)
## v1.0
- Initial version, fork of codetantrabot from iron-war

# Contributions
- Feel free to contribute to this project, either in terms of code, documentation or reporting issues.

# Credits
- This bot is a fork from https://github.com/iron-war/codetantrabot/
