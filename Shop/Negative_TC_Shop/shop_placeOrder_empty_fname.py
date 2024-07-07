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

def login_shop():
    driver.get("https://uat.ushop.lk/sam01")

def add_to_cart():
    wait = WebDriverWait(driver, 10)

    # increment(+)
    add_item2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[2]/div/div[3]/div/div/button[2]')))
    #scrolling to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", add_item2)
    add_item2.click()
    add_item2.click()

    add_item3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div[2]/div[4]/div/div[3]/div/div[3]/div/div/button[2]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", add_item3)
    add_item3.click()

    #dicrement(-)
    remove_item2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/div[3]/div/div/button[1]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", remove_item2)
    remove_item2.click()

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

    # first_name = wait.until(EC.presence_of_element_located((By.NAME,'first_name')  ))
    # first_name.send_keys("Amali")
    last_name = wait.until(EC.presence_of_element_located((By.NAME,'last_name') ))
    last_name.send_keys("Perera")
    contact_no = wait.until(EC.presence_of_element_located((By.NAME,'contact_no') ))
    contact_no.send_keys("0719471609")
    contact_no_secondary = wait.until(EC.presence_of_element_located((By.NAME,'contact_no_secondary') ))
    contact_no_secondary.send_keys("0117896332")

    #Delivery details
    #radio button
    status = driver.find_element(By.XPATH,'//*[@id="Cash on Delivery"]').is_selected()    #true/faulse-not selected by default
    print(status) #false
    driver.find_element(By.XPATH, '//*[@id="Cash on Delivery"]').click()  #select raio button.
    status = driver.find_element(By.XPATH,'//*[@id="Cash on Delivery"]').is_selected()  # true/faulse-not selected by default
    print(status)  #true

    #dropdown menu
    #1.select 1 option.
    #2.capture options from drop down
    #3.count how many options present

    element = driver.find_element(By.NAME,'distance')
    drop_down = Select(element)

    #select by visible text
    #drop_down.select_by_visible_text("0KM-50KM")

    #select by index
    #drop_down.select_by_index(2)

    #select by value
    drop_down.select_by_value("04cbb7a1-441c-4e9d-a25f-f9b951f7af93") #value in html code


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
time.sleep(5)
driver.quit()
print("SUCCESSFULLY EXECUTED!")