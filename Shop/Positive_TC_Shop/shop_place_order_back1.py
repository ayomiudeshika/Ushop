#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

def login_shop():
    driver.get("https://uat.ushop.lk/sam01")

def add_to_cart():
    wait = WebDriverWait(driver, 10)
    item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[3]/div/div/button[2]')))
    #scrolling to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", item2)
    item2.click()

    # wait = WebDriverWait(driver, 10)
    # item2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[3]/div/div/button[2]')))
    # driver.execute_script("arguments[0].scrollIntoView(true);", item2)
    # item2.click()

    item3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[3]/div/div[3]/div/div/button[2]')))
    #item3 = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[3]/div/div[3]/div/div/button[2]')
    driver.execute_script("arguments[0].scrollIntoView(true);", item3)
    item3.click()

def place_order_back1():
    wait = WebDriverWait(driver, 10)
    cart = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')))
    #cart = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')
    cart.click()
    time.sleep(2)


    back1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[3]/div/button[1]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", back1)
    back1.click()



login_shop()
time.sleep(2)
add_to_cart()
time.sleep(2)
place_order_back1()
time.sleep(2)
driver.quit()
print("SUCCESSFULLY EXECUTED!")