from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def login():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div[2]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[2]').click()
    time.sleep(2)

def createItem():
    driver.find_element(By.LINK_TEXT,'Manage Items').click()

login()
time.sleep(2)
#createItem()
time.sleep(2)
driver.close()
