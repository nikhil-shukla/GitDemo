#Lambda- small anonymous functions
#normal approach

l1=range(9)
l2=[1,5,7,9]

def sqr(num):
    print(num*num)

sqr(5)
for x in l1:
    sqr(x)

for x in l2:
    sqr(x)


str1="abc4523fhhgfd"
print(str1.count('h'))