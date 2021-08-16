tup1=(1,"python",98.0,True,1,1,1,"QA",2,2,2)
print(tup1)
print(type(tup1))

#converting tuple into list
l1=list(tup1)
print(l1)
print(type(l1))

#converting tuple into set
s1=set(tup1)
print(s1)
print(type(s1))

print("**********************************************")

#Example for interview
tup2=("nikhil")
print(tup2)
print(len(tup2)) #counting charcater by character string and providing length

tup3=("nikhil",) #after separating by comma its treated as single entity
print(tup3)
print(len(tup3))

#Interview question - list of tuples
l2=[(1,2,3),(5,8,9),(11,8,9)]
print(l2)
print(l2[1])
print(l2[1][2])