import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.southwest.com/air/check-in/index.html")

time.sleep(2)

input_confirm = driver.find_element_by_id("confirmationNumber")
input_fname = driver.find_element_by_id('passengerFirstName')
input_lname = driver.find_element_by_id('passengerLastName')

input_confirm.send_keys('2EGQJY')
time.sleep(2)
input_fname.send_keys('Andrew')
time.sleep(2)
input_lname.send_keys('Chow')
time.sleep(2)

checkin_btn = driver.find_element_by_id('form-mixin--submit-button')
print('pppp')
checkin_btn.click()
time.sleep(20)
print('yyyyy')
