#PASS
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
    mobile_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phone-no"]')))
    mobile_no.send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()

def cancel_discount_deletion():
    discount = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[3]')))
    discount.click()
    select_item = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/div[2]/div/div[4]/div/div[1]/a')))
    select_item.click()
    delete = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/form/div[3]/button[2]')))
    delete.click()
    time.sleep(2)
    cancel = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id=":r0:"]/div/div/div/div/button[1]')))
    cancel.click()
    time.sleep(2)

login()
cancel_discount_deletion()
driver.quit()
print("EXECUTED SUCCESSFULLY!")