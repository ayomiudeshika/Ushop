from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
#driver.implicitly_wait(10)


def login():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(5)

def add_Item():
    add_item_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[1]')))
    add_item_button.click()
    time.sleep(5)

#check item table
#Check catalog

#def add_Item():
    #addItem_Button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[1]')))
    #addItem_Button = driver.find_element(By.XPATH, '//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[1]')
    #addItem_Button.click()


login()
add_Item()
driver.close()
