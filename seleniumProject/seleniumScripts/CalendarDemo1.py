from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(5)
driver.find_element(By.ID, "datepicker").click()
time.sleep(1)

date=driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']/a")

for x in date:
    print(x.text)

    if x.text == "9":
        x.click()
        break

driver.quit()
