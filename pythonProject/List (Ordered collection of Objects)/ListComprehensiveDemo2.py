import os

print((os.listdir(".")))
list=os.listdir(".")
print([x for x in list if x.endswith(".py")])