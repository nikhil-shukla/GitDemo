from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("Bh")
time.sleep(5)
l1 = driver.find_elements(By.XPATH, "//li[contains(@id,'react-autosuggest-1-suggestion')]//div[@class='mainTxt clearfix']//span")
print(len(l1))
for ele in l1:
    print(ele.text)

    if "Bhopal" in ele.text:
        print("Record found")
        ele.click()
        break

#   if ele.text == "Bhopal":
#       print("Record found")
#       ele.click()
#       break


driver.quit()