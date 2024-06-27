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

def change_whatsappNo_invalid():
    settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[5]')))
    settings.click()

    whatsapp_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="whats-app"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", whatsapp_no)
    whatsapp_no.clear()
    whatsapp_no.send_keys("07194716")

    save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="general-example"]/div/form/div[2]/button')))
    driver.execute_script("arguments[0].scrollIntoView(true);", save)
    save.click()
    time.sleep(5)

login()
change_whatsappNo_invalid()
driver.close()
print("SUCCESSFULLY EXECUTED!")
