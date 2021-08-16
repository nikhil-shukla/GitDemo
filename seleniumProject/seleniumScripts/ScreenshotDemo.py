import os

from selenium import webdriver

from pythonProject.pythonUtilities.datetimedemo import utility

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.goibibo.com/")
name = utility.current_time()
driver.get_screenshot_as_file(os.getcwd() + "/screenshots/"+"Goibibo_" + utility.current_time() + ".png")

driver.get("https://www.google.co.in/")
driver.get_screenshot_as_file(os.getcwd() + "/screenshots/" + "Google_" + utility.current_time() + ".png")
driver.quit()
