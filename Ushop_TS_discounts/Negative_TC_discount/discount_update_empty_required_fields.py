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

def update_discount():
    discount = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[3]')))
    discount.click()

    def empty_mandatory_fields(xpath, wait):

        for _ in range(3):  # retry upto 5 items
            try:
                discount_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/div/div[4]/div/div[1]/a')))
                discount_name.click()
                mandatory_field = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", mandatory_field)
                mandatory_field.clear()
                save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/form/div[3]/button[1]')))
                save.click()
                time.sleep(5)
                driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    empty_mandatory_fields('//*[@id="discount-name"]', wait)
    empty_mandatory_fields('//*[@id="discount_code"]', wait)
    empty_mandatory_fields('//*[@id="dicount"]', wait)

login()
update_discount()
driver.quit()
print("SUCCESSFULLY EXECUTED! ")
