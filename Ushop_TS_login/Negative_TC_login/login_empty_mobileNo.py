#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.maximize_window()

def empty_mobileNo():
    OTP = "9774"
    driver.get("https://uat.ushop.lk/")
    driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div/div[1]/div[1]/div[1]/div/button').click()
    # mobile_no = wait .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phone-no"]')))
    # mobile_no.send_keys("767778194")
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/div[2]/form/div/button')))
    confirm_button.click()
    time.sleep(5)

    #alert = driver.switch_to.alert

    # Get the text of the alert
    #alert_text = alert.text
    #print("Alert text:", alert_text)

empty_mobileNo()
driver.close()
print("SUCCESSFULLY EXECUTED!")