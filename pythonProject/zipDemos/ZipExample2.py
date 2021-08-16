#zipping

name={"nikhil","mukesh","chhaya"} #arguments should be same in both lists to zip it
marks={70,80,60}
address={"ABC","XYZ","DEMO"}
data=zip(name,marks,address)
mydata=set(data)
print(mydata)



#unzipping

a,b,c =zip(*mydata)
print(a)
print(b)
print(c)

for x,y,z in list(zip(name,marks,address)):
    print(x,y,z)
