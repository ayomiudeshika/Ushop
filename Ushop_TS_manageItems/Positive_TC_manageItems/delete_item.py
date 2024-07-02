#error-cancel_close_delete
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
    mobile_no = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="phone-no"]')))
    mobile_no.send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(5)

def delete_item():
    item_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/div[3]/div/div[3]/div/div[2]/a')))
    item_name.click()


    def delete_confirmation(xpath,wait):
        for _ in range(3):  # Retry up to 3 times
            try:
                delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div[1]/form/div[1]/div/button[2]')))
                delete_button.click()
                cancel_close_delete = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", cancel_close_delete)
                cancel_close_delete.click()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    delete_confirmation('//*[@id=":rc:"]/div/div/div/div/button[1]',wait)
    delete_confirmation('//*[@id=":rc:"]/div/div/button/svg', wait)
    delete_confirmation('//*[@id=":rc:"]/div/div/div/div/button[2]', wait)
    time.sleep(2)

#Check catalog


login()
delete_item()
driver.close()
print("SUCCESSFULLY EXECUTED!")
