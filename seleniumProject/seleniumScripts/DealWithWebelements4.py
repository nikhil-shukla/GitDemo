from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# s=Service("F:/Study/SeleniumWebDrivers/chromedriver.exe")

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

l1=driver.find_elements(By.TAG_NAME, "a")

for x in l1:
    print("\n")
    print(x)


#forgotLink = driver.find_element(By.LINK_TEXT, "Forgot your password?")
forgotLink = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot your")
forgotLink.click()

driver.quit()