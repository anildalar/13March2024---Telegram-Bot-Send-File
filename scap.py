from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from topmodule.submodule.submoduel import Eleme1
from selenium.webdriver.chrome.options import Options
import time


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open Chrome in fullscreen mode


webdriver_service = Service('./chromedriver.exe')  # Replace '/path/to/chromedriver' with the actual path to chromedriver executable
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get('https://mphc.gov.in/case-status')


# Find the input element with id "txtnoS"
input_element = driver.find_element(By.ID, "txtnoS")

# Fill the value "123" into the input element
input_element.send_keys("123")

time.sleep(10)

# Close the browser
driver.quit()