#Syntax 1
tup1=(1,"python",98.0,True,1,1,1,"QA",2,2,2)
print(tup1)

#Indexing
print(tup1[1])
print(tup1[-2])
print(tup1.count(1)) #internally python consider true as 1 therfore we are having 5 times 1
print(tup1.count(2))

print((tup1.index(98.0)))

#Slicing
print(tup1[0:4])
print(tup1[::-1])

print("****************************************************")

#add
#tup1[0]="nikhil" #tuple is immutable
#print(tup1)

print(type(tup1))