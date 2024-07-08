
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

def edit_item_empty_mandatory():


    def empty_mandatory_fields(xpath, wait):

        for _ in range(5):  #retry upto 5 items
            try:
                product = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/div[3]/div/div[4]/div/div[2]/a')))
                product.click()

                mandatory_field = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", mandatory_field)
                mandatory_field.clear()

                unit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="unit_id"]')))
                time.sleep(2)
                drop_down = Select(unit)
                drop_down.select_by_visible_text("Unit")

                submit_item = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div[1]/form/div[1]/div/button[1]')))
                submit_item.click()
                time.sleep(5)
                #driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    empty_mandatory_fields('//*[@id="product-name"]',wait)
    empty_mandatory_fields('//*[@id="product-price"]', wait)
    empty_mandatory_fields('//*[@id="product-count"]', wait)
    #empty_mandatory_fields('//*[@id="address"]', wait)


    # #visibility radio button
    # status = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[1]/form/div[2]/div/div[4]/label/div').is_selected()  # true/false-not selected by default
    # print(status)
    # driver.find_element(By.XPATH, '//*[@id="body"]/body/div[1]/div[1]/form/div[2]/div/div[3]/label/div').click()  # select raio button.
    # status = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[1]/form/div[2]/div/div[3]/label/div').is_selected()  # true/false-not selected by default
    # print(status)
    #
    # #Availability radio button
    # status = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[1]/form/div[2]/div/div[4]/label/div').is_selected()  # true/false-not selected by default
    # print(status)
    # driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[1]/form/div[2]/div/div[4]/label/div').click()  # select raio button.
    # status = driver.find_element(By.XPATH,'//*[@id="body"]/body/div[1]/div[1]/form/div[2]/div/div[4]/label/div').is_selected()  # true/false-not selected by default
    # print(status)
    #
    # submit_item = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div[1]/form/div[1]/div/button')))
    # submit_item.click()
    # time.sleep(5)

#Check catalog

login()
edit_item_empty_mandatory()
driver.close()
print("SUCCESSFULLY EXECUTED!")
