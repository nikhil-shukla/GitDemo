#even odd program using list and loop

evenList=[]
oddList=[]

for x in range(100):
    if x%2 ==0:
        evenList.append(x)
    else:
        oddList.append(x)
print(evenList)
print(oddList)