#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.maximize_window()

def login():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    mobile_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phone-no"]')))
    mobile_no.send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()

def change_discount_data():
    discount = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[3]')))
    discount.click()
    discount_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/div/div[4]/div/div[1]/a')))
    discount_name.click()

    discount_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="discount-name"]')))
    discount_name.clear()
    discount_name.send_keys("Update01")

    discount_code = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="discount_code"]')))
    discount_code.clear()
    discount_code.send_keys("U001")

    # discount items entering field should be here.
    # calender
    # start_date = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="start-date"]')))
    # start_date.send_keys("06132024")

    discount_amount_fixed = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dicount"]')))
    discount_amount_fixed.send_keys("8")

    save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/form/div[3]/button')))
    save.click()
    time.sleep(5)


login()
change_discount_data()
driver.close()
print("SUCCESSFULLY EXECUTED!")

