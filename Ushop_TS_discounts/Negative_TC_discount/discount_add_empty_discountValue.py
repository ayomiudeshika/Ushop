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

def add_discount():
    discount = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/nav[1]/div[1]/div/div[3]/div[1]/a[3]')))
    discount.click()
    add_new = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/div[1]/a')))
    add_new.click()
    discount_name = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="discount-name"]')))
    discount_name.send_keys("Summer Sale")

    discount_code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="body"]/body/div[1]/div/form/div[1]/div/a')))
    discount_code.click()

    #discount items entering field should be here.
    #calender
    # start_date = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="start-date"]')))
    # start_date.send_keys("06132024")
    switch_to_percentage = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/form/div[2]/div[3]/div/div[1]/div/button[1]')))
    switch_to_percentage.click()

    # discount_amount_fixed = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="dicount"]')))
    # discount_amount_fixed.send_keys("10")
    # time.sleep(2)

    save = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/body/div[1]/div/form/div[3]/button')))
    save.click()
    time.sleep(5)



login()
add_discount()
driver.close()
print("SUCCESSFULLY EXECUTED!")

#discount items entering field.
#Using calender option.