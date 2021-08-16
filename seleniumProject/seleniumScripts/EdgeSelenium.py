from selenium import webdriver

driver=webdriver.Edge(executable_path="F:/Study/SeleniumWebDrivers/msedgedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
print(driver.current_url)
driver.quit()