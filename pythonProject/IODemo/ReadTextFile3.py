#Contextmanager usage
#with block of code will automatically close the file

import os
filepath=os.getcwd()
print(filepath)
file=os.path.dirname((filepath))
print(file)
with open(file+"\DemoNew.txt") as f:
    print("Current state is ",f.closed)
    data=f.read()
    print(data)

print("File state is",f.closed)
