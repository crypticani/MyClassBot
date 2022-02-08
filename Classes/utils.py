import imp
from termcolor import colored
import settings

def abort():
    print(colored('[-] Aborting', 'red'))
    settings.driver.quit()
    exit(0)