from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

def login():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(5)


def view_reporting():
    driver.find_element(By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[4]').click()
    time.sleep(2)


login()
view_reporting()
driver.close()
print("SUCCESSFULLY EXECUTED")
