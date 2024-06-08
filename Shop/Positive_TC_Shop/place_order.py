from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

def login_shop():
    driver.get("https://uat.ushop.lk/sam")

def add_to_cart():
    item2 = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[3]/div/div/button[2]')
    #scrolling to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", item2)
    item2.click()
    item3 = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[3]/div/div[3]/div/div/button[2]')
    item3.click()

def place_order():
    cart = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')
    cart.click()
    #should check the amount here.
    next1 = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[3]/div/button[2]')
    driver.execute_script("arguments[0].scrollIntoView(true);", next1)
    next1.click()
    time.sleep(2)
    #Contact details
    driver.find_element(By.NAME,'first_name').send_keys("Amali")
    #driver.find_element(By.XPATH,'//*[@id="first-name"]').send_keys("Amali")
    driver.find_element(By.NAME,'last_name').send_keys("Perera")
    driver.find_element(By.NAME,'contact_no').send_keys("0719471609")
    driver.find_element(By.NAME,'contact_no_secondary').send_keys("0117896332")


login_shop()
add_to_cart()
place_order()
time.sleep(5)
driver.quit()
print("SUCCESSFULLY EXECUTED!")