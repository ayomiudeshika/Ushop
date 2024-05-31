#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

def aboutUs():
    driver.get("https://uat.ushop.lk/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"About Us").click()

def termsOfService():
    driver.get("https://uat.ushop.lk/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"Terms of Service").click()

def privacyPolicy():
    driver.get("https://uat.ushop.lk/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"Privacy Policy").click()

aboutUs()
time.sleep(2)
termsOfService()
time.sleep(2)
privacyPolicy()
time.sleep(2)
driver.close() #close only one browser at a time.
#driver.quit() close all the browsers.