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

def sort_Items():
    drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r5:"]/span/svg')))
    drop_down.click()

    def click_sort_option(xpath, wait):
        for _ in range(4):  # Retry up to 4 times
            try:
                sort_by = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", sort_by)
                sort_by.click()
                time.sleep(2)
                # driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    click_sort_option('//*[@id=":r4:"]/ul/ul/li[1]/button/li/a', wait)
    click_sort_option('//*[@id=":r4:"]/ul/ul/li[2]/button/li/a', wait)
    click_sort_option('//*[@id=":r4:"]/ul/ul/li[3]/button/li/a', wait)
    click_sort_option('//*[@id=":r4:"]/ul/ul/li[4]/button/li/a', wait)
    time.sleep(2)

login()
sort_Items()
driver.close()
print("SUCCESSFULLY EXECUTED!")

