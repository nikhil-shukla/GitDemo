from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://en-gb.facebook.com/")
time.sleep(1)
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(3)
month = driver.find_element(By.ID, "month")
m = Select(month)
mlist = m.options

default = m.first_selected_option
print("First option is: ", default.text)
assert "Mar" in default.text, "Failed"
print("Passed")

print(len(mlist))

for ele in mlist:
    print("Value is: ", ele.text)

    if ele.text == "Nov":
        ele.click()
        break

driver.quit()
