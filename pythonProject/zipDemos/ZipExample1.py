print(dir(__builtins__))
print(zip)

name=["nikhil","mukesh","chhaya"] #arguments should be same in both lists to zip it
marks=[70,80,60]
address=["ABC","XYZ","DEMO"]

#name.append(marks)
#print(name)

data=zip(name,marks,address)
mydata=list(data)
print(mydata)

l1=[1,2,3,4] #works with single list too
print(list(zip(l1)))