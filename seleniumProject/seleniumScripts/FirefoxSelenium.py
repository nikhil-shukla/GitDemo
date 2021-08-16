from selenium import webdriver

driver=webdriver.Firefox(executable_path="F:/Study/SeleniumWebDrivers/geckodriver.exe")
driver.get("http://www.google.com")
print(driver.title)
print(driver.current_url)
driver.quit()