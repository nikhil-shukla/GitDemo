from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonProject.pythonUtilities.datetimedemo import utility

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.implicitly_wait(2)
driver.find_element(By.NAME,"proceed").click()
driver.switch_to.alert.accept()
driver.find_element(By.NAME,"login").send_keys("Selenium")