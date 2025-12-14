import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Gets the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Joins it with your driver path
driver_path = os.path.join(script_dir, 'chromedriver-linux64/chromedriver')

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
# ... rest of code