#example1
number=input("please enter number: ")
num=int(number)
def check_even_number(num):
    result=num%2==0
    print(result)

check_even_number(num)


#example2
def check_odd_number(list1):
    even_number=[]
    odd_number=[]

    for x in list1:
        if x%2==0:
            pass
           # even_number.append(x)
        else:
           # pass
            odd_number.append(x)
    return odd_number

result=check_odd_number([4,64,128])

if len(result)>0:
    print(result)
else:
    print("sorry no odd number found")