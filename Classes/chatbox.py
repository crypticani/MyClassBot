from selenium.webdriver.common.keys import Keys
from settings import driver
import time

#reply in chatbox(not working)
def chatbox():
    try:
        time.sleep(30)
        driver.find_element_by_xpath('//button[@aria-label="Users and messages toggle"]').send_keys(Keys.RETURN)
        time.sleep(5)
        print("ok")
        # driver.find_element_by_xpath('//div[@data-test="chatButton"]').send_keys(Keys.RETURN)
        # driver.find_element_by_xpath('//div[@aria-label="Public Chat"]').send_keys(Keys.RETURN)
        # time.sleep(5)
        # reply = driver.find_element_by_xpath('//textarea[@placeholder="Send message to Public Chat"]')
        # sendtext = "done"
        # reply.send_keys(sendtext)
        # reply.send_keys(Keys.ENTER)
        # print("Written in Chatbox")
    except:
        print("Error sending message")
        pass
    return 
