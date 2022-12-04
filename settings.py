from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


ID = <your ums id>
PASSWORD = '<your ums password>'

BROWSER_PATH = "path of the browser"

POLL_DELAY_TIME = 30


# Do not edit below code without knowing what is does
brave_path = BROWSER_PATH
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
