list1=[12,78,98,89,98,98]
print(list1[-2])
print(list1.count(98))

print(list1[1:3]) #after colon value wont be included, its just a stopper

list1[0]=666
print(list1)

list1.append(46) #add the value at the last
list1.append('Nikhil')
list1.append('Python')
print(list1)

list1.insert(0,555)
list1.insert(2,444)
print(list1)