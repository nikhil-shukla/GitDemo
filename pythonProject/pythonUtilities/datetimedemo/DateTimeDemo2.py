import datetime

current_time=datetime.datetime.now()

print(current_time.strftime("%a"))
print(current_time.strftime("%A"))
print(current_time.strftime("%w"))

print(current_time.strftime("%d_%m_%Y_%H_%M_%S"))