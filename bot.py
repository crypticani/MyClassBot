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


def main():
    have_class = False
    while True:
        login.open()
        hr = check.get_time()
        if int(hr) >= 20:
            print(colored('[-] No classes are scheduled after 8 pm', 'cyan', attrs=['reverse', 'blink']))
            utils.abort()

        have_class = check.check_for_class(hr)

        if have_class and login.join():
            print(colored("[+] Joined the Class", 'green'))
            do_polls()
            
            settings.driver.refresh()
            # settings.driver.close()
            print(colored("[+] Wait for 30 Seconds.", 'blue'))
            time.sleep(30)
            print(colored('[+] Refreshing Daemon For other classes', 'cyan'))
            
            login.join_again()
        else:
            print(colored("[+] No ongoing lectures found at", 'blue'), colored(check.ryt_now(), 'blue'))
            print(colored('[+] Sleeping for', 'blue'), colored('30', 'blue'), colored('seconds', 'blue'))
            time.sleep(30)
            settings.driver.refresh()

if __name__ == "__main__":
    main()
