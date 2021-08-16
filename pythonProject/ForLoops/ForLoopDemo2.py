sent="I love Python"

for i in sent:
    print(i)

sent={10,30,90,"Nikhil",90.0,"Python",10,10}
for x in sent:
    print(x)

mydict={1:"Nikhil",2:"python","name":"shukla"}
for a,b in mydict.items(): #to fetch values in 2 variables
    print(a)
    print(b)

for a in mydict.values(): #only values
    print(a)

for a in mydict.keys(): #only keys
    print(a)

for a in mydict.items(): #all key values
    print(a)