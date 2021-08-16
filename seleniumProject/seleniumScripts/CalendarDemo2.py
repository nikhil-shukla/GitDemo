from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//label[@for='departure']").click()
time.sleep(1)

date=driver.find_elements(By.XPATH, "//div[@role='gridcell']/div/p[1]")

for x in date:
    print(x.text)

    if x.text == "28":
        x.click()
        break

time.sleep(5)
driver.quit()
