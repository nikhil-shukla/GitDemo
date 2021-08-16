list1=[12,78,98,89,98,98]
print(list1)
list2=["Nikhil","Shukla","Python","Java","Selenium"]
list3="nik"
print(list2)
list1.extend(list2)
print(list1)
#print(list1.extend(list3)) #extend method wont return anything

list1.extend(list3)
print(list1)

list2.pop() #last element will be removed
print(list2)

list2.pop(1)
print(list2)

list2.remove("Java")
print(list2)