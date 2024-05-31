from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

def invalidOTP():
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/nav/div[1]/div/div[3]/div[1]/div/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("0000")
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()



invalidOTP()

driver.close()