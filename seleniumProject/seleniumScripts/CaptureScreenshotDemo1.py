from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://facebook.com/")
driver.implicitly_wait(2)
driver.get_screenshot_as_file("selenium.png")
driver.get("https://google.com/")
driver.get_screenshot_as_file("selenium.png")
driver.quit()