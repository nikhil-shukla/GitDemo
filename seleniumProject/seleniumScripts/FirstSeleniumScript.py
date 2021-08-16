from selenium import webdriver

driver=webdriver.Chrome(executable_path="F:/Study/SeleniumWebDrivers/chromedriver.exe")
#print(type(driver))
driver.maximize_window()
driver.get("http://www.google.com")
driver.implicitly_wait(1000)
myPageTitle=driver.title
print(myPageTitle)
#print(driver.quit)
driver.get_screenshot_as_file("google.png")
assert "Google" in myPageTitle,"Google not found"
print("Validation passed")
driver.quit()