import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonProject.pythonUtilities.datetimedemo import utility

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//i[contains(@id,'profile')]").click()
driver.find_element(By.XPATH, "//li[text()='Sign In/Sign Up']").click()

#this element is in iframe
#Nosuchelement exception if we dnt switch

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
# driver.switch_to.parent_frame() #to again access the same page
parent=driver.current_window_handle
childs=driver.window_handles

for child in childs:
    if parent!=child:
        driver.switch_to.window(child)
        driver.find_element(By.ID,"identifierId").send_keys("NikhilShukla")
        time.sleep(2)
        driver.close()

#driver.switch_to.parent_frame()
#driver.switch_to.window(parent)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
frameText=driver.find_element(By.XPATH,"//div[contains(text(),'Smarter')]").text
print(frameText)
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"//a[@id='cars']").click()

assert driver.find_element(By.XPATH,"//div[contains(text(),'Commuting within the City?')]").is_displayed(),"Failed"
print("Passed")
driver.quit()