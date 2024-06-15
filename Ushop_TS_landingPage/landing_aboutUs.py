#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.implicitly_wait(10)
driver.maximize_window()

# def login():
#     wait = WebDriverWait(driver, 20)
#     driver.get("https://uat.ushop.lk/")
#
#     def click_element(xpath,wait):
#         for _ in range(4):  # Retry up to 3 times
#             try:
#                 element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#                 driver.execute_script("arguments[0].scrollIntoView(true);", element)
#                 element.click()
#                 driver.back()
#                 break  # Exit the loop if successful
#             except StaleElementReferenceException:
#                 pass  # Retry the loop if exception occurs
#
#     click_element('//*[@id="body"]/body/div[1]/div/div[2]/a[1]',wait)
#     click_element('//*[@id="body"]/body/div[1]/div/div[2]/a[2]',wait)
#     click_element('//*[@id="body"]/body/div[1]/div/div[2]/a[3]',wait)
#     click_element('//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button',wait)
#Identifies a time out exception.

def aboutUs():
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.LINK_TEXT,"About Us").click()

def termsOfService():
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.LINK_TEXT,"Terms of Service").click()

def privacyPolicy():
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.LINK_TEXT,"Privacy Policy").click()

def getStarted():
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH,"//button[normalize-space()='Get Started']").click()
    time.sleep(2)


aboutUs()
time.sleep(2)
termsOfService()
time.sleep(2)
privacyPolicy()
time.sleep(2)
getStarted()
#login()
time.sleep(2)
driver.close()
print('SUCCESSFULLY EXECUTED!')

#close only one browser at a time.
#driver.quit() close all the browsers.