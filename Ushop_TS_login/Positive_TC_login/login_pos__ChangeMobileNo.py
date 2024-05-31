from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def loginChange():
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/div/div[1]/a').click()
loginChange()
time.sleep(2)
driver.close()

#PASS
