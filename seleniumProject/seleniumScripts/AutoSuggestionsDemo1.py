from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


s=Service("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
time.sleep(5)
driver.find_element(By.ID, "tags").send_keys("S")
time.sleep(5)
l1 = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']//div")
print(len(l1))
for ele in l1:
    # print(ele.text)
    if ele.text == "Selenium":
        print("Record found")
        ele.click()
        break

driver.quit()