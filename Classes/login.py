from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from termcolor import colored
import settings
import Classes.utils as utils
import time


def join():
    try:
        # wait = WebDriverWait(driver, 3600)
        # wait.until(EC.visibility_of_element_located(By.ID("//a[@role='button']")))
        settings.driver.find_element_by_class_name('btn').send_keys(Keys.RETURN)
        time.sleep(5)
        settings.driver.switch_to.frame(settings.driver.find_element_by_id('frame'))
        settings.driver.find_element_by_xpath('//button[@aria-label="Microphone"]').send_keys(Keys.RETURN)
        time.sleep(12)
        settings.driver.find_element_by_xpath('//button[@aria-label="Echo is audible"]').send_keys(Keys.RETURN)
        settings.driver.switch_to.default_content()
        return True
    except:
        settings.driver.refresh()
        # settings.driver.quit()
        # print(colored('[-] Join Button not available. Retrying in 30 Seconds', 'red', attrs=['reverse', 'blink']))
        # time.sleep(1 * 30)
        # return False


#login to codetantra
def do_login(username, password):

    id_field = settings.driver.find_element_by_xpath("//input[@placeholder='Username']")
    pass_field = settings.driver.find_element_by_xpath("//input[@placeholder='Password']")

    id_field.send_keys(username)
    pass_field.send_keys(password)

    pass_field.send_keys(Keys.RETURN)
    message = settings.driver.find_element_by_xpath("//a[@title='Click here to view Meetings']")
    message.send_keys(Keys.RETURN)


def open():
    settings.driver.get("http://myclass.lpu.in")

    # uncomment line below to hide the class tab
    #chrome_options.headless = True
    # chrome_options.add_argument("--mute-audio")

    try:
        do_login(settings.ID, settings.PASSWORD)
    except:
        print(colored('[-] Probably your credentials are invalid', 'red'))
        utils.abort()
