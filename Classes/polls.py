import imp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
from settings import driver, POLL_DELAY_TIME
import Classes.CheckClass as check
import time


def do_polls():
    poll_number = 1
    print(colored('[+] Starting poll daemon', 'green'))
    # print('End time estimated:', cur_hour)
    driver.switch_to.frame(driver.find_element_by_id('frame'))
    while True:
        try:
            wait = WebDriverWait(driver, 5)
            element = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//button[starts-with(@aria-labelledby,"pollAnswerLabel")]')))

            time.sleep(POLL_DELAY_TIME)
            element.click()
            print('[+]', poll_number, 'poll(s) marked.')
            poll_number += 1
        except:
            pass
        if int(check.ryt_now().split(':')[1]) == 5:
            return

