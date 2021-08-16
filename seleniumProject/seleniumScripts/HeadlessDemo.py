import os

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

from pythonProject.pythonUtilities.datetimedemo import utility

#headless - config
opt=Options()
#opt.add_argument("--headless") #option1
opt.headless=True #option2
driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe",options=opt)

driver.maximize_window()
driver.get("https://www.goibibo.com/")
name = utility.current_time()
driver.get_screenshot_as_file(os.getcwd() + "/screenshots/"+"Goibibo_" + utility.current_time() + ".png")

driver.get("https://www.google.co.in/")
driver.get_screenshot_as_file(os.getcwd() + "/screenshots/" + "Google_" + utility.current_time() + ".png")
driver.quit()