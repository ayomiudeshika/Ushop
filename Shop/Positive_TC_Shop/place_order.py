from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

def login_shop():
    driver.get("https://uat.ushop.lk/sam")

def add_to_cart():
    wait = WebDriverWait(driver, 10)
    item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[3]/div/div/button[2]')))
    #scrolling to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", item2)
    item2.click()

    item3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[3]/div/div[3]/div/div/button[2]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", item3)
    item3.click()

def place_order():
    wait = WebDriverWait(driver, 10)
    cart = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')))
    #cart = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div[2]/div/button[2]')
    cart.click()

    #should check the amount here.

    next1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[3]/div/button[2]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", next1)
    next1.click()

    # #Contact details

    first_name = wait.until(EC.presence_of_element_located((By.NAME,'first_name')  ))
    first_name.send_keys("Amali")
    last_name = wait.until(EC.presence_of_element_located((By.NAME,'last_name') ))
    last_name.send_keys("Perera")
    contact_no = wait.until(EC.presence_of_element_located((By.NAME,'contact_no') ))
    contact_no.send_keys("0719471609")
    contact_no_secondary = wait.until(EC.presence_of_element_located((By.NAME,'contact_no_secondary') ))
    contact_no_secondary.send_keys("0117896332")

    #Delivery details
    #radio button
    # status = driver.find_element(By.XPATH,'//*[@id="Cash on Delivery"]').is_selected()    #true/faulse-not selected by default
    # print(status)
    # driver.find_element(By.XPATH, '//*[@id="Cash on Delivery"]').click()  #select raio button.
    # status = driver.find_element(By.XPATH,'//*[@id="Cash on Delivery"]').is_selected()  # true/faulse-not selected by default
    # print(status)
    
    status = driver.find_element(By.XPATH,'//*[@id="Bank Transfer"]').is_selected()  # true/faulse-not selected by default
    print(status)
    driver.find_element(By.XPATH, '//*[@id="Bank Transfer"]').click()  # select raio button.
    status = driver.find_element(By.XPATH, '//*[@id="Bank Transfer"]').is_selected()  # true/faulse-not selected by default
    print(status)

    #dropdown menu

    delivery_address = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="address"]') ))
    delivery_address.send_keys("14/D, Kandy Rd, Kadawatha.")
    comments = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="comment"]')))
    comments.send_keys("This is my first order, and I hope you will deliver my package as soon as possible and safely")
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[3]/div/button[2]')))
    next2.click()








login_shop()
time.sleep(2)
add_to_cart()
time.sleep(2)
place_order()
time.sleep(2)
driver.quit()
print("SUCCESSFULLY EXECUTED!")