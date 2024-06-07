#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

def resendOTP():
    driver.get("https://uat.ushop.lk/")
    # signin button
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/nav/div[1]/div/div[3]/div[1]/div/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(70)
    #Try again
    driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div/div[2]/form/div/div/div[2]/div/button').click()

resendOTP()
time.sleep(2)
driver.close()
print('SUCCESSFULLY EXECUTED!')
