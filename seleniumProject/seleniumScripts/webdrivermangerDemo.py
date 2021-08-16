from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome("F:/Study/SeleniumWebDrivers/chromedriver.exe")
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://facebook.com/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(3)
driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("Jacob")
driver.find_element(By.NAME, "reg_email__").send_keys("johnjacob@gamil.com")
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("johnjacob@gamil.com")
driver.find_element(By.ID, "password_step_input").send_keys("johnjacob123")

day = Select(driver.find_element(By.ID, "day"))
day.select_by_visible_text("9")

month = Select(driver.find_element(By.ID, "month"))
month.select_by_visible_text("Oct")

year = Select(driver.find_element(By.ID, "year"))
year.select_by_visible_text("2000")

driver.find_element(By.XPATH, "//label[text()='Male']/..//input").click()

driver.get_screenshot_as_file("facebook.png")

driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()