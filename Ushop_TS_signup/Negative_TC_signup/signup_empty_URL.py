from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.maximize_window()


def signup():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    signup_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/nav/div[1]/div/div[3]/div[1]/div/button[2]')))
    signup_button.click()
    mobile_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phone-no"]')))
    mobile_no.send_keys("775413822")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(2)

    store_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="store-name"]')))
    store_name.send_keys("Anu closet")

    # store_URL = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="store-url"]')))
    # store_URL.send_keys("Anu")

    whatsapp_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="whats-app"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", whatsapp_no)
    whatsapp_no.send_keys("0775413822")

    address = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", address)
    address.send_keys("123, Batuwatta, Ragama.")

    description = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="description"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", description)
    description.send_keys(
        " Closet by Anu is an exclusive ladies' formalwear brand that offers power-dressing essentials that bring out the 'Boss lady' in every woman")

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div[2]/button')))
    next_button.click()
    time.sleep(5)

signup()
driver.close()
print("SUCCESSFULLY ECECUTED!")
