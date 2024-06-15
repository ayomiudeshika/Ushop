#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#PASS
def login_shop():
    driver.get("https://uat.ushop.lk/sam")

def add_to_cart():
    wait = WebDriverWait(driver, 10)

    # increment(+)
    add_item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[3]/div/div/button[2]')))
    #scrolling to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", add_item2)
    add_item2.click()

    add_item3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[3]/div/div[3]/div/div/button[2]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_item3)
    add_item3.click()

def order_review():
    wait = WebDriverWait(driver, 10)
    cart = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')))
    #cart = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')
    cart.click()

    add_item2_inreview = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/button[2]')))
    add_item2_inreview.click()

    remove_item2_inreview = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/button[1]')))
    remove_item2_inreview.click()

    delete_itme2_inreview = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/button/i')))
    delete_itme2_inreview.click()



login_shop()
add_to_cart()
order_review()
time.sleep(2)
driver.quit()
print("SUCCESSFULLY EXECUTED")