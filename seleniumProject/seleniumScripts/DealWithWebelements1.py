from selenium import webdriver

driver=webdriver.Chrome(executable_path="F:/Study/SeleniumWebDrivers/chromedriver.exe")
#print(type(driver))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
username=driver.find_element_by_name("txtUsername")
#print(type(username))
print(username.is_enabled())
print(username.is_displayed())
username.clear()
print(username.get_attribute("id"))
print(username.value_of_css_property("font-size"))
username.send_keys("Admin")
pwd=driver.find_element_by_id("txtPassword")
pwd.send_keys("admin123")
loginbtn=driver.find_element_by_class_name("button")
loginbtn.click()
driver.implicitly_wait(1000)
print(driver.title)
assert "OrangeHRM" in driver.title,"Failed"
print("Passed")
driver.quit()

