#PASS
#changing the login credentials(mobile no)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()


def loginChange():
    driver.get("https://uat.ushop.lk/")
    #signin button
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/nav/div[1]/div/div[3]/div[1]/div/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    #change
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/div/div[1]/a').click()

loginChange()
time.sleep(2)
driver.close()
print('SUCCESSFULLY EXECUTED!')


#PASS
