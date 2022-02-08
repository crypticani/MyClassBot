from selenium.webdriver.common.keys import Keys
from settings import driver
import time

#reply in chatbox(not working)
def chatbox():
    driver.find_element_by_xpath('//button[@aria-label="Users and messages toggle"]').send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_xpath('//div[@data-test="chatButton"]').send_keys(Keys.RETURN)
    reply = driver.find_element_by_xpath('//textarea[@placeholder="Send message to Public Chat"]')
    sendtext = "ok"
    reply.send_keys(sendtext)
    reply.send_keys(Keys.ENTER)
    return 
