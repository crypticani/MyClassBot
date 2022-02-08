from selenium.webdriver.common.keys import Keys
import time

import settings
import Classes.login as login
import Classes.utils as utils
import Classes.CheckClass as check
from Classes.polls import do_polls

from termcolor import colored


print(colored('Welcome to CodeTantra Bot', 'green'))
print(colored('Maintained by crypticani, originally developed by iron-war ', 'green'))
frequency = 1


have_class = False
while True:
    login.open()
    hr = check.get_time()
    if int(hr) >= 20:
        print(colored('[-] No classes are scheduled after 8 pm', 'cyan', attrs=['reverse', 'blink']))
        utils.abort()

    have_class = check.check_for_class(hr)

    if have_class and login.join():
        do_polls()
        # send_sms(process_hr)
        settings.driver.quit()
        time.sleep(60)
        print(colored('[+] Refreshing Daemon For other classes', 'cyan'))
    else:
        print(colored("[+] No ongoing lectures found at", 'blue'), colored(check.ryt_now(), 'blue'))
        settings.driver.quit()
        print(colored('[+] Sleeping for', 'blue'), colored(frequency, 'blue'), colored('minutes', 'blue'))
        time.sleep(frequency * 60)
    
    if have_class and login.join():
        # chatbox()
        print( 'replyed')
    else:
        print("class have not been joined")
