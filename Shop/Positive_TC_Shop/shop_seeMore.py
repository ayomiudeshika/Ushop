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

def see_more():
    wait = WebDriverWait(driver, 10)
    see_more_item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/a')))
    driver.execute_script("arguments[0].scrollIntoView(true);", see_more_item2)
    see_more_item2.click()

    add_item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id=":r2:"]/div/div/div[2]/div[4]/div/button[2]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_item2)
    add_item2.click()
    add_item2.click()
    time.sleep(2)

    remove_item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id=":r2:"]/div/div/div[2]/div[4]/div/button[1]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", remove_item2)
    remove_item2.click()
    time.sleep(2)

    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id=":r2:"]/div/div/div[2]/div[5]/button')))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
    add_to_cart.click()


login_shop()
see_more()
time.sleep(5)
driver.quit()
print("SUCCESSFULLY EXECUTED")