assert "Selenium" in "Selenium is for Web Automation","Validation Failed"
print("Validation 1 passed")

str1="Python"
str2="Python"

assert str1==str2,"String matching failed"
print("Validation 2 passed")

assert "Selenium" in ["Selenium","Java","JS"],"Selenium is not present"
print("Validation 3 passed")

import math

assert math.sqrt(4)==3,"Value is wrong"
print("Validation 4 passed")