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
driver.maximize_window()
wait = WebDriverWait(driver, 10)


def login():
    OTP="9774"
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    mobile_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phone-no"]')))
    mobile_no.send_keys("767778194")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(20)
    driver.find_element(By.XPATH, '//*[@id="phone-no"]').send_keys("OTP")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[2]/form/div/button').click()
    time.sleep(5)


def next_previous():
    driver.find_element(By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[1]').click()
    time.sleep(2)
    next = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/div[3]/nav/ul/li[6]/button')))
    driver.execute_script("arguments[0].scrollIntoView(true);", next)
    next.click()
    previous = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/div[3]/nav/ul/li[1]/button')))
    driver.execute_script("arguments[0].scrollIntoView(true);", previous)
    previous.click()
    time.sleep(2)

    def click_pageNo(xpath,wait):
        for _ in range(4):  # Retry up to 4 times
            try:
                page_no = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", page_no)
                page_no.click()
                time.sleep(2)
                #driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    click_pageNo('//*[@id="body"]/body/div[1]/div/div[3]/nav/ul/li[5]/button',wait)#pg4
    click_pageNo('//*[@id="body"]/body/div[1]/div/div[3]/nav/ul/li[3]/button',wait)#pg3
    click_pageNo('//*[@id="body"]/body/div[1]/div/div[3]/nav/ul/li[4]/button',wait)#pg2
    click_pageNo('//*[@id="body"]/body/div[1]/div/div[3]/nav/ul/li[2]/button',wait)#pg1
    time.sleep(2)

login()
next_previous()
driver.close()
print("SUCCESSFULLY EXECUTED!")
