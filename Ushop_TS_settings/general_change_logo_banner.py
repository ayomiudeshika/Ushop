import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchWindowException

#from selenium.common.exceptions import StaleElementReferenceException


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

def upload_files():
    settings = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[5]')))
    settings.click()


    # Wait for the logo input field to be visible and upload the logo
    logo_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="general-example"]/div/form/div[1]/div[1]/div[1]/div/div/button')))  # Replace with the actual XPath
    logo_input.send_keys(r"F:\downloads\logo02.jpg")  # Replace with the actual file path

    # Wait for the banner input field to be visible and upload the banner
    banner_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="general-example"]/div/form/div[1]/div[1]/div[2]/div/div/button')))  # Replace with the actual XPath
    banner_input.send_keys(r"F:\downloads\Banner02.jpg")  # Replace with the actual file path
    time.sleep(5)

    save = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="general-example"]/div/form/div[2]/button')))
    driver.execute_script("arguments[0].scrollIntoView(true);", save)
    save.click()
    time.sleep(5)

try:
    upload_files()
except selenium.common.exceptions.NoSuchWindowException as e:
    print(f"Window closed unexpectedly: {e}")
finally:
    # Add a sleep to see the result if needed
    time.sleep(5)


login()
upload_files()
driver.quit()
print("SUCCESSFULLY EXECUTED!")