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

def remove_distances_prices():
    settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[5]')))
    settings.click()
    distances_prices = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="distance-tab-example"]')))
    distances_prices.click()

    def cancel_close_delete(XPATH,wait):

        for _ in range(3):  # retry upto 5 items
            try:
                bin = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="distance-example"]/div/div/div[2]/table/tbody/tr[2]/td[3]/i')))
                bin.click()
                actions = wait.until(EC.visibility_of_element_located((By.XPATH, wait)))
                driver.execute_script("arguments[0].scrollIntoView(true);", actions)
                actions.click()
                time.sleep(5)
                driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    cancel_close_delete('//*[@id=":r2:"]/div/div/div/div/button[1]', wait)
    cancel_close_delete('//*[@id=":r2:"]/div/div/button/svg', wait)
    cancel_close_delete('//*[@id=":r2:"]/div/div/div/div/button[2]', wait)

login()
remove_distances_prices()
driver.quit()
print("SUCCESSFULLY EXECUTED!")



