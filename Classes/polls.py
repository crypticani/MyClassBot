import imp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
# from bot import JOINED_TIME
from settings import driver, POLL_DELAY_TIME
import Classes.CheckClass as check
import time
from Classes.chatbox import chatbox

JOINED_TIME = time.strftime("%H:%M:%S",time.localtime())

def do_polls():
    poll_number = 1
    class_title = driver.find_elements_by_tag_name("h1")
    print(class_title)
    print('Joined the class at ', JOINED_TIME)
    print(colored('[+] Starting poll daemon', 'green'))
    # print('End time estimated:', cur_hour)
    chatbox()
    driver.switch_to.frame(driver.find_element_by_id('frame'))
    while True:
        try:
            wait = WebDriverWait(driver, 5)
            element = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//button[starts-with(@aria-labelledby,"pollAnswerLabel")]')))
            # start_time = time.time()
            # choice_poll = input(print(colored("Enter 'y' to poll yourself: ", 'blue')))
            # while time.time() - start_time > 21 or choice_poll!='y' or choice_poll!='Noney':
            #     if choice_poll=='y' or choice_poll=='Noney':
            #         print("Auto poll marking paused.")
            #         time.sleep(300)
            #         element.click()
            
            time.sleep(POLL_DELAY_TIME)
            element.click()
            print('[+]', poll_number, 'poll(s) marked.')
            poll_number += 1
        except:
            pass

        if int(check.ryt_now().split(':')[1]) > 52:
            wait_end = WebDriverWait(driver, 5)
            element_end = wait_end.until(
                EC.element_to_be_clickable((By.XPATH, '//button[starts-with(@aria-labelledby,"OK")]')))
            print(colored('Class Ended', 'red'))
            print(colored('Sleeping for 30 Seconds', 'cyan'))
            time.sleep(30)
            return
        
        # is_active = driver.find_elements_by_id("app")
        # if is_active:
        #     return

        # cur_time_hr = int(time.strftime("%H:%M:%S",time.localtime()).split(':')[0])
        # join_time_hr = int(JOINED_TIME.split(':')[0])
        # if int(check.ryt_now().split(':')[0]) == join_time_hr+1:
        #     cur_time = int(time.strftime("%H:%M:%S",time.localtime()).split(':')[1])
        #     join_time = int(JOINED_TIME.split(':')[1])
        #     if abs(join_time-cur_time) > 3:
        #         return

