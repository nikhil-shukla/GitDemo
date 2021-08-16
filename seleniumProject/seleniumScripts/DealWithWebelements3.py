from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# s=Service("F:/Study/SeleniumWebDrivers/chromedriver.exe")

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
# driver.find_element(By.ID,"txtPassword").send_keys("admin123")
# driver.find_element(By.CLASS_NAME,"button").click()

# different locators apart from the one earlier used

driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input#txtPassword").send_keys("admi123")
driver.find_element(By.NAME, "Submit").click()
driver.implicitly_wait(2000)
print(driver.title)
assert "OrangeHRM" in driver.title, "Failed"
print("Passed")
print("Before login URL: ", driver.current_url)
assert "dashboard" in driver.current_url
driver.find_element(By.XPATH, "//a[contains(text(),'Welcome')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
time.sleep(2)
print("after logout url: ", driver.current_url)
assert "login" in driver.current_url
driver.quit()
