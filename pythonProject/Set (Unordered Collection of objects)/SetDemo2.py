mySet={98,25,8,96,2,888,2,2,"nikhil",15.26}
print(mySet)
mySet2=mySet.copy()
mySet.clear()
print(mySet) #will return set constructor - empty one
print(mySet2)

print("**************************************")

#set constructor
set1=set(["nikhil",1,2,3,4]) #passing list in set constructor
print(set1)

set2=set(("nikhil","python","java",78,89)) #passing tuple in set constructor
print(set2)
