from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://en-gb.facebook.com/")
time.sleep(1)
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(3)
month=driver.find_element(By.ID, "month")
m=Select(month)
m.select_by_index(2)
time.sleep(2)
m.select_by_value("8")
time.sleep(2)
m.select_by_visible_text("Apr")