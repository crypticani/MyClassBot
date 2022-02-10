from selenium.webdriver.common.keys import Keys
import time
from termcolor import colored
from settings import driver
from Classes.login import join_again

def add(hour, val):
    return str(int(hour) + val)


#get current time
def ryt_now():
    cur_time = time.localtime()
    cur_time=time.strftime("%H:%M:%S",cur_time)
    return cur_time

#get hour form ryt_now()
def get_time():
    cur_time = ryt_now()
    hour, mn, sec = cur_time.split(':')
    if int(mn) >= 40:
        hour = str((int(hour) + 1))
    return hour


def process_hr(cur_hr, minutes):
    if int(cur_hr) > 12:
        cur_hr = str((int(cur_hr) - 12))
    cur = str((minutes + 60) % 60)
    if len(cur) < 2:
        cur = '0' + cur
    return cur_hr + ':' + cur
    

# check for classes from cur time t in order t - 1, t, t + 1
# handle false positive of night
# can be more efficient
def check_for_class(hour):
    print(colored('Checking for ongoing class', 'cyan'))
    for cur_hr in [add(hour, -2), add(hour, -1), hour, add(hour, 1)]:
        for minutes in range(0, 60):
            val = process_hr(cur_hr, minutes)
            # print('Checking class at', val)
            try:
                path = "//div[@data-start='" + val + "']"
                current_class = driver.find_element_by_xpath(path)
                extra_check = current_class.get_attribute('data-full')
                if len(extra_check) > 8:
                    continue
                print(val, ' - Class Found')
                current_class.find_element_by_xpath("./../..").send_keys(Keys.RETURN)
                return val
            except:
                pass
    return False
