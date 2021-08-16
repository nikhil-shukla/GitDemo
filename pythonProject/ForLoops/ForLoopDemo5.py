#tuple unpacking using loops

t1=(1,2,3)
t2=(5,6,88)
t3=(100,200,300)

l1=[t1,t2,t3]
print (l1)

for x in l1:
    print(x)
    print(x[0])
    print(x[1])
    print(x[2])

#tuple unpacking
for x,y,z in l1:
    print(x)
    print(y)
    print(z)