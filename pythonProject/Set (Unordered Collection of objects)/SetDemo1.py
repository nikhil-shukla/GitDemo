mySet={98,25,8,96,2,888,2,2}
print(mySet)
print(len(mySet))
mySet.add(777)
print(mySet)

mySet.pop() #random value removal
print(mySet)

mySet.remove(25) #specific value
print(mySet)

mySet.discard(25) #if value doesnt exist it wont throw Key error
print(mySet)

