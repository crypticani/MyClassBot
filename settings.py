from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


ID = 12345678
PASSWORD = 'UMS Password'

BROWSER_PATH = "Path of Chrome.exe"

POLL_DELAY_TIME = 30


# Do not edit below code without knowing what is does
brave_path = BROWSER_PATH
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)