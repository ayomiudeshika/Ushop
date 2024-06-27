#PASS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

def item_filters():
    wait = WebDriverWait(driver, 10)
    driver.get("https://uat.ushop.lk/sam01")

    # Define a helper function to click an element with retry logic
    #Retry Mechanism: Added a helper function click_element with retry logic to handle StaleElementReferenceException.
    def click_element(xpath):
        for _ in range(3):  # Retry up to 3 times
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    click_element('//*[@id="body"]/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/div/button')
    click_element('//*[@id="body"]/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/div/button')
    click_element('//*[@id="body"]/body/div[1]/div[2]/div[3]/div[1]/div/div[3]/div/button')


item_filters()
time.sleep(5)
driver.quit()
print('SUCCESSFULLY EXECUTED!')