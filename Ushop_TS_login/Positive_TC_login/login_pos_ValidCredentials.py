#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

def login():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    #signin
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(2)
    # otp_field = driver.find_element(By.ID, "otp_field_id")
    # otp_field.send_keys(otp)

login()
driver.close()
