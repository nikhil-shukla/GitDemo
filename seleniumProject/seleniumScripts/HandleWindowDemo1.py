import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonProject.pythonUtilities.datetimedemo import utility

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(2)
parent_window=driver.current_window_handle
print(type(parent_window))
print("Parent window handle: ",parent_window)
beforeSwitchParent_title=driver.title
print(beforeSwitchParent_title)
driver.find_element(By.XPATH, "//img[@alt='OrangeHRM on twitter']").click()
child_windows=driver.window_handles
print(type(child_windows))
print("Type of all windows: ",child_windows)

for child in child_windows:
    print(child)
    if parent_window!=child:
        print("Switching to new window/tab")
        driver.switch_to.window(child)
        print(driver.title)
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//input[@enterkeyhint='search']").send_keys("Nikhil Shukla")
        driver.close()


driver.switch_to.window(parent_window)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
afterSwitchParent_title=driver.title
print(driver.title)
assert beforeSwitchParent_title==afterSwitchParent_title, "Fail"
print("Pass")
driver.quit()


